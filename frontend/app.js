const API = '';

// ── Klokke ─────────────────────────────────────────────────────────────────
function tickClock() {
  const n = new Date();
  document.getElementById('clock-time').textContent =
    n.toLocaleTimeString('no-NO', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  document.getElementById('clock-date').textContent =
    n.toLocaleDateString('no-NO', { weekday: 'short', day: 'numeric', month: 'short' });
}
setInterval(tickClock, 1000);
tickClock();

// ── API ─────────────────────────────────────────────────────────────────────
async function get(path) {
  const r = await fetch(API + path);
  if (!r.ok) throw new Error(await r.text());
  return r.json();
}
async function post(path, body = {}) {
  const r = await fetch(API + path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!r.ok) throw new Error(await r.text());
  return r.json();
}
async function del(path) {
  const r = await fetch(API + path, { method: 'DELETE' });
  return r.json();
}

// ── Toast ───────────────────────────────────────────────────────────────────
let toastTimer;
function toast(msg) {
  const el = document.getElementById('toast');
  el.textContent = msg;
  el.classList.remove('hidden');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.add('hidden'), 3200);
}

// ── Tab-navigasjon ──────────────────────────────────────────────────────────
const BREADCRUMBS = {
  hendelser: 'Hendelser', situasjon: 'Situasjonsbilde',
  tiltakskort: 'Tiltakskort', smitte: 'Smittesporing',
  logg: 'Hendelseslogg', ressurser: 'Ressursoversikt', kontakter: 'Kontakter',
};

document.querySelectorAll('.nav-item').forEach(btn => {
  btn.addEventListener('click', () => switchTab(btn.dataset.tab));
});

function switchTab(tabId) {
  document.querySelectorAll('.nav-item').forEach(b => b.classList.toggle('active', b.dataset.tab === tabId));
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.getElementById(`tab-${tabId}`).classList.add('active');
  document.getElementById('topbar-breadcrumb').innerHTML =
    `<span class="breadcrumb-page">${BREADCRUMBS[tabId] || tabId}</span>`;

  if (tabId === 'situasjon') { oppdaterSituasjon().then(() => { if (ressursKart) setTimeout(() => ressursKart.invalidateSize(), 50); }); }
  if (tabId === 'logg')      lastLogg();
  if (tabId === 'smitte')    lastSmitte();
  if (tabId === 'ressurser') lastRessurser();
  if (tabId === 'kontakter') lastKontakter();
}

// ── Modaler ─────────────────────────────────────────────────────────────────
function openModal(id) { document.getElementById(id).classList.remove('hidden'); }
function closeModal(id) { document.getElementById(id).classList.add('hidden'); }
document.querySelectorAll('.modal').forEach(m =>
  m.addEventListener('click', e => { if (e.target === m) closeModal(m.id); })
);

// ── Hendelsestyper ──────────────────────────────────────────────────────────
let hendelsestyper = [];
async function lastHendelsestyper() {
  hendelsestyper = await get('/api/hendelsestyper');
  const opts = hendelsestyper.map(h => `<option value="${h.id}">${h.ikon} ${h.navn}</option>`).join('');
  document.getElementById('h-type').innerHTML = '<option value="">— Velg —</option>' + opts;
  document.getElementById('tiltakskort-velger').innerHTML =
    '<option value="">— Velg hendelsestype —</option>' + opts;
}

function oppdaterTittelForslag() {
  const ht = hendelsestyper.find(x => x.id === document.getElementById('h-type').value);
  if (ht) document.getElementById('h-tittel').value = ht.navn;
}

// ── Hendelsestype → kategori (for filter) ──────────────────────────────────
const TYPE_KAT = {
  smitteutbrudd: 'smitte', pandemi: 'smitte', matbaren: 'smitte',
  brann_sykehjem: 'helse', evakuering: 'helse', personellmangel: 'helse', legemiddelmangel: 'helse',
  strombortfall: 'infrastruktur', cyberangrep: 'infrastruktur', forurenset_vann: 'infrastruktur',
  storulykke: 'ulykke', kjemikalieutslipp: 'ulykke', ekstremvar: 'annet',
};

// ── Pills ───────────────────────────────────────────────────────────────────
function pillAlv(a) {
  const m = { lav:'green', middels:'yellow', høy:'orange', kritisk:'red' };
  return `<span class="pill pill-${m[a]||'blue'}">${a}</span>`;
}
function pillSann(s) {
  const m = { høy:'red', middels:'yellow', lav:'green' };
  return `<span class="pill pill-${m[s]||'blue'}">S: ${s}</span>`;
}
function pillKons(k) {
  const m = { kritisk:'red', alvorlig:'orange', moderat:'yellow', lav:'green' };
  return `<span class="pill pill-${m[k]||'blue'}">K: ${k}</span>`;
}
function pillStatus(s) {
  const m = { operativ:'green', tilgjengelig:'blue', begrenset:'yellow', utilgjengelig:'red' };
  return `<span class="pill pill-${m[s]||'muted'}">${s}</span>`;
}
function pillSmitte(s) {
  const m = { bekreftet:'red', mistenkt:'orange', nærkontakt:'yellow' };
  return `<span class="pill pill-${m[s]||'blue'}">${s}</span>`;
}

// ═══════════════════════════════════════════════════════════════════════════
// HENDELSER-OVERSIKT
// ═══════════════════════════════════════════════════════════════════════════
let alleScenarioer = [];
let valgtScenarioId = null;
let oversiktKart = null;
let oversiktMarkorer = {};
let aktivtDemoId = null;

async function lastHendelserOversikt() {
  alleScenarioer = await get('/api/demo/scenarioer');
  renderHendelserListe(alleScenarioer);
  initOversiktKart(alleScenarioer);
}

function filterHendelser(type, btn) {
  document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
  btn.classList.add('active');
  const filtrert = type === 'alle'
    ? alleScenarioer
    : alleScenarioer.filter(s => TYPE_KAT[s.type_id] === type || s.alvorlighetsgrad === type);
  renderHendelserListe(filtrert);
}

const LOGG_IKONER = { beslutning:'⚖️', varsling:'📡', tiltak:'✅', observasjon:'👁', møte:'🤝', hendelse:'🚨', smitte:'🦠' };

function renderHendelserListe(liste) {
  const el = document.getElementById('hendelser-liste');
  if (!liste.length) {
    el.innerHTML = '<div class="empty-state"><div class="empty-icon">🔍</div><p>Ingen hendelser matcher filteret.</p></div>';
    return;
  }
  el.innerHTML = liste.map(s => {
    const ht = hendelsestyper.find(h => h.id === s.type_id) || { ikon: '⚡' };
    const kat = TYPE_KAT[s.type_id] || 'annet';
    return `
    <div class="hendelse-item" id="hi-${s.id}" onclick="velgHendelse('${s.id}')">
      <div class="hi-ikon ${s.alvorlighetsgrad}">${ht.ikon}</div>
      <div class="hi-body">
        <div class="hi-tittel">${s.tittel}</div>
        <div class="hi-lokasjon">📍 ${s.lokasjon.split('–')[0].trim()}</div>
        <div class="hi-meta">
          ${pillAlv(s.alvorlighetsgrad)}
          <span class="pill pill-muted">${kat}</span>
        </div>
      </div>
      <div class="hi-right">
        <div class="hi-stats">
          <span class="hi-stat">📝 ${s.antall_logg}</span>
          ${s.antall_smitte ? `<span class="hi-stat">🦠 ${s.antall_smitte}</span>` : ''}
        </div>
      </div>
    </div>`;
  }).join('');
}

