from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import os
import backend.data as data

app = FastAPI(title="Kommunal Beredskapsmodul")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Hendelsestyper ──────────────────────────────────────────────────────────

@app.get("/api/hendelsestyper")
def get_hendelsestyper():
    return data.HENDELSESTYPER


# ── Aktiv hendelse ──────────────────────────────────────────────────────────

class HendelsesInput(BaseModel):
    type_id: str
    tittel: str
    beskrivelse: str
    lokasjon: str
    alvorlighetsgrad: str  # "lav", "middels", "høy", "kritisk"

@app.get("/api/hendelse")
def get_hendelse():
    return data.aktiv_hendelse or {}

@app.post("/api/hendelse")
def opprett_hendelse(h: HendelsesInput):
    ht = next((x for x in data.HENDELSESTYPER if x["id"] == h.type_id), None)
    if not ht:
        raise HTTPException(404, "Hendelsestype ikke funnet")
    data.aktiv_hendelse = {
        "id": 1,
        "type_id": h.type_id,
        "type_navn": ht["navn"],
        "ikon": ht["ikon"],
        "tittel": h.tittel,
        "beskrivelse": h.beskrivelse,
        "lokasjon": h.lokasjon,
        "alvorlighetsgrad": h.alvorlighetsgrad,
        "opprettet": datetime.now().isoformat(),
        "status": "aktiv",
    }
    data.hendelseslogg.insert(0, {
        "id": data.neste_id(data.hendelseslogg),
        "tidspunkt": datetime.now().isoformat(),
        "type": "hendelse",
        "tittel": f"Hendelse opprettet: {ht['navn']}",
        "tekst": h.beskrivelse,
        "bruker": "Kommuneoverlege",
    })
    return data.aktiv_hendelse

@app.delete("/api/hendelse")
def avslutt_hendelse():
    if data.aktiv_hendelse:
        data.aktiv_hendelse["status"] = "avsluttet"
        data.hendelseslogg.insert(0, {
            "id": data.neste_id(data.hendelseslogg),
            "tidspunkt": datetime.now().isoformat(),
            "type": "hendelse",
            "tittel": "Hendelse avsluttet",
            "tekst": f"Hendelsen '{data.aktiv_hendelse['tittel']}' ble avsluttet.",
            "bruker": "Kommuneoverlege",
        })
    return {"ok": True}


# ── Tiltakskort ─────────────────────────────────────────────────────────────

@app.get("/api/tiltakskort/{type_id}")
def get_tiltakskort(type_id: str):
    kort = data.TILTAKSKORT.get(type_id)
    if not kort:
        raise HTTPException(404, "Tiltakskort ikke funnet")
    return kort


# ── Ressurser ────────────────────────────────────────────────────────────────

@app.get("/api/ressurser")
def get_ressurser():
    return data.RESSURSER

class RessursStatusUpdate(BaseModel):
    kategori: str
    index: int
    status: str

@app.put("/api/ressurser/status")
def oppdater_ressurs_status(u: RessursStatusUpdate):
    kat = data.RESSURSER.get(u.kategori)
    if not kat or u.index >= len(kat):
        raise HTTPException(404, "Ressurs ikke funnet")
    kat[u.index]["status"] = u.status
    return {"ok": True}


# ── Kontakter ────────────────────────────────────────────────────────────────

@app.get("/api/kontakter")
def get_kontakter():
    return data.KONTAKTER


# ── Hendelseslogg ────────────────────────────────────────────────────────────

class LoggInput(BaseModel):
    type: str  # "beslutning", "varsling", "tiltak", "observasjon", "møte"
    tittel: str
    tekst: str
    bruker: Optional[str] = "Kommuneoverlege"

@app.get("/api/logg")
def get_logg():
    return data.hendelseslogg

@app.post("/api/logg")
def legg_til_logg(entry: LoggInput):
    ny = {
        "id": data.neste_id(data.hendelseslogg),
        "tidspunkt": datetime.now().isoformat(),
        "type": entry.type,
        "tittel": entry.tittel,
        "tekst": entry.tekst,
        "bruker": entry.bruker,
    }
    data.hendelseslogg.insert(0, ny)
    return ny


# ── Tiltaksoppfølging per utbrudd ────────────────────────────────────────────

class TiltakInput(BaseModel):
    kategori: str  # "testing", "isolasjon", "kohortering", "varsling", "annet"
    tittel: str
    beskrivelse: str
    ansvarlig: str
    status: str = "planlagt"  # "planlagt", "pågår", "fullført"
    frist: Optional[str] = None

@app.get("/api/tiltak")
def get_tiltak():
    return data.smitte_tiltak

@app.post("/api/tiltak")
def legg_til_tiltak(t: TiltakInput):
    ny = {"id": data.neste_id(data.smitte_tiltak), **t.model_dump(), "opprettet": datetime.now().isoformat()}
    data.smitte_tiltak.append(ny)
    return ny