function velgHendelse(id) {
  document.querySelectorAll('.hendelse-item').forEach(el => el.classList.remove('selected'));
  document.getElementById(`hi-${id}`)?.classList.add('selected');
  valgtScenarioId = id;

  // Pan kart til markøren
  const m = oversiktMarkorer[id];
  if (m && oversiktKart) {
    oversiktKart.flyTo(m.getLatLng(), 14, { animate: true, duration: 0.6 });
    m.openPopup();
  }

  // Skjul hint
  document.querySelector('.kart-hint')?.remove();
}

function initOversiktKart(scenarioer) {
  const el = document.getElementById('hendelser-kart');
  el.innerHTML = '';

  if (oversiktKart) { oversiktKart.remove(); oversiktKart = null; }
  oversiktMarkorer = {};

  oversiktKart = L.map('hendelser-kart', { zoomControl: true })
    .setView([59.9050, 10.5300], 11);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="https://carto.com">CARTO</a> © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 18,
  }).addTo(oversiktKart);

  setTimeout(() => oversiktKart.invalidateSize(), 100);


  const farge = { lav:'#34d399', middels:'#fbbf24', høy:'#fb923c', kritisk:'#f87171' };

  scenarioer.forEach(s => {
    if (!s.lat || !s.lon) return;
    const ht = hendelsestyper.find(h => h.id === s.type_id) || { ikon: '⚡' };
    const c = farge[s.alvorlighetsgrad] || '#5b7ff7';

    const ikon = L.divIcon({
      className: '',
      html: `<div style="
        background:${c};
        border:3px solid #0d0f18;
        border-radius:50%;
        width:38px;height:38px;
        display:flex;align-items:center;justify-content:center;
        font-size:17px;
        box-shadow:0 2px 12px ${c}66;
        cursor:pointer;
        transition:transform .15s;
      ">${ht.ikon}</div>`,
      iconSize: [38, 38],
      iconAnchor: [19, 19],
      popupAnchor: [0, -22],
    });

    const popup = `
      <div style="min-width:200px">
        <div style="font-weight:700;font-size:13px;margin-bottom:6px;line-height:1.3">${s.tittel}</div>
        <div style="font-size:11px;color:#8b91b8;margin-bottom:8px">📍 ${s.lokasjon.split(',')[0]}</div>
        <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px">
          <span style="padding:2px 8px;border-radius:20px;font-size:10px;font-weight:700;background:${c}22;color:${c};border:1px solid ${c}44">${s.alvorlighetsgrad.toUpperCase()}</span>
        </div>
        <div style="font-size:11px;color:#8b91b8">📝 ${s.antall_logg} loggoppf. ${s.antall_smitte ? '&nbsp;🦠 ' + s.antall_smitte + ' tilfeller' : ''}</div>
        <button onclick="lastDemo('${s.id}')" style="
          margin-top:10px;width:100%;
          background:#5b7ff7;color:#fff;border:none;border-radius:6px;
          padding:6px;font-size:12px;font-weight:600;cursor:pointer;
        ">Last inn scenario →</button>
      </div>`;

    const marker = L.marker([s.lat, s.lon], { icon: ikon })
      .addTo(oversiktKart)
      .bindPopup(popup, { maxWidth: 260 });

    marker.on('click', () => {
      document.querySelectorAll('.hendelse-item').forEach(el => el.classList.remove('selected'));
      document.getElementById(`hi-${s.id}`)?.classList.add('selected');
      document.getElementById(`hi-${s.id}`)?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      document.querySelector('.kart-hint')?.remove();
    });

    oversiktMarkorer[s.id] = marker;
  });

  // Bærum-grense polygon (forenklet)
  const bærum = [
    [59.9640,10.4380],[59.9550,10.6200],[59.9000,10.6600],
    [59.8700,10.6200],[59.8650,10.5100],[59.8800,10.4400],
    [59.9200,10.4100],[59.9640,10.4380]
  ];
  L.polygon(bærum, {
    color: '#5b7ff7',
    weight: 1.5,
    fillColor: '#5b7ff7',
    fillOpacity: 0.04,
    dashArray: '6 4',
  }).addTo(oversiktKart).bindTooltip('Bærum kommune', { permanent: false, className: '' });
}

// ═══════════════════════════════════════════════════════════════════════════
// DEMO-SCENARIOER
// ═══════════════════════════════════════════════════════════════════════════
async function lastDemoScenarioer() {
  const scenarioer = await get('/api/demo/scenarioer');
  document.getElementById('demo-knapper').innerHTML = scenarioer.map(s =>
    `<button class="demo-btn" id="demo-${s.id}" onclick="lastDemo('${s.id}')">${s.navn}</button>`
  ).join('');
}

async function lastDemo(id) {
  document.querySelectorAll('.demo-btn').forEach(b => b.classList.remove('aktiv'));
  document.getElementById(`demo-${id}`)?.classList.add('aktiv');
  aktivtDemoId = id;

  await post(`/api/demo/last/${id}`);

  // Ødelegg ressurskart og smittekart så de re-initialiseres
  if (ressursKart) { ressursKart.remove(); ressursKart = null; }
  if (smitteKart)  { smitteKart.remove();  smitteKart  = null; }

  await oppdaterSituasjon();
  await lastLogg();
  await lastSmitte();

  switchTab('situasjon');
  toast('✓ Scenario lastet');
}

async function resetDemo() {
  await post('/api/demo/reset');
  aktivtDemoId = null;
  document.querySelectorAll('.demo-btn').forEach(b => b.classList.remove('aktiv'));
  if (ressursKart) { ressursKart.remove(); ressursKart = null; }
  if (smitteKart)  { smitteKart.remove();  smitteKart  = null; }
  await oppdaterSituasjon();
  await lastLogg();
  await lastSmitte();
  switchTab('situasjon');
  toast('Nullstilt');
}

// ═══════════════════════════════════════════════════════════════════════════
// SITUASJON
// ═══════════════════════════════════════════════════════════════════════════
async function opprettHendelse(e) {
  e.preventDefault();
  await post('/api/hendelse', {
    type_id:        document.getElementById('h-type').value,
    tittel:         document.getElementById('h-tittel').value,
    beskrivelse:    document.getElementById('h-beskrivelse').value,
    lokasjon:       document.getElementById('h-lokasjon').value,
    alvorlighetsgrad: document.getElementById('h-alvorlighet').value,
  });
  closeModal('modal-hendelse');
  e.target.reset();
  await oppdaterSituasjon();
  toast('✓ Hendelse opprettet');
}

async function avsluttHendelse() {
  if (!confirm('Avslutt aktiv hendelse?')) return;
  await del('/api/hendelse');
  if (ressursKart) { ressursKart.remove(); ressursKart = null; }
  await oppdaterSituasjon();
  toast('Hendelse avsluttet');
}

async function oppdaterSituasjon() {
  const [h, logg] = await Promise.all([get('/api/hendelse'), get('/api/logg')]);
  const harHendelse = h && h.id && h.status !== 'avsluttet';

  // Sidebar status
  const dot   = document.querySelector('.status-dot');
  const stTxt = document.querySelector('.aktiv-status span');
  const badge = document.getElementById('aktiv-badge');
  const navBadge = document.getElementById('nav-alvorlighet');

  if (!harHendelse) {
    document.getElementById('ingen-hendelse').classList.remove('hidden');
    document.getElementById('aktiv-hendelse-panel').classList.add('hidden');
    badge.classList.add('hidden');
    navBadge.classList.add('hidden');
    dot.className = 'status-dot inactive';
    stTxt.textContent = 'Ingen aktiv hendelse';
    document.getElementById('nav-logg-count').classList.add('hidden');
    return;
  }

  document.getElementById('ingen-hendelse').classList.add('hidden');
  document.getElementById('aktiv-hendelse-panel').classList.remove('hidden');

  badge.textContent = `⚠ ${h.type_navn}`;
  badge.className = `aktiv-badge ${h.alvorlighetsgrad}`;

  navBadge.textContent = h.alvorlighetsgrad;
  navBadge.className = `nav-badge pill pill-${{lav:'green',middels:'yellow',høy:'orange',kritisk:'red'}[h.alvorlighetsgrad]}`;
  navBadge.classList.remove('hidden');

  dot.className = `status-dot ${h.alvorlighetsgrad === 'kritisk' ? 'kritisk' : 'active'}`;
  stTxt.textContent = h.type_navn;

  const loggCount = document.getElementById('nav-logg-count');
  loggCount.textContent = logg.length;
  loggCount.classList.remove('hidden');

  // Hero
  const hero = document.getElementById('hendelse-kort');
  hero.className = `hendelse-hero ${h.alvorlighetsgrad}`;
  hero.innerHTML = `
    <div class="hero-ikon">${h.ikon}</div>
    <div class="hero-tittel">${h.tittel}</div>
    <div class="hero-type">${h.type_navn}</div>
    <div class="hero-meta">
      <span class="hero-meta-item">📍 ${h.lokasjon}</span>
      <span class="hero-meta-item">🕐 ${h.opprettet.slice(0,16).replace('T',' ')}</span>
      <span class="hero-meta-item">${pillAlv(h.alvorlighetsgrad)}</span>
    </div>`;

  // Hent smitte og tiltak parallelt for situasjonsbilde
  const [smitte, tiltak] = await Promise.all([get('/api/smitte'), get('/api/tiltak')]);
  const nBekreftet   = smitte.filter(s => s.status === 'bekreftet').length;
  const nMistenkt    = smitte.filter(s => s.status === 'mistenkt').length;
  const nKontakter   = smitte.filter(s => s.status === 'nærkontakt').length;
  const nTiltakOK    = tiltak.filter(t => t.status === 'fullført').length;
  const nTiltakPagar = tiltak.filter(t => t.status === 'pågår').length;

  // Statuskort
  const harSmitte = smitte.length > 0;
  document.getElementById('situasjon-oversikt').innerHTML = `
    <div class="data-row"><span class="data-row-label">Type hendelse</span><strong>${h.type_navn}</strong></div>
    <div class="data-row"><span class="data-row-label">Lokasjon</span><strong>${h.lokasjon.split(',')[0]}</strong></div>
    <div class="data-row"><span class="data-row-label">Alvorlighetsgrad</span>${pillAlv(h.alvorlighetsgrad)}</div>
    <div class="data-row"><span class="data-row-label">Status</span><span class="pill pill-green">Aktiv</span></div>
    <div class="data-row"><span class="data-row-label">Loggoppføringer</span><strong>${logg.length}</strong></div>
    ${harSmitte ? `
    <div style="margin-top:12px;padding-top:12px;border-top:1px solid var(--border)">
      <div style="font-size:11px;color:var(--text3);text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px">Smittesituasjon</div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px">
        <div class="mini-stat-kort red"><div class="mini-stat-tall">${nBekreftet}</div><div class="mini-stat-label">Bekreftet</div></div>
        <div class="mini-stat-kort orange"><div class="mini-stat-tall">${nMistenkt}</div><div class="mini-stat-label">Mistenkt</div></div>
        <div class="mini-stat-kort yellow"><div class="mini-stat-tall">${nKontakter}</div><div class="mini-stat-label">Nærkontakter</div></div>
      </div>
    </div>` : ''}
    ${tiltak.length ? `
    <div style="margin-top:10px">
      <div style="font-size:11px;color:var(--text3);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px">Tiltaksstatus</div>
      <div style="display:flex;gap:8px;font-size:12px">
        <span style="color:#34d399">✅ ${nTiltakOK} fullført</span>
        <span style="color:#fbbf24">🔄 ${nTiltakPagar} pågår</span>
        <span style="color:var(--text3)">📋 ${tiltak.length - nTiltakOK - nTiltakPagar} planlagt</span>
      </div>
    </div>` : ''}
  `;

  // ROS
  try {
    const kort = await get(`/api/tiltakskort/${h.type_id}`);
    document.getElementById('ros-liste').innerHTML = kort.ros_risikoer.map(r => `
      <div class="data-row">
        <span class="data-row-label">${r.risiko}</span>
        <div class="data-row-pills">${pillSann(r.sannsynlighet)}${pillKons(r.konsekvens)}</div>
      </div>`).join('');
  } catch(_) {}

  // Ressurskart
  await renderRessursKart(h);

  // Siste logg
  document.getElementById('situasjon-logg').innerHTML =
    logg.slice(0, 5).map(loggHTML).join('') ||
    '<p style="color:var(--text3);font-size:12px;padding:8px 0">Ingen oppføringer ennå.</p>';
}

// ═══════════════════════════════════════════════════════════════════════════
// RESSURSKART (situasjon-siden)
// ═══════════════════════════════════════════════════════════════════════════
let ressursKart = null;

const RESSURS_CFG = {
  helse:       { farge:'#5b7ff7', emoji:'🏥' },
  institusjon: { farge:'#34d399', emoji:'🏠' },
  krise:       { farge:'#fbbf24', emoji:'🚨' },
  frivillig:   { farge:'#a78bfa', emoji:'🤝' },
  transport:   { farge:'#f87171', emoji:'🚑' },
};

async function renderRessursKart(hendelse) {
  const ressurser = await get('/api/ressurser');
  const alle = [
    ...(ressurser.helse     || []),
    ...(ressurser.frivillig || []),
    ...(ressurser.transport || []),
  ];

  // Alltid destruer og gjenskap for å unngå størrelsesproblemer
  if (ressursKart) { ressursKart.remove(); ressursKart = null; }

  ressursKart = L.map('kart', { zoomControl: true }).setView([59.9050, 10.5300], 12);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="https://carto.com">CARTO</a> © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 18,
  }).addTo(ressursKart);

  // Tving størrelsesjustering etter at DOM er ferdig oppdatert
  setTimeout(() => ressursKart.invalidateSize(), 100);

  alle.forEach(r => {
    const cfg = RESSURS_CFG[r.type] || { farge:'#8b91b8', emoji:'📍' };
    const ikon = L.divIcon({
      className: '',
      html: `<div style="background:${cfg.farge};border:2px solid #0d0f18;border-radius:50%;width:30px;height:30px;display:flex;align-items:center;justify-content:center;font-size:13px;box-shadow:0 2px 8px ${cfg.farge}55;">${cfg.emoji}</div>`,
      iconSize: [30, 30], iconAnchor: [15, 15], popupAnchor: [0, -18],
    });
    L.marker([r.lat, r.lon], { icon: ikon }).addTo(ressursKart)
      .bindPopup(`<b>${cfg.emoji} ${r.navn}</b><br><span style="color:#8b91b8;font-size:11px">${r.adresse}</span><br>${r.kapasitet} · ${pillStatus(r.status)}<br><b style="color:#34d399">📞 ${r.kontakt}</b>`);
  });

  // Hendelsesmarkør
  if (hendelse?.id) {
    const hIkon = L.divIcon({
      className: '',
      html: `<div style="background:#f87171;border:3px solid #fff;border-radius:50%;width:40px;height:40px;display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 0 0 0 rgba(248,113,113,.6);animation:pulse-map 2s infinite;">${hendelse.ikon||'🚨'}</div>`,
      iconSize: [40,40], iconAnchor: [20,20], popupAnchor: [0,-22],
    });
    L.marker([59.8893, 10.5214], { icon: hIkon }).addTo(ressursKart)
      .bindPopup(`<b>⚠ ${hendelse.tittel}</b><br><i style="color:#8b91b8">${hendelse.lokasjon.split(',')[0]}</i>`).openPopup();
  }

  // Legend
  const existingLegend = document.querySelector('.leaflet-control-custom-legend');
  if (existingLegend) existingLegend.remove();

  const legend = L.control({ position: 'bottomright' });
  legend.onAdd = () => {
    const d = L.DomUtil.create('div', 'leaflet-control-custom-legend');
    d.style.cssText = 'background:rgba(19,22,32,.95);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:10px 14px;font-size:11px;color:#eef0f8;line-height:1.8;backdrop-filter:blur(8px);';
    d.innerHTML = '<b style="display:block;margin-bottom:4px;font-size:10px;color:#565c82;text-transform:uppercase;letter-spacing:.06em">Ressurstype</b>' +
      Object.entries(RESSURS_CFG).map(([k,v]) =>
        `<div style="display:flex;align-items:center;gap:7px"><div style="width:12px;height:12px;border-radius:50%;background:${v.farge}"></div>${v.emoji} ${k}</div>`
      ).join('');
    return d;
  };
  legend.addTo(ressursKart);
}