@app.put("/api/tiltak/{tid}/status")
def oppdater_tiltak_status(tid: int, status: str):
    t = next((x for x in data.smitte_tiltak if x["id"] == tid), None)
    if not t:
        raise HTTPException(404)
    t["status"] = status
    return t

@app.delete("/api/tiltak/{tid}")
def slett_tiltak(tid: int):
    data.smitte_tiltak = [x for x in data.smitte_tiltak if x["id"] != tid]
    return {"ok": True}


# ── Eksponeringshendelser ─────────────────────────────────────────────────────

class EksponeringsInput(BaseModel):
    sted: str
    adresse: str
    dato: str
    tidspunkt: str
    type: str  # "restaurant", "skole", "transport", "arbeidsplass", "arrangement", "annet"
    antall_eksponert: int
    beskrivelse: str

@app.get("/api/eksponeringer")
def get_eksponeringer():
    return data.eksponeringer

@app.post("/api/eksponeringer")
def legg_til_eksponering(e: EksponeringsInput):
    ny = {"id": data.neste_id(data.eksponeringer), **e.model_dump(), "opprettet": datetime.now().isoformat()}
    data.eksponeringer.append(ny)
    return ny

@app.delete("/api/eksponeringer/{eid}")
def slett_eksponering(eid: int):
    data.eksponeringer = [x for x in data.eksponeringer if x["id"] != eid]
    return {"ok": True}


# ── Smittevern-veileder / beslutningsstøtte ───────────────────────────────────

@app.get("/api/smittevern/{sykdom}")
def get_smittevern_veileder(sykdom: str):
    return data.SMITTEVERN_VEILEDERE.get(sykdom, data.SMITTEVERN_VEILEDERE["generell"])


# ── Smittesporing ────────────────────────────────────────────────────────────

class SmittetilfellInput(BaseModel):
    navn: str
    alder: int
    kjønn: str
    prøvedato: str
    symptomstart: Optional[str] = None
    smittekilde_id: Optional[int] = None
    lokasjon: str
    institusjon: Optional[str] = None
    status: str = "bekreftet"  # "bekreftet", "mistenkt", "nærkontakt"

@app.get("/api/smitte")
def get_smittetilfeller():
    return data.smittetilfeller

@app.post("/api/smitte")
def legg_til_smittetilfelle(s: SmittetilfellInput):
    ny = {
        "id": data.neste_id(data.smittetilfeller),
        **s.model_dump(),
        "registrert": datetime.now().isoformat(),
    }
    data.smittetilfeller.append(ny)
    data.hendelseslogg.insert(0, {
        "id": data.neste_id(data.hendelseslogg),
        "tidspunkt": datetime.now().isoformat(),
        "type": "smitte",
        "tittel": f"Nytt smittetilfelle registrert: {s.status}",
        "tekst": f"{s.navn}, {s.alder} år – {s.lokasjon}",
        "bruker": "Smittevern",
    })
    return ny

@app.delete("/api/smitte/{tilfelle_id}")
def slett_smittetilfelle(tilfelle_id: int):
    data.smittetilfeller = [x for x in data.smittetilfeller if x["id"] != tilfelle_id]
    return {"ok": True}


# ── Situasjonsrapport ────────────────────────────────────────────────────────