// ═══════════════════════════════════════════════════════════════════════════
// HENDELSESLOGG
// ═══════════════════════════════════════════════════════════════════════════
const LOGG_IKONER2 = { beslutning:'⚖️', varsling:'📡', tiltak:'✅', observasjon:'👁', møte:'🤝', hendelse:'🚨', smitte:'🦠' };

function loggHTML(entry) {
  const tid = entry.tidspunkt.slice(0,16).replace('T',' ');
  const type = entry.type || 'observasjon';
  return `
    <div class="logg-item">
      <div class="logg-dot-col">
        <div class="logg-dot ${type}">${LOGG_IKONER2[type]||'📝'}</div>
        <div class="logg-line"></div>
      </div>
      <div class="logg-body">
        <div class="logg-meta">
          <span class="logg-tid">${tid}</span>
          <span class="pill pill-muted" style="font-size:9px">${type}</span>
        </div>
        <div class="logg-tittel">${entry.tittel}</div>
        ${entry.tekst ? `<div class="logg-tekst">${entry.tekst}</div>` : ''}
        <div class="logg-bruker">— ${entry.bruker}</div>
      </div>
    </div>`;
}

async function lastLogg() {
  const logg = await get('/api/logg');
  const el = document.getElementById('logg-innhold');
  el.innerHTML = logg.length
    ? `<div class="card">${logg.map(loggHTML).join('')}</div>`
    : '<div class="empty-state"><div class="empty-icon">📝</div><p>Ingen loggoppføringer ennå.</p></div>';

  const cnt = document.getElementById('nav-logg-count');
  cnt.textContent = logg.length;
  cnt.classList.toggle('hidden', logg.length === 0);
}

async function leggTilLogg(e) {
  e.preventDefault();
  await post('/api/logg', {
    type:   document.getElementById('l-type').value,
    tittel: document.getElementById('l-tittel').value,
    tekst:  document.getElementById('l-tekst').value,
    bruker: document.getElementById('l-bruker').value,
  });
  closeModal('modal-logg');
  e.target.reset();
  await lastLogg();
  toast('✓ Loggoppføring lagret');
}

// ═══════════════════════════════════════════════════════════════════════════
// TILTAKSKORT
// ═══════════════════════════════════════════════════════════════════════════
async function lastTiltakskort(typeId) {
  const el = document.getElementById('tiltakskort-innhold');
  if (!typeId) {
    el.innerHTML = '<div class="empty-state"><div class="empty-icon">📋</div><p>Velg hendelsestype over.</p></div>';
    return;
  }
  const k = await get(`/api/tiltakskort/${typeId}`);
  el.innerHTML = `
    <div class="tiltak-grid">
      <div class="card">
        <div class="card-title">⚡ Umiddelbare tiltak</div>
        <ol class="tiltak-liste">${k.umiddelbare_tiltak.map((t,i) => `<li><span class="tiltak-nr">${i+1}</span>${t}</li>`).join('')}</ol>
      </div>
      <div class="card">
        <div class="card-title">📡 Varslingsrutiner</div>
        <ol class="tiltak-liste">${k.varslingsrutiner.map((t,i) => `<li><span class="tiltak-nr">${i+1}</span>${t}</li>`).join('')}</ol>
      </div>
    </div>
    <div class="card">
      <div class="card-title">👥 Roller og ansvar</div>
      <div>${k.roller.map(r => `<div class="rolle-item"><div class="rolle-tittel">${r.rolle}</div><div class="rolle-ansvar">${r.ansvar}</div></div>`).join('')}</div>
    </div>
    <div class="card">
      <div class="card-title">⚠ ROS – Risikovurdering</div>
      ${k.ros_risikoer.map(r => `<div class="data-row"><span class="data-row-label">${r.risiko}</span><div class="data-row-pills">${pillSann(r.sannsynlighet)}${pillKons(r.konsekvens)}</div></div>`).join('')}
    </div>`;
}

// ═══════════════════════════════════════════════════════════════════════════
// RESSURSER
// ═══════════════════════════════════════════════════════════════════════════
async function lastRessurser() {
  const data = await get('/api/ressurser');
  const seks = [
    { key:'helse',     tittel:'🏥 Helse og omsorg' },
    { key:'frivillig', tittel:'🤝 Frivillige og Sivilforsvaret' },
    { key:'transport', tittel:'🚑 Transport og ambulanse' },
  ];
  document.getElementById('ressurser-innhold').innerHTML = seks.map(s => `
    <div class="card">
      <div class="card-title">${s.tittel}</div>
      <div class="ressurs-grid">
        ${(data[s.key]||[]).map(r => {
          const cfg = RESSURS_CFG[r.type] || { emoji:'📍' };
          return `<div class="ressurs-item">
            <div class="ressurs-ikon">${cfg.emoji}</div>
            <div>
              <div class="ressurs-navn">${r.navn}</div>
              <div class="ressurs-info">${r.kapasitet} · ${r.adresse.split(',')[0]}</div>
              <div style="margin-top:4px">${pillStatus(r.status)}</div>
            </div>
            <div class="ressurs-tlf">📞 ${r.kontakt}</div>
          </div>`;
        }).join('')}
      </div>
    </div>`).join('');
}

// ═══════════════════════════════════════════════════════════════════════════
// KONTAKTER
// ═══════════════════════════════════════════════════════════════════════════
let alleKontakter = [];
async function lastKontakter() {
  alleKontakter = await get('/api/kontakter');
  renderKontakter(alleKontakter);
}
function renderKontakter(liste) {
  const grupper = [
    { key:'kommunal',     tittel:'Kommunal kriseledelse – Bærum' },
    { key:'statlig',      tittel:'Statlige myndigheter' },
    { key:'nodetater',    tittel:'Nødetater og sykehus' },
    { key:'infrastruktur',tittel:'Infrastruktur' },
  ];
  document.getElementById('kontakter-innhold').innerHTML = grupper.map(g => {
    const liste2 = liste.filter(k => k.kategori === g.key);
    if (!liste2.length) return '';
    return `<div class="kontakt-seksjon">
      <div class="kontakt-seksjon-tittel">${g.tittel}</div>
      <div class="kontakt-grid">
        ${liste2.map(k => `
          <div class="kontakt-kort">
            <div>
              <div class="kontakt-navn">${k.navn}</div>
              <div class="kontakt-person">${k.person}</div>
            </div>
            <div style="display:flex;align-items:center;gap:8px">
              <span class="kontakt-tlf">📞 ${k.tlf}</span>
              <a href="mailto:${k.epost}" class="kontakt-epost">✉</a>
            </div>
          </div>`).join('')}
      </div>
    </div>`;
  }).join('');
}
function filterKontakter(q) {
  const ql = q.toLowerCase();
  renderKontakter(alleKontakter.filter(k =>
    k.navn.toLowerCase().includes(ql) || k.person.toLowerCase().includes(ql)
  ));
}

// ═══════════════════════════════════════════════════════════════════════════
// SMITTESPORING
// ═══════════════════════════════════════════════════════════════════════════
async function leggTilSmitte(e) {
  e.preventDefault();
  const kilde = document.getElementById('sm-kilde').value;
  await post('/api/smitte', {
    navn:          document.getElementById('sm-navn').value,
    alder:         parseInt(document.getElementById('sm-alder').value),
    kjønn:         document.getElementById('sm-kjønn').value,
    prøvedato:     document.getElementById('sm-prøve').value,
    symptomstart:  document.getElementById('sm-symptom').value || null,
    smittekilde_id:kilde ? parseInt(kilde) : null,
    lokasjon:      document.getElementById('sm-lokasjon').value,
    institusjon:   document.getElementById('sm-inst').value || null,
    status:        document.getElementById('sm-status').value,
  });
  closeModal('modal-smitte');
  e.target.reset();
  await lastSmitte();
  toast('✓ Tilfelle registrert');
}

async function slettSmitte(id) {
  await del(`/api/smitte/${id}`);
  await lastSmitte();
  toast('Tilfelle slettet');
}

async function lastSmitte() {
  const t = await get('/api/smitte');
  const bek  = t.filter(x => x.status === 'bekreftet').length;
  const mis  = t.filter(x => x.status === 'mistenkt').length;
  const nær  = t.filter(x => x.status === 'nærkontakt').length;

  document.getElementById('s-bekreftet').textContent = bek;
  document.getElementById('s-mistenkt').textContent  = mis;
  document.getElementById('s-kontakter').textContent = nær;
  document.getElementById('s-total').textContent     = t.length;

  const cnt = document.getElementById('nav-smitte-count');
  cnt.textContent = t.length;
  cnt.classList.toggle('hidden', t.length === 0);

  renderNettverkGraf(t);
  renderEpiKurve(t);
  renderBeroerteInst(t);

  const el = document.getElementById('smitte-liste');
  if (!t.length) {
    el.innerHTML = '<p style="color:var(--text3);text-align:center;padding:20px;font-size:12px">Ingen tilfeller registrert.</p>';
    return;
  }
  el.innerHTML = `<table class="smitte-tabell">
    <thead><tr>
      <th>ID</th><th>Navn</th><th>Alder</th><th>Status</th>
      <th>Lokasjon</th><th>Institusjon</th><th>Prøvedato</th><th>Kilde</th><th></th>
    </tr></thead>
    <tbody>${t.map(r => `<tr>
      <td><strong>#${r.id}</strong></td>
      <td>${r.navn}</td><td>${r.alder}år</td>
      <td>${pillSmitte(r.status)}</td>
      <td>${r.lokasjon}</td>
      <td style="color:var(--text3)">${r.institusjon||'–'}</td>
      <td style="color:var(--text3)">${r.prøvedato}</td>
      <td style="color:var(--text3)">${r.smittekilde_id ? '#'+r.smittekilde_id : '–'}</td>
      <td><button class="btn btn-sm btn-danger" onclick="slettSmitte(${r.id})">Slett</button></td>
    </tr>`).join('')}</tbody>
  </table>`;
}

// ── Smittenettverk (D3 force-directed) ─────────────────────────────────────
let nettverkSim = null;