@app.post("/api/rapport")
def generer_rapport():
    h = data.aktiv_hendelse
    if not h:
        raise HTTPException(400, "Ingen aktiv hendelse")

    bekreftet = [x for x in data.smittetilfeller if x["status"] == "bekreftet"]
    mistenkt = [x for x in data.smittetilfeller if x["status"] == "mistenkt"]
    naerkontakter = [x for x in data.smittetilfeller if x["status"] == "nærkontakt"]

    tiltak_fullfort = [t for t in data.smitte_tiltak if t["status"] == "fullført"]
    tiltak_pagar = [t for t in data.smitte_tiltak if t["status"] == "pågår"]
    tiltak_planlagt = [t for t in data.smitte_tiltak if t["status"] == "planlagt"]

    berørte_inst = {}
    for s in data.smittetilfeller:
        inst = s.get("institusjon") or "Ukjent"
        berørte_inst[inst] = berørte_inst.get(inst, 0) + 1

    eksp_antall = sum(e.get("antall_eksponert", 0) for e in data.eksponeringer)

    siste_logg = data.hendelseslogg[:5] if data.hendelseslogg else []
    siste_logg_tekst = "\n".join(
        f"  • [{e['tidspunkt'][:16].replace('T',' ')}] {e['tittel']} ({e['bruker']})"
        for e in siste_logg
    )

    tiltak_tekst = ""
    if data.smitte_tiltak:
        tiltak_tekst = (
            f"\nTILTAKSOPPFØLGING ({len(data.smitte_tiltak)} tiltak totalt):\n"
            f"  Fullført: {len(tiltak_fullfort)}  |  Pågår: {len(tiltak_pagar)}  |  Planlagt: {len(tiltak_planlagt)}\n"
        )
        for t in data.smitte_tiltak:
            status_ikon = {"fullført": "✅", "pågår": "🔄", "planlagt": "📋"}.get(t["status"], "•")
            tiltak_tekst += f"  {status_ikon} [{t['kategori'].upper()}] {t['tittel']} – {t['ansvarlig']}\n"

    inst_tekst = ""
    if berørte_inst:
        inst_tekst = "\nBERØRTE INSTITUSJONER:\n"
        for inst, antall in sorted(berørte_inst.items(), key=lambda x: -x[1]):
            inst_tekst += f"  • {inst}: {antall} tilfelle(r)\n"

    eksp_tekst = ""
    if data.eksponeringer:
        eksp_tekst = f"\nEKSPONERINGSHENDELSER ({len(data.eksponeringer)} steder, ~{eksp_antall} eksponerte):\n"
        for e in data.eksponeringer:
            eksp_tekst += f"  • {e['sted']} – {e['dato']} – {e['antall_eksponert']} eksponerte\n"

    sammendrag = (
        f"━━━ SITUASJONSRAPPORT – {datetime.now().strftime('%d.%m.%Y %H:%M')} ━━━\n\n"
        f"HENDELSE: {h['type_navn']} – {h['tittel']}\n"
        f"Lokasjon: {h['lokasjon']}\n"
        f"Opprettet: {h['opprettet'][:16].replace('T', ' ')}\n"
        f"Alvorlighetsgrad: {h['alvorlighetsgrad'].upper()}\n"
        f"Status: {h['status'].upper()}\n\n"
        f"SMITTESITUASJON:\n"
        f"  Bekreftede tilfeller: {len(bekreftet)}\n"
        f"  Mistenkte tilfeller: {len(mistenkt)}\n"
        f"  Nærkontakter under oppfølging: {len(naerkontakter)}\n"
        f"  Totalt registrert: {len(data.smittetilfeller)}\n"
        f"{inst_tekst}"
        f"{eksp_tekst}"
        f"{tiltak_tekst}"
        f"\nHENDELSESLOGG ({len(data.hendelseslogg)} oppføringer):\n"
        f"{siste_logg_tekst}\n"
        f"{'  (+ flere...)' if len(data.hendelseslogg) > 5 else ''}\n\n"
        f"Rapport generert av: Kommuneoverlegen, Bærum kommune"
    )

    rapport = {
        "id": data.neste_id(data.situasjonsrapporter),
        "tidspunkt": datetime.now().isoformat(),
        "hendelse": h["tittel"],
        "alvorlighetsgrad": h["alvorlighetsgrad"],
        "status": h["status"],
        "sammendrag": sammendrag,
        "statistikk": {
            "bekreftet": len(bekreftet),
            "mistenkt": len(mistenkt),
            "naerkontakter": len(naerkontakter),
            "tiltak_fullfort": len(tiltak_fullfort),
            "tiltak_pagar": len(tiltak_pagar),
            "eksponeringer": len(data.eksponeringer),
            "totalt_eksponert": eksp_antall,
            "logg_oppforinger": len(data.hendelseslogg),
        },
    }
    data.situasjonsrapporter.append(rapport)
    return rapport


# ── Demo-scenarioer ──────────────────────────────────────────────────────────

@app.get("/api/demo/scenarioer")
def get_demo_scenarioer():
    return [
        {
            "id": s["id"],
            "navn": s["navn"],
            "beskrivelse": s["beskrivelse"],
            "lat": s.get("lat"),
            "lon": s.get("lon"),
            "type_id": s["hendelse"]["type_id"],
            "alvorlighetsgrad": s["hendelse"]["alvorlighetsgrad"],
            "lokasjon": s["hendelse"]["lokasjon"],
            "tittel": s["hendelse"]["tittel"],
            "antall_logg": len(s["logg"]),
            "antall_smitte": len(s["smitte"]),
        }
        for s in data.DEMO_SCENARIOER
    ]

@app.post("/api/demo/last/{scenario_id}")
def last_demo(scenario_id: str):
    data.situasjonsrapporter = []
    resultat = data.last_demo_scenario(scenario_id)
    if not resultat:
        raise HTTPException(404, "Demo-scenario ikke funnet")
    return {"ok": True, "hendelse": resultat}

@app.post("/api/demo/reset")
def reset_demo():
    data.aktiv_hendelse = None
    data.hendelseslogg = []
    data.smittetilfeller = []
    data.situasjonsrapporter = []
    data.smitte_tiltak = []
    data.eksponeringer = []
    return {"ok": True}


# ── Statiske filer / frontend ────────────────────────────────────────────────

frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="static")