function renderNettverkGraf(tilfeller) {
  const container = document.getElementById('smitte-nettverk');
  container.innerHTML = '';

  if (!tilfeller.length) {
    container.innerHTML = '<div class="nett-empty">Ingen tilfeller å vise</div>';
    return;
  }

  const W = container.clientWidth || 700;
  const H = 420;

  // Bygg nodes og links
  const nodes = tilfeller.map(t => ({
    id: t.id,
    navn: t.navn,
    alder: t.alder,
    status: t.status,
    institusjon: t.institusjon,
    lokasjon: t.lokasjon,
    prøvedato: t.prøvedato,
    smittekilde_id: t.smittekilde_id,
  }));

  const links = tilfeller
    .filter(t => t.smittekilde_id != null && tilfeller.find(x => x.id === t.smittekilde_id))
    .map(t => ({ source: t.smittekilde_id, target: t.id }));

  const farge = { bekreftet: '#f87171', mistenkt: '#fb923c', nærkontakt: '#fbbf24' };
  const radius = { bekreftet: 22, mistenkt: 18, nærkontakt: 15 };

  const svg = d3.select(container).append('svg')
    .attr('width', W).attr('height', H);

  // Defs: pil-markør og glow-filter
  const defs = svg.append('defs');

  defs.append('marker')
    .attr('id', 'pil')
    .attr('viewBox', '0 -4 10 8')
    .attr('refX', 32).attr('refY', 0)
    .attr('markerWidth', 7).attr('markerHeight', 7)
    .attr('orient', 'auto')
    .append('path')
    .attr('d', 'M0,-4L10,0L0,4')
    .attr('fill', 'rgba(255,255,255,.25)');

  ['bekreftet','mistenkt','nærkontakt'].forEach(st => {
    const f = defs.append('filter').attr('id', `glow-${st}`);
    f.append('feGaussianBlur').attr('stdDeviation', '3').attr('result', 'blur');
    const merge = f.append('feMerge');
    merge.append('feMergeNode').attr('in', 'blur');
    merge.append('feMergeNode').attr('in', 'SourceGraphic');
  });

  // Zoom
  const g = svg.append('g');
  const zoom = d3.zoom()
    .scaleExtent([0.3, 3])
    .on('zoom', e => g.attr('transform', e.transform));
  svg.call(zoom);
  svg._zoom = zoom; // lagre for reset

  // Bakgrunnsgrid
  const gridG = g.append('g').attr('class', 'grid');
  for (let x = 0; x < W * 2; x += 60)
    gridG.append('line').attr('x1', x).attr('y1', 0).attr('x2', x).attr('y2', H * 2)
      .attr('stroke', 'rgba(255,255,255,.025)').attr('stroke-width', 1);
  for (let y = 0; y < H * 2; y += 60)
    gridG.append('line').attr('x1', 0).attr('y1', y).attr('x2', W * 2).attr('y2', y)
      .attr('stroke', 'rgba(255,255,255,.025)').attr('stroke-width', 1);

  // Kanter
  const link = g.append('g').selectAll('line')
    .data(links).join('line')
    .attr('stroke', 'rgba(255,255,255,.2)')
    .attr('stroke-width', 1.5)
    .attr('stroke-dasharray', d => {
      const target = tilfeller.find(t => t.id === d.target.id || t.id === d.target);
      return target?.status === 'nærkontakt' ? '5 4' : null;
    })
    .attr('marker-end', 'url(#pil)');

  // Node-gruppe
  const node = g.append('g').selectAll('g')
    .data(nodes).join('g')
    .attr('cursor', 'grab')
    .call(d3.drag()
      .on('start', (e, d) => { if (!e.active) sim.alphaTarget(.3).restart(); d.fx = d.x; d.fy = d.y; })
      .on('drag',  (e, d) => { d.fx = e.x; d.fy = e.y; })
      .on('end',   (e, d) => { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; })
    );

  // Ytre glød-sirkel
  node.append('circle')
    .attr('r', d => radius[d.status] + 7)
    .attr('fill', d => farge[d.status] + '18')
    .attr('stroke', d => farge[d.status] + '40')
    .attr('stroke-width', 1);

  // Hoved-sirkel
  node.append('circle')
    .attr('r', d => radius[d.status])
    .attr('fill', d => farge[d.status] + '22')
    .attr('stroke', d => farge[d.status])
    .attr('stroke-width', 2)
    .attr('filter', d => `url(#glow-${d.status})`);

  // Emoji ikon
  node.append('text')
    .attr('text-anchor', 'middle')
    .attr('dominant-baseline', 'central')
    .attr('font-size', d => radius[d.status] * 0.9)
    .text(d => d.status === 'bekreftet' ? '🦠' : d.status === 'mistenkt' ? '⚠' : '👤');

  // ID-label under node
  node.append('text')
    .attr('y', d => radius[d.status] + 14)
    .attr('text-anchor', 'middle')
    .attr('font-size', 10)
    .attr('font-weight', '700')
    .attr('fill', d => farge[d.status])
    .text(d => `#${d.id}`);

  // Navn-label
  node.append('text')
    .attr('y', d => radius[d.status] + 26)
    .attr('text-anchor', 'middle')
    .attr('font-size', 9)
    .attr('fill', 'rgba(255,255,255,.45)')
    .text(d => d.navn.split(' ')[0]);

  // Tooltip
  const tooltip = d3.select(container).append('div').attr('class', 'nett-tooltip').style('display', 'none');

  node
    .on('mouseover', (e, d) => {
      tooltip.style('display', 'block').html(`
        <div style="font-weight:700;margin-bottom:4px">${d.navn}</div>
        <div style="color:var(--text3)">Alder: ${d.alder} år</div>
        <div>Status: <span style="color:${farge[d.status]};font-weight:600">${d.status}</span></div>
        ${d.institusjon ? `<div style="color:var(--text3)">${d.institusjon}</div>` : ''}
        <div style="color:var(--text3)">${d.lokasjon}</div>
        <div style="color:var(--text3);margin-top:3px">Prøvedato: ${d.prøvedato}</div>
        ${d.smittekilde_id ? `<div style="color:var(--text3)">Smittekilde: #${d.smittekilde_id}</div>` : '<div style="color:var(--text3)">Indekskasus</div>'}
      `);
    })
    .on('mousemove', e => {
      const rect = container.getBoundingClientRect();
      let x = e.clientX - rect.left + 14;
      let y = e.clientY - rect.top - 10;
      if (x + 230 > W) x -= 244;
      tooltip.style('left', x + 'px').style('top', y + 'px');
    })
    .on('mouseout', () => tooltip.style('display', 'none'));

  // Force-simulasjon
  if (nettverkSim) nettverkSim.stop();
  const sim = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(100).strength(0.6))
    .force('charge', d3.forceManyBody().strength(-280))
    .force('center', d3.forceCenter(W / 2, H / 2))
    .force('collision', d3.forceCollide().radius(d => radius[d.status] + 14))
    .on('tick', () => {
      link
        .attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
      node.attr('transform', d => `translate(${d.x},${d.y})`);
    });

  nettverkSim = sim;

  // Lagre zoom-referanse for reset
  container._zoom = zoom;
  container._svg  = svg;
}

function resetNettverkZoom() {
  const container = document.getElementById('smitte-nettverk');
  if (container._svg && container._zoom) {
    container._svg.transition().duration(400)
      .call(container._zoom.transform, d3.zoomIdentity);
  }
}

function renderSmittekjede(t) {
  const el = document.getElementById('smittekjede');
  const bek = t.filter(x => x.status === 'bekreftet');
  if (!bek.length) { el.innerHTML = '<p style="color:var(--text3);font-size:12px">Ingen bekreftede tilfeller.</p>'; return; }
  let html = '<div style="display:flex;flex-wrap:wrap;align-items:center;gap:4px;">';
  bek.forEach(item => {
    const kilde = t.find(x => x.id === item.smittekilde_id);
    if (kilde) html += `<span class="kjede-node bekreftet">👤 ${kilde.navn.split(' ')[0]} #${kilde.id}</span><span class="kjede-pil">→</span>`;
    html += `<span class="kjede-node ${item.status}">👤 ${item.navn.split(' ')[0]} #${item.id}${item.institusjon ? `<span style="color:var(--text3);font-size:10px;margin-left:3px">${item.institusjon.split(' ')[0]}</span>` : ''}</span>`;
    const nk = t.filter(x => x.smittekilde_id === item.id && x.status === 'nærkontakt');
    if (nk.length) html += `<span class="kjede-pil">⤵</span>${nk.map(n=>`<span class="kjede-node nærkontakt">👤 ${n.navn.split(' ')[0]} #${n.id}</span>`).join(' ')}`;
    html += ' ';
  });
  el.innerHTML = html + '</div>';
}

function renderEpiKurve(t) {
  const el = document.getElementById('epi-kurve');
  const data = t.filter(x => x.status !== 'nærkontakt');
  if (!data.length) { el.innerHTML = '<p style="color:var(--text3);font-size:12px">Ingen data for epidemiologisk kurve.</p>'; return; }

  const teller = {};
  data.forEach(x => {
    teller[x.prøvedato] = teller[x.prøvedato] || { bekreftet:0, mistenkt:0 };
    teller[x.prøvedato][x.status]++;
  });
  const datoer = Object.keys(teller).sort();
  const max = Math.max(...datoer.map(d => teller[d].bekreftet + teller[d].mistenkt)) || 1;
  const W=440, H=130, pad=28, bw=Math.max(12, Math.min(36, (W-2*pad)/datoer.length - 4));

  const bars = datoer.map((d,i) => {
    const tot = teller[d].bekreftet + teller[d].mistenkt;
    const bek = teller[d].bekreftet;
    const mis = teller[d].mistenkt;
    const bH  = (tot/max)*(H-50);
    const bkH = (bek/max)*(H-50);
    const x   = pad + i*((W-2*pad)/datoer.length);
    const y   = H-24-bH;
    return `
      <rect x="${x}" y="${H-24-bkH}" width="${bw}" height="${bkH}" fill="#f87171" rx="3" opacity=".9"><title>${d}: ${bek} bekreftet</title></rect>
      ${mis ? `<rect x="${x}" y="${y}" width="${bw}" height="${bH-bkH}" fill="#fb923c" rx="3" opacity=".9"><title>${d}: ${mis} mistenkt</title></rect>` : ''}
      <text x="${x+bw/2}" y="${H-6}" text-anchor="middle" font-size="9" fill="#565c82">${d.slice(5)}</text>
      <text x="${x+bw/2}" y="${y-4}" text-anchor="middle" font-size="10" font-weight="700" fill="#eef0f8">${tot}</text>`;
  }).join('');

  el.innerHTML = `<svg viewBox="0 0 ${W} ${H}" style="width:100%;height:${H}px">
    <text x="${W/2}" y="13" text-anchor="middle" font-size="10" fill="#565c82">Tilfeller per prøvedato</text>
    <line x1="${pad}" y1="${H-24}" x2="${W-pad}" y2="${H-24}" stroke="#212540" stroke-width="1"/>
    ${bars}
    <rect x="${W-80}" y="4" width="10" height="10" fill="#f87171" rx="2"/>
    <text x="${W-66}" y="13" font-size="9" fill="#8b91b8">Bekreftet</text>
    <rect x="${W-80}" y="18" width="10" height="10" fill="#fb923c" rx="2"/>
    <text x="${W-66}" y="27" font-size="9" fill="#8b91b8">Mistenkt</text>
  </svg>`;
}

// ═══════════════════════════════════════════════════════════════════════════
// SUB-TABS (smitte)
// ═══════════════════════════════════════════════════════════════════════════
document.querySelectorAll('.sub-tab').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.sub-tab').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.stab-content').forEach(c => { c.classList.remove('active'); c.classList.add('hidden'); });
    btn.classList.add('active');
    const stab = document.getElementById(`stab-${btn.dataset.stab}`);
    if (stab) { stab.classList.remove('hidden'); stab.classList.add('active'); }
    if (btn.dataset.stab === 'oversikt')     renderSmitkart();
    if (btn.dataset.stab === 'tiltak')       lastTiltak();
    if (btn.dataset.stab === 'eksponeringer') lastEksponeringer();
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// GEOGRAFISK SMITTEKART
// ═══════════════════════════════════════════════════════════════════════════
let smitteKart = null;

async function renderSmitkart() {
  const tilfeller = await get('/api/smitte');
  const el = document.getElementById('smitte-kart');
  if (!el) return;
  if (smitteKart) { smitteKart.remove(); smitteKart = null; }
  smitteKart = L.map('smitte-kart').setView([59.905, 10.53], 12);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 18,
  }).addTo(smitteKart);
  setTimeout(() => smitteKart.invalidateSize(), 100);

  const instCoords = {
    'Dønski bo- og behandlingssenter': [59.9088, 10.5452],
    'Østerås sykehjem': [59.9257, 10.5694],
    'Rykkinn bo- og behandlingssenter': [59.9289, 10.4794],
    'Valler VGS': [59.9205, 10.5812],
    'Valler VGS – Vg2A': [59.9205, 10.5812],
    'Fornebu International School': [59.895, 10.6198],
    'Bekkestua barneskole': [59.9127, 10.5621],
    'Restaurant Smaken': [59.8897, 10.5220],
  };

  const groups = {};
  tilfeller.forEach(t => {
    const key = t.institusjon || t.lokasjon;
    if (!groups[key]) groups[key] = { tilfeller: [], key };
    groups[key].tilfeller.push(t);
  });

  Object.values(groups).forEach(g => {
    const coords = Object.entries(instCoords).find(([k]) => g.key && g.key.includes(k.split(' ')[0]))?.[1]
      || [59.905 + (Math.random() - .5) * .04, 10.53 + (Math.random() - .5) * .06];

    const bek = g.tilfeller.filter(t => t.status === 'bekreftet').length;
    const mis = g.tilfeller.filter(t => t.status === 'mistenkt').length;
    const nær = g.tilfeller.filter(t => t.status === 'nærkontakt').length;
    const r = Math.min(30, 12 + g.tilfeller.length * 2);

    const ikon = L.divIcon({
      className: '',
      html: `<div style="background:#f87171;border:2px solid #0d0f18;border-radius:50%;width:${r*2}px;height:${r*2}px;display:flex;align-items:center;justify-content:center;font-size:${r*.7}px;font-weight:700;color:#fff;box-shadow:0 2px 8px #f8717166;">${g.tilfeller.length}</div>`,
      iconSize: [r*2, r*2], iconAnchor: [r, r], popupAnchor: [0, -r-4],
    });
    L.marker(coords, { icon: ikon }).addTo(smitteKart)
      .bindPopup(`<b>${g.key}</b><br>Bekreftet: ${bek} · Mistenkt: ${mis} · Nærkontakt: ${nær}`);
  });
}

// ═══════════════════════════════════════════════════════════════════════════
// BERØRTE INSTITUSJONER
// ═══════════════════════════════════════════════════════════════════════════
function renderBeroerteInst(tilfeller) {
  const el = document.getElementById('berorte-inst');
  if (!el) return;
  const groups = {};
  tilfeller.forEach(t => {
    const key = t.institusjon || t.lokasjon;
    if (!groups[key]) groups[key] = { navn: key, total: 0, bekreftet: 0 };
    groups[key].total++;
    if (t.status === 'bekreftet') groups[key].bekreftet++;
  });
  const sorted = Object.values(groups).sort((a, b) => b.total - a.total);
  el.innerHTML = sorted.length ? sorted.map(g => `
    <div class="inst-item">
      <div><div class="inst-navn">${g.navn}</div><div class="inst-count">${g.bekreftet} bekreftet · ${g.total} totalt</div></div>
      <div class="pill ${g.bekreftet > 3 ? 'pill-red' : 'pill-orange'}">${g.total} tilfeller</div>
    </div>`).join('') : '<p style="color:var(--text3);font-size:12px">Ingen institusjoner registrert.</p>';
}

// ═══════════════════════════════════════════════════════════════════════════
// TILTAKSOPPFØLGING
// ═══════════════════════════════════════════════════════════════════════════
const TILTAK_IKONER = { testing:'🧪', isolasjon:'🏠', kohortering:'👥', varsling:'📡', annet:'📋' };

async function lastTiltak() {
  const tiltak = await get('/api/tiltak');
  const el = document.getElementById('tiltak-liste');
  if (!el) return;
  if (!tiltak.length) {
    el.innerHTML = '<p style="color:var(--text3);font-size:12px;text-align:center;padding:20px">Ingen tiltak registrert.</p>';
    return;
  }
  const statusOrd = { planlagt: 0, pågår: 1, fullført: 2 };
  const sortert = [...tiltak].sort((a, b) => statusOrd[a.status] - statusOrd[b.status]);
  el.innerHTML = sortert.map(t => `
    <div class="tiltak-item ${t.status}">
      <div class="tiltak-kat-ikon">${TILTAK_IKONER[t.kategori] || '📋'}</div>
      <div style="flex:1">
        <div class="tiltak-tittel">${t.tittel}</div>
        ${t.beskrivelse ? `<div class="tiltak-besk">${t.beskrivelse}</div>` : ''}
        <div class="tiltak-meta">
          <span class="pill pill-muted">${t.kategori}</span>
          ${pillTiltakStatus(t.status)}
          <span style="font-size:11px;color:var(--text3)">${t.ansvarlig}</span>
          ${t.frist ? `<span style="font-size:11px;color:var(--text3)">Frist: ${t.frist}</span>` : ''}
        </div>
      </div>
      <div style="display:flex;gap:6px;flex-shrink:0">
        ${t.status !== 'fullført' ? `<button class="btn btn-ghost btn-sm" onclick="oppdaterTiltakStatus(${t.id},'${t.status === 'planlagt' ? 'pågår' : 'fullført'}')">→</button>` : ''}
        <button class="btn btn-sm btn-danger" onclick="slettTiltak(${t.id})">×</button>
      </div>
    </div>`).join('');
}

function pillTiltakStatus(s) {
  const m = { planlagt:'muted', pågår:'yellow', fullført:'green' };
  return `<span class="pill pill-${m[s] || 'muted'}">${s}</span>`;
}

async function leggTilTiltak(e) {
  e.preventDefault();
  await post('/api/tiltak', {
    kategori:    document.getElementById('t-kat').value,
    tittel:      document.getElementById('t-tittel').value,
    beskrivelse: document.getElementById('t-besk').value,
    ansvarlig:   document.getElementById('t-ansv').value,
    status:      document.getElementById('t-status').value,
    frist:       document.getElementById('t-frist').value || null,
  });
  closeModal('modal-tiltak');
  e.target.reset();
  await lastTiltak();
  toast('✓ Tiltak registrert');
}

async function oppdaterTiltakStatus(id, nyStatus) {
  await fetch(`${API}/api/tiltak/${id}/status?status=${encodeURIComponent(nyStatus)}`, { method: 'PUT' });
  await lastTiltak();
}

async function slettTiltak(id) {
  await del(`/api/tiltak/${id}`);
  await lastTiltak();
  toast('Tiltak slettet');
}

// ═══════════════════════════════════════════════════════════════════════════
// EKSPONERINGER
// ═══════════════════════════════════════════════════════════════════════════
const EKSP_IKONER = { skole:'🏫', restaurant:'🍽', transport:'🚌', arbeidsplass:'🏢', arrangement:'🎉', annet:'📍' };

async function lastEksponeringer() {
  const eksp = await get('/api/eksponeringer');
  const el = document.getElementById('eksponeringer-liste');
  if (!el) return;
  if (!eksp.length) {
    el.innerHTML = '<p style="color:var(--text3);font-size:12px;text-align:center;padding:20px">Ingen eksponeringer registrert.</p>';
    return;
  }
  el.innerHTML = eksp.map(e => `
    <div class="eksp-item">
      <div style="font-size:22px">${EKSP_IKONER[e.type] || '📍'}</div>
      <div style="flex:1">
        <div class="eksp-sted">${e.sted}</div>
        <div class="eksp-meta">${e.adresse} · ${e.dato} ${e.tidspunkt} · ${e.antall_eksponert} eksponert</div>
        ${e.beskrivelse ? `<div class="eksp-meta" style="margin-top:2px">${e.beskrivelse}</div>` : ''}
      </div>
      <div style="display:flex;gap:8px;align-items:center">
        <span class="pill pill-orange">${e.type}</span>
        <button class="btn btn-sm btn-danger" onclick="slettEksponering(${e.id})">×</button>
      </div>
    </div>`).join('');
}

async function leggTilEksponering(e) {
  e.preventDefault();
  await post('/api/eksponeringer', {
    sted:            document.getElementById('e-sted').value,
    adresse:         document.getElementById('e-adr').value,
    dato:            document.getElementById('e-dato').value,
    tidspunkt:       document.getElementById('e-tid').value,
    type:            document.getElementById('e-type').value,
    antall_eksponert: parseInt(document.getElementById('e-ant').value) || 0,
    beskrivelse:     document.getElementById('e-besk').value,
  });
  closeModal('modal-eksponering');
  e.target.reset();
  await lastEksponeringer();
  toast('✓ Eksponering registrert');
}

async function slettEksponering(id) {
  await del(`/api/eksponeringer/${id}`);
  await lastEksponeringer();
  toast('Eksponering slettet');
}

// ═══════════════════════════════════════════════════════════════════════════
// BESLUTNINGSSTØTTE / VEILEDER
// ═══════════════════════════════════════════════════════════════════════════
async function lastVeileder(sykdom) {
  if (!sykdom) return;
  const v = await get(`/api/smittevern/${sykdom}`);
  const meldepliktJa = v.meldeplikt.startsWith('JA');
  document.getElementById('veileder-innhold').innerHTML = `
    <div class="veileder-meldeplikt ${meldepliktJa ? 'ja' : 'nei'}">
      <strong>${meldepliktJa ? '⚠ MELDEPLIKT' : '✓ Ikke meldeplikt'}</strong><br>${v.meldeplikt}
    </div>
    ${v.varslingsplikt ? `<div style="background:var(--surface2);border-radius:var(--radius-sm);padding:10px 14px;margin-bottom:14px;font-size:12px"><strong>Varslingsplikt:</strong> ${v.varslingsplikt}</div>` : ''}
    <div class="veileder-grid">
      <div>
        <div class="card-title" style="margin-bottom:8px">🦠 ${v.sykdom}</div>
        <div class="data-row"><span class="data-row-label">Inkubasjonstid</span><strong>${v.inkubasjonstid}</strong></div>
        <div class="data-row"><span class="data-row-label">Smitteperiode</span><strong>${v.smitteperiode}</strong></div>
        <div style="margin-top:10px">
          <div style="font-size:11px;font-weight:700;color:var(--text3);text-transform:uppercase;margin-bottom:6px">Smitteveier</div>
          ${v.smitteveier.map(s => `<div style="padding:5px 10px;background:var(--surface2);border-radius:4px;margin-bottom:4px;font-size:12px">→ ${s}</div>`).join('')}
        </div>
      </div>
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--text3);text-transform:uppercase;margin-bottom:8px">Anbefalte tiltak</div>
        ${v.tiltak.map((t, i) => `<div style="display:flex;gap:8px;padding:7px 10px;background:var(--surface2);border-radius:4px;margin-bottom:4px;font-size:12px;list-style:none"><span class="tiltak-nr">${i+1}</span>${t}</div>`).join('')}
        <div style="margin-top:10px">
          <div style="font-size:11px;font-weight:700;color:var(--text3);text-transform:uppercase;margin-bottom:6px">Veiledere</div>
          ${v.veiledere.map(v2 => `<div style="padding:5px 10px;background:var(--blue-dim);border-radius:4px;margin-bottom:4px;font-size:12px;color:var(--blue)">📄 ${v2}</div>`).join('')}
        </div>
      </div>
    </div>`;
}

// ═══════════════════════════════════════════════════════════════════════════
// SITUASJONSRAPPORT
// ═══════════════════════════════════════════════════════════════════════════
async function genererRapport() {
  try {
    const r = await post('/api/rapport');
    const s = r.statistikk || {};
    const alv = r.alvorlighetsgrad || 'middels';
    const farge = { lav:'#34d399', middels:'#fbbf24', høy:'#fb923c', kritisk:'#f87171' }[alv] || '#5b7ff7';

    const html = `
      <div class="rapport-header" style="border-left:4px solid ${farge};padding-left:14px;margin-bottom:18px">
        <div style="font-size:18px;font-weight:700;color:var(--text1);margin-bottom:4px">${r.hendelse}</div>
        <div style="font-size:12px;color:var(--text3)">Rapport generert: ${new Date(r.tidspunkt).toLocaleString('nb-NO')}
          &nbsp;·&nbsp; <span style="color:${farge};font-weight:700;text-transform:uppercase">${alv}</span>
        </div>
      </div>
      ${s.bekreftet !== undefined ? `
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:18px">
        <div class="mini-stat-kort red"><div class="mini-stat-tall">${s.bekreftet}</div><div class="mini-stat-label">Bekreftet</div></div>
        <div class="mini-stat-kort orange"><div class="mini-stat-tall">${s.mistenkt}</div><div class="mini-stat-label">Mistenkt</div></div>
        <div class="mini-stat-kort yellow"><div class="mini-stat-tall">${s.naerkontakter}</div><div class="mini-stat-label">Nærkontakter</div></div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:18px">
        <div class="mini-stat-kort green"><div class="mini-stat-tall">${s.tiltak_fullfort}</div><div class="mini-stat-label">Tiltak fullført</div></div>
        <div class="mini-stat-kort blue"><div class="mini-stat-tall">${s.tiltak_pagar}</div><div class="mini-stat-label">Tiltak pågår</div></div>
        <div class="mini-stat-kort muted"><div class="mini-stat-tall">${s.eksponeringer}</div><div class="mini-stat-label">Eksponeringssteder</div></div>
      </div>` : ''}
      <div style="background:var(--surface2);border-radius:8px;padding:14px;font-size:12px;line-height:1.8;white-space:pre-wrap;font-family:monospace;color:var(--text2);max-height:380px;overflow-y:auto">${r.sammendrag}</div>
    `;
    document.getElementById('rapport-tekst').innerHTML = html;
    openModal('rapport-modal');
  } catch(e) { toast('Feil: ' + e.message); }
}
function copyRapport() {
  const el = document.getElementById('rapport-tekst');
  navigator.clipboard.writeText(el.innerText || el.textContent);
  toast('✓ Kopiert');
}

// ═══════════════════════════════════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════════════════════════════════
async function init() {
  await lastHendelsestyper();
  await lastDemoScenarioer();
  await lastHendelserOversikt();
  oppdaterSituasjon();
  lastLogg();
  lastSmitte();
  lastRessurser();
  lastKontakter();
}

init();
