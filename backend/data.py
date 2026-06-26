from datetime import datetime

HENDELSESTYPER = [
    {"id": "smitteutbrudd", "navn": "Smitteutbrudd", "ikon": "🦠", "kategori": "smitte"},
    {"id": "pandemi", "navn": "Pandemi", "ikon": "🌍", "kategori": "smitte"},
    {"id": "matbaren", "navn": "Mat-/vannbårent utbrudd", "ikon": "💧", "kategori": "smitte"},
    {"id": "brann_sykehjem", "navn": "Brann i sykehjem", "ikon": "🔥", "kategori": "helse"},
    {"id": "evakuering", "navn": "Evakuering av institusjon", "ikon": "🚨", "kategori": "helse"},
    {"id": "personellmangel", "navn": "Kritisk personellmangel", "ikon": "👥", "kategori": "helse"},
    {"id": "legemiddelmangel", "navn": "Legemiddelmangel", "ikon": "💊", "kategori": "helse"},
    {"id": "strombortfall", "navn": "Langvarig strømbrudd", "ikon": "⚡", "kategori": "infrastruktur"},
    {"id": "cyberangrep", "navn": "Cyberangrep", "ikon": "💻", "kategori": "infrastruktur"},
    {"id": "forurenset_vann", "navn": "Forurenset drikkevann", "ikon": "🚱", "kategori": "infrastruktur"},
    {"id": "storulykke", "navn": "Storulykke", "ikon": "🚑", "kategori": "ulykke"},
    {"id": "kjemikalieutslipp", "navn": "Kjemikalieutslipp", "ikon": "☣️", "kategori": "ulykke"},
    {"id": "ekstremvar", "navn": "Ekstremvær", "ikon": "🌪️", "kategori": "annet"},
]

TILTAKSKORT = {
    "smitteutbrudd": {
        "tittel": "Smitteutbrudd – tiltakskort",
        "umiddelbare_tiltak": [
            "Bekreft diagnose og smittekilde",
            "Varsle kommunedirektør og kriseledelse",
            "Kontakt FHI for veiledning (tlf. 21 07 70 00)",
            "Opprett smittesporing – start registrering av tilfeller og nærkontakter",
            "Vurder isolasjon av smittede",
            "Kartlegg berørte institusjoner (skoler, barnehager, sykehjem)",
            "Vurder meldeplikt (MSIS)",
        ],
        "varslingsrutiner": [
            "Kommunedirektør – umiddelbart",
            "Statsforvalter i Oslo og Viken – innen 2 timer ved større utbrudd",
            "FHI – ved meldepliktig sykdom",
            "Helsedirektoratet – ved behov for nasjonal koordinering",
            "Vestre Viken HF / Bærum sykehus – ved alvorlige tilfeller",
            "Presse/informasjonsansvarlig – koordinert kommunikasjon",
        ],
        "roller": [
            {"rolle": "Kommuneoverlege Bærum", "ansvar": "Faglig ledelse, smittevern, varsling til FHI"},
            {"rolle": "Kommunedirektør", "ansvar": "Overordnet kriseledelse og beslutninger"},
            {"rolle": "Beredskapskoordinator", "ansvar": "Koordinering, logg, ressurser"},
            {"rolle": "Bærum legevakt", "ansvar": "Klinisk håndtering, testing"},
            {"rolle": "Informasjonsansvarlig", "ansvar": "Pressemelding, innbyggerinformasjon"},
        ],
        "ros_risikoer": [
            {"risiko": "Rask spredning i sykehjem", "sannsynlighet": "høy", "konsekvens": "kritisk"},
            {"risiko": "Sårbare grupper (eldre, immunsvakt)", "sannsynlighet": "høy", "konsekvens": "kritisk"},
            {"risiko": "Kapasitetssvikt Bærum legevakt", "sannsynlighet": "middels", "konsekvens": "alvorlig"},
            {"risiko": "Mangel på testkapasitet", "sannsynlighet": "lav", "konsekvens": "moderat"},
        ],
    },
    "pandemi": {
        "tittel": "Pandemi – tiltakskort",
        "umiddelbare_tiltak": [
            "Aktiver Bærum kommunes pandemiplan",
            "Innkall kriseledelse til møte i rådhuset, Sandvika",
            "Vurder aktivering av ekstra helsepersonell",
            "Etabler kontakt med Bærum sykehus (Vestre Viken HF)",
            "Vurder skalering av legevaktkapasitet",
            "Start kontinuerlig situasjonsoppdatering",
            "Opprett informasjonskanal til Bærums innbyggere (~130 000)",
        ],
        "varslingsrutiner": [
            "Kommunedirektør – umiddelbart",
            "Statsforvalter i Oslo og Viken – innen 1 time",
            "FHI – løpende",
            "Helsedirektoratet – daglig rapportering",
            "Vestre Viken HF – koordinering av kapasitet",
        ],
        "roller": [
            {"rolle": "Kommuneoverlege", "ansvar": "Medisinsk faglig ledelse og smitteverntiltak"},
            {"rolle": "Kommunedirektør", "ansvar": "Krisestab og ressursprioritering"},
            {"rolle": "Helse- og omsorgsledelse", "ansvar": "Tjenestekontinuitet"},
            {"rolle": "Beredskapskoordinator", "ansvar": "Koordinering på tvers av etater"},
        ],
        "ros_risikoer": [
            {"risiko": "Massekasualistikk", "sannsynlighet": "høy", "konsekvens": "kritisk"},
            {"risiko": "Personellmangel helse", "sannsynlighet": "høy", "konsekvens": "alvorlig"},
            {"risiko": "Legemiddelmangel", "sannsynlighet": "middels", "konsekvens": "alvorlig"},
            {"risiko": "Sosial uro", "sannsynlighet": "lav", "konsekvens": "moderat"},
        ],
    },
    "brann_sykehjem": {
        "tittel": "Brann i sykehjem – tiltakskort",
        "umiddelbare_tiltak": [
            "Bekreft evakuering pågår – kontakt brannvesen (110)",
            "Etabler kontakt med sykehjemsleder",
            "Kartlegg antall beboere og personalstatus",
            "Vurder behov for akuttmedisinsk bistand – AMK (113)",
            "Aktiver kommunalt kriseteam Bærum",
            "Identifiser midlertidige plasseringsmuligheter for beboere (andre sykehjem i Bærum)",
            "Varsle pårørende – koordiner med sykehjemsledelse",
        ],
        "varslingsrutiner": [
            "Brannvesen 110 – umiddelbart",
            "AMK 113 – ved personskade",
            "Kommunedirektør – umiddelbart",
            "Statsforvalter i Oslo og Viken – innen 2 timer",
            "Pårørende – via sykehjem så raskt som mulig",
        ],
        "roller": [
            {"rolle": "Kommuneoverlege", "ansvar": "Medisinsk koordinering, helsevurdering evakuerte"},
            {"rolle": "Sykehjemsleder", "ansvar": "Evakuering, personaloversikt, pårørendekontakt"},
            {"rolle": "Kommunedirektør", "ansvar": "Overordnet koordinering og ressurser"},
            {"rolle": "Kriseteam Bærum", "ansvar": "Psykososial støtte til beboere og ansatte"},
        ],
        "ros_risikoer": [
            {"risiko": "Skade/død blant sårbare beboere", "sannsynlighet": "høy", "konsekvens": "kritisk"},
            {"risiko": "Mangel på alternative plasser i Bærum", "sannsynlighet": "middels", "konsekvens": "alvorlig"},
            {"risiko": "Medisinsk utstyr tilgjengelighet", "sannsynlighet": "middels", "konsekvens": "alvorlig"},
        ],
    },
    "strombortfall": {
        "tittel": "Langvarig strømbrudd – tiltakskort",
        "umiddelbare_tiltak": [
            "Kontakt Elvia (nettselskap) for status og estimert gjenopprettingstid",
            "Kartlegg berørte helseinstitusjoner (sykehjem, legevakt, fastleger) i Bærum",
            "Verifiser nødstrømsaggregater er operative",
            "Vurder evakuering av sårbare beboere ved lang varighet",
            "Sikre kjøling av legemidler og biologisk materiale",
            "Aktiver manuell journalføring",
            "Varsle ansatte om alternativ kommunikasjon",
        ],
        "varslingsrutiner": [
            "Elvia (nettselskap Bærum) – umiddelbart for status",
            "Kommunedirektør – ved varighet over 2 timer",
            "Statsforvalter – ved varighet over 4 timer",
            "Bærum sykehus – koordinering av pasienter med kritisk utstyrsbehov",
        ],
        "roller": [
            {"rolle": "Kommuneoverlege", "ansvar": "Medisinsk risikovurdering, sårbare grupper"},
            {"rolle": "Beredskapskoordinator", "ansvar": "Ressurskoordinering, nødstrøm"},
            {"rolle": "Sykehjemsledere", "ansvar": "Lokal håndtering, varme og pleie"},
        ],
        "ros_risikoer": [
            {"risiko": "Bortfall av medisinsk utstyr", "sannsynlighet": "middels", "konsekvens": "kritisk"},
            {"risiko": "Nedkjøling av sårbare beboere", "sannsynlighet": "middels", "konsekvens": "alvorlig"},
            {"risiko": "Tap av legemiddelkjøling", "sannsynlighet": "lav", "konsekvens": "alvorlig"},
            {"risiko": "Svikt i kommunikasjonssystemer", "sannsynlighet": "høy", "konsekvens": "moderat"},
        ],
    },
    "forurenset_vann": {
        "tittel": "Forurenset drikkevann – tiltakskort",
        "umiddelbare_tiltak": [
            "Kontakt Vann- og avløpsetaten / Bærum Vann for bekreftelse og prøvetaking",
            "Utsted kokevarsel via kommunens kanaler (baerum.kommune.no, SMS-varsling)",
            "Varsle helseinstitusjoner, skoler og barnehager umiddelbart",
            "Organiser distribusjon av rent vann (kontakt Sivilforsvaret og Røde Kors)",
            "Kartlegg sykdomstilfeller – mulig allerede pågående utbrudd",
            "Kontakt Mattilsynet region Oslo, Akershus og Østfold",
        ],
        "varslingsrutiner": [
            "Bærum Vann – umiddelbart",
            "Mattilsynet – innen 1 time",
            "Kommunedirektør – umiddelbart",
            "Statsforvalter i Oslo og Viken – innen 2 timer",
            "Innbyggere – kokevarsel via SMS, baerum.kommune.no, NRK",
        ],
        "roller": [
            {"rolle": "Kommuneoverlege", "ansvar": "Helsefaglig vurdering, smittevernrådgivning"},
            {"rolle": "Teknisk etat Bærum", "ansvar": "Vannverk, infrastruktur"},
            {"rolle": "Mattilsynet", "ansvar": "Tilsyn og prøvetaking"},
            {"rolle": "Informasjonsansvarlig", "ansvar": "Innbyggerinformasjon"},
        ],
        "ros_risikoer": [
            {"risiko": "Masseintoksikasjon", "sannsynlighet": "lav", "konsekvens": "kritisk"},
            {"risiko": "Gastrointestinalt utbrudd", "sannsynlighet": "høy", "konsekvens": "alvorlig"},
            {"risiko": "Spesielt sårbare (spedbarn, immunsvakt)", "sannsynlighet": "høy", "konsekvens": "kritisk"},
        ],
    },
}

for ht in HENDELSESTYPER:
    if ht["id"] not in TILTAKSKORT:
        TILTAKSKORT[ht["id"]] = {
            "tittel": f"{ht['navn']} – tiltakskort",
            "umiddelbare_tiltak": [
                "Innhent informasjon og bekreft hendelsen",
                "Varsle kommunedirektør og kriseledelse",
                "Etabler situasjonsbilde",
                "Vurder behov for ekstern bistand",
                "Start hendelseslogg",
            ],
            "varslingsrutiner": [
                "Kommunedirektør – umiddelbart",
                "Statsforvalter i Oslo og Viken – innen 2 timer",
                "Relevante fagmyndigheter",
            ],
            "roller": [
                {"rolle": "Kommuneoverlege Bærum", "ansvar": "Faglig ledelse og vurdering"},
                {"rolle": "Kommunedirektør", "ansvar": "Overordnet kriseledelse"},
                {"rolle": "Beredskapskoordinator", "ansvar": "Koordinering og logg"},
            ],
            "ros_risikoer": [
                {"risiko": "Eskalering av hendelsen", "sannsynlighet": "middels", "konsekvens": "alvorlig"},
                {"risiko": "Kapasitetssvikt i tjenester", "sannsynlighet": "lav", "konsekvens": "moderat"},
            ],
        }

# Bærum-spesifikke ressurser med ekte koordinater
RESSURSER = {
    "helse": [
        {
            "navn": "Bærum legevakt",
            "type": "helse",
            "kapasitet": "24/7 – akutt",
            "status": "operativ",
            "kontakt": "67 80 05 00",
            "adresse": "Gjettumveien 22, 1346 Gjettum",
            "lat": 59.9062,
            "lon": 10.5339,
        },
        {
            "navn": "Bærum sykehus (Vestre Viken)",
            "type": "helse",
            "kapasitet": "330 senger",
            "status": "operativ",
            "kontakt": "67 80 00 00",
            "adresse": "Sykehusveien 25, 1346 Gjettum",
            "lat": 59.9048,
            "lon": 10.5318,
        },
        {
            "navn": "Bekkestua legesenter",
            "type": "helse",
            "kapasitet": "12 fastleger",
            "status": "operativ",
            "kontakt": "67 53 07 00",
            "adresse": "Bekkestua, 1357 Bærum",
            "lat": 59.9127,
            "lon": 10.5621,
        },
        {
            "navn": "Sandvika legesenter",
            "type": "helse",
            "kapasitet": "8 fastleger",
            "status": "operativ",
            "kontakt": "67 54 44 00",
            "adresse": "Rådhusveien 7, 1300 Sandvika",
            "lat": 59.8903,
            "lon": 10.5234,
        },
        {
            "navn": "Dønski bo- og behandlingssenter",
            "type": "institusjon",
            "kapasitet": "110 plasser",
            "status": "operativ",
            "kontakt": "67 50 43 00",
            "adresse": "Halvard Birkelandsvei 31, 1346 Gjettum",
            "lat": 59.9088,
            "lon": 10.5452,
        },
        {
            "navn": "Østerås sykehjem",
            "type": "institusjon",
            "kapasitet": "75 plasser",
            "status": "operativ",
            "kontakt": "67 50 42 00",
            "adresse": "Østerås, 1361 Østerås",
            "lat": 59.9257,
            "lon": 10.5694,
        },
        {
            "navn": "Rykkinn bo- og behandlingssenter",
            "type": "institusjon",
            "kapasitet": "88 plasser",
            "status": "operativ",
            "kontakt": "67 50 41 00",
            "adresse": "Rykkinn, 1349 Rykkinn",
            "lat": 59.9289,
            "lon": 10.4794,
        },
        {
            "navn": "Bærum hjemmetjeneste",
            "type": "helse",
            "kapasitet": "~2000 brukere",
            "status": "operativ",
            "kontakt": "67 50 40 00",
            "adresse": "Kommunehuset, Sandvika",
            "lat": 59.8897,
            "lon": 10.5220,
        },
        {
            "navn": "Kommunalt kriseteam Bærum",
            "type": "krise",
            "kapasitet": "8 fagpersoner",
            "status": "tilgjengelig",
            "kontakt": "67 50 50 00",
            "adresse": "Rådhuset, Arnold Haukelands plass 10, Sandvika",
            "lat": 59.8893,
            "lon": 10.5214,
        },
    ],
    "frivillig": [
        {
            "navn": "Røde Kors Bærum",
            "type": "frivillig",
            "kapasitet": "~150 frivillige",
            "status": "tilgjengelig",
            "kontakt": "67 54 20 00",
            "adresse": "Sandvika, 1300 Bærum",
            "lat": 59.8920,
            "lon": 10.5190,
        },
        {
            "navn": "Sivilforsvaret Bærum",
            "type": "frivillig",
            "kapasitet": "45 mannskaper",
            "status": "tilgjengelig",
            "kontakt": "23 00 10 00",
            "adresse": "Gjettum, Bærum",
            "lat": 59.9071,
            "lon": 10.5280,
        },
        {
            "navn": "Norsk Folkehjelp Bærum",
            "type": "frivillig",
            "kapasitet": "Variabel",
            "status": "tilgjengelig",
            "kontakt": "22 03 77 00",
            "adresse": "Sandvika, 1300 Bærum",
            "lat": 59.8940,
            "lon": 10.5260,
        },
        {
            "navn": "Sanitetsforeningen Bærum",
            "type": "frivillig",
            "kapasitet": "30 frivillige",
            "status": "tilgjengelig",
            "kontakt": "67 55 10 00",
            "adresse": "Bekkestua, Bærum",
            "lat": 59.9134,
            "lon": 10.5640,
        },
    ],
    "transport": [
        {
            "navn": "AMK Akershus",
            "type": "transport",
            "kapasitet": "Ambulanser Bærum-sektoren",
            "status": "operativ",
            "kontakt": "113",
            "adresse": "Bærum sykehus, Gjettum",
            "lat": 59.9050,
            "lon": 10.5325,
        },
        {
            "navn": "Bærum kommune – transport",
            "type": "transport",
            "kapasitet": "8 kjøretøy",
            "status": "operativ",
            "kontakt": "67 50 50 10",
            "adresse": "Teknisk etat, Sandvika",
            "lat": 59.8880,
            "lon": 10.5200,
        },
    ],
}

KONTAKTER = [
    # Kommunal ledelse Bærum
    {"navn": "Kommunedirektør", "person": "Erik Bjørnsen", "tlf": "67 50 40 00", "epost": "postmottak@baerum.kommune.no", "kategori": "kommunal"},
    {"navn": "Ordfører", "person": "Lisbeth Hammer Krog", "tlf": "67 50 40 01", "epost": "ordforer@baerum.kommune.no", "kategori": "kommunal"},
    {"navn": "Kommuneoverlege", "person": "[din tittel]", "tlf": "67 50 40 10", "epost": "kommuneoverlege@baerum.kommune.no", "kategori": "kommunal"},
    {"navn": "Beredskapskoordinator", "person": "Bærum beredskap", "tlf": "67 50 40 20", "epost": "beredskap@baerum.kommune.no", "kategori": "kommunal"},
    {"navn": "Helse- og omsorgssjef", "person": "Bærum HO", "tlf": "67 50 40 30", "epost": "helse@baerum.kommune.no", "kategori": "kommunal"},
    {"navn": "Informasjonsansvarlig", "person": "Kommunikasjonsavdeling", "tlf": "67 50 40 40", "epost": "info@baerum.kommune.no", "kategori": "kommunal"},
    # Statlige
    {"navn": "Statsforvalter Oslo og Viken – helse", "person": "Helseavdeling", "tlf": "22 00 35 00", "epost": "sfovpost@statsforvalteren.no", "kategori": "statlig"},
    {"navn": "FHI – smittevernvakt", "person": "Vakthavende", "tlf": "21 07 70 00", "epost": "smittevern@fhi.no", "kategori": "statlig"},
    {"navn": "Helsedirektoratet", "person": "Beredskapsavdelingen", "tlf": "810 20 050", "epost": "beredskap@helsedir.no", "kategori": "statlig"},
    {"navn": "Mattilsynet – region øst", "person": "Oslo/Akershus", "tlf": "22 40 00 00", "epost": "postmottak@mattilsynet.no", "kategori": "statlig"},
    # Nødetater
    {"navn": "Politi – Asker og Bærum", "person": "Operasjonssentral", "tlf": "02800", "epost": "oslo.politidistrikt@politiet.no", "kategori": "nodetater"},
    {"navn": "Asker og Bærum brannvesen", "person": "110-sentral", "tlf": "110", "epost": "brann@abbv.no", "kategori": "nodetater"},
    {"navn": "AMK – Akershus", "person": "AMK-sentral", "tlf": "113", "epost": "amk@vestreviken.no", "kategori": "nodetater"},
    {"navn": "Bærum sykehus – smittevern", "person": "Smittevernlege Vestre Viken", "tlf": "67 80 00 00", "epost": "smittevern@vestreviken.no", "kategori": "nodetater"},
    # Infrastruktur
    {"navn": "Elvia (strøm Bærum)", "person": "Feilmelding/beredskap", "tlf": "22 17 20 00", "epost": "post@elvia.no", "kategori": "infrastruktur"},
    {"navn": "Bærum Vann (Veas)", "person": "Driftsvakt", "tlf": "67 86 39 00", "epost": "post@veas.nu", "kategori": "infrastruktur"},
    {"navn": "Telenor – driftssentral", "person": "Beredskap", "tlf": "09000", "epost": "beredskap@telenor.com", "kategori": "infrastruktur"},
]

SMITTEVERN_VEILEDERE = {
    "norovirus": {
        "sykdom": "Norovirus (mage-tarminfeksjon)",
        "meldeplikt": "Nei – men skal meldes ved utbrudd på institusjon (§ 2-3 smittevernloven)",
        "varslingsplikt": "Statsforvalter ved utbrudd med ≥2 tilfeller på helseinstitusjon",
        "inkubasjonstid": "12–48 timer",
        "smitteperiode": "Fra symptomdebut til 48 timer etter symptomfrihet",
        "smitteveier": ["Fekal-oral", "Dråpesmitte (oppkast)", "Kontaktsmitte via overflater"],
        "tiltak": [
            "Kohortering av smittede og friske beboere",
            "Smittevernsutstyr (hansker, frakk, munnbind) ved stell",
            "Håndhygiene med såpe og vann (klorhexidin har begrenset effekt)",
            "Desinfeksjon med klorbasert middel (1000 ppm)",
            "Isolasjon til 48 timer etter symptomfrihet",
            "Stenge kantine / stans av felles matservering",
            "Ekskluder sykt personale fra arbeid 48t etter symptomfrihet",
        ],
        "veiledere": ["FHI: Norovirus", "Hdir: Smittevern i helseinstitusjoner"],
    },
    "influensa": {
        "sykdom": "Influensa A/B",
        "meldeplikt": "Nei for sporadiske tilfeller. Utbrudd på institusjon meldes.",
        "varslingsplikt": "Statsforvalter ved utbrudd med uvanlig alvorlighetsgrad",
        "inkubasjonstid": "1–4 dager",
        "smitteperiode": "1 dag før til 5–7 dager etter symptomstart",
        "smitteveier": ["Dråpesmitte", "Kontaktsmitte", "Aerosoler ved nær kontakt"],
        "tiltak": [
            "Isoler syke elever/ansatte",
            "Vurder stenging av berørte klasser ved høyt fravær (>30%)",
            "Tilby influensavaksine til uvaksinerte i risikogrupper",
            "Antiviral behandling (Tamiflu) ved risikogrupper",
            "Informer foreldre om symptomer og karanteneregler",
            "Forsterket renhold av kontaktflater",
            "Håndhygienerutiner i klassen",
        ],
        "veiledere": ["FHI: Influensa i barnehager og skoler", "Hdir: Influensavaksine"],
    },
    "meslinger": {
        "sykdom": "Meslinger (Morbilli)",
        "meldeplikt": "JA – gruppe A (§ 2-1 smittevernloven). Meldes umiddelbart til kommuneoverlegen og FHI.",
        "varslingsplikt": "FHI umiddelbart. WHO-varsling via FHI.",
        "inkubasjonstid": "7–18 dager (gjennomsnitt 10–12 dager)",
        "smitteperiode": "4 dager FØR til 4 dager ETTER utslett",
        "smitteveier": ["Luftbåren smitte (svært smittsom, R0: 12–18)", "Dråpesmitte", "Kontaktsmitte"],
        "tiltak": [
            "UMIDDELBAR isolasjon av smittede",
            "Identifiser alle nærkontakter (alle som var i samme rom)",
            "Tilby posteksponeringsimmunisering (MMR) innen 72 timer",
            "Immunoglobulin til sårbare grupper innen 6 dager",
            "Sjekk vaksinasjonsstatus via SYSVAK for alle nærkontakter",
            "Ekskluder uvaksinerte nærkontakter fra skole/barnehage i 21 dager",
            "Informer ALLE foreldre med barn på skolen",
        ],
        "veiledere": ["FHI: Meslinger smittevernveileder", "FHI: MMR-vaksine", "ECDC: Measles guidance"],
    },
    "generell": {
        "sykdom": "Generell smittesykdom",
        "meldeplikt": "Vurder basert på diagnose – se MSIS-liste over meldepliktige sykdommer",
        "varslingsplikt": "Statsforvalter ved utbrudd med alvorlig alvorlighetsgrad",
        "inkubasjonstid": "Varierer",
        "smitteperiode": "Varierer",
        "smitteveier": ["Avhengig av agens"],
        "tiltak": [
            "Identifiser smitteagen og smittevei",
            "Isoler tilfeller",
            "Kartlegg nærkontakter",
            "Vurder meldeplikt",
            "Kontakt FHI for veiledning",
        ],
        "veiledere": ["FHI: Smittevernhåndboken", "Hdir: Smittevern"],
    },
    "legionella": {
        "sykdom": "Legionella / Legionærsjuke",
        "meldeplikt": "Gruppe A – meldes umiddelbart til kommuneoverlege og MSIS. Varsle Statsforvalter ved klynge (≥2 tilfeller).",
        "inkubasjonstid": "2–10 dager (vanligvis 5–6 dager)",
        "smitteperiode": "Ikke smitte mellom mennesker. Kilden (forurenset vann) er smittsom så lenge den er aktiv.",
        "smitteveier": [
            "Innånding av aerosoler fra boblebad, dusjer, kjøletårn",
            "Drikking av svært høy bakteriekonsentrasjon (sjelden)",
            "IKKE dråpesmitte person-til-person",
        ],
        "tiltak": [
            "Steng kontaminert vannkilde umiddelbart",
            "Ta vannprøver fra alle mulige kilder (boblebad, dusjer, kjøletårn, fontener)",
            "Varsle Mattilsynet og FHI",
            "Meld til MSIS (gruppe A) senest innen 24 timer",
            "Innhent besøksregistre for eksponeringsperioden",
            "Koordiner med Mattilsynet om kildesanering (termisk desinfeksjon 70°C eller klorering)",
            "Følg opp alle pasienter med klinisk Legionella-pneumoni",
            "Informer besøkende til det mistenkte stedet i eksponeringsperioden",
        ],
        "veiledere": ["FHI: Legionella-veilederen", "Mattilsynet: Vannhygiene", "ECDC: Legionella guidance"],
    },
    "tuberkulose": {
        "sykdom": "Tuberkulose (TB)",
        "meldeplikt": "Gruppe A – meldepliktig. Meldes til kommuneoverlege (innen 24t) og MSIS. Smittesporing er juridisk pålagt.",
        "inkubasjonstid": "Uker til måneder (primærinfeksjon). Reaktivering kan skje år/tiår senere.",
        "smitteperiode": "Smittsom ved aktiv lungetuberkulose – vanligvis ikke smittsom etter 2–4 uker med effektiv behandling.",
        "smitteveier": [
            "Luftbåren (dråpekjerner) ved hoste, nysing, sang",
            "Krev nær og langvarig eksponering (timer, ikke minutter)",
            "IKKE via kontaktflater eller dråpesmitte",
        ],
        "tiltak": [
            "Isoler indekspasient – ikke smittsom etter 2–4 ukers effektiv behandling",
            "Start DOTS-behandling (HRZE 2 mnd, HR 4 mnd)",
            "Kartlegg alle nærkontakter: husstand, arbeid, institusjon",
            "Systematisk screening: Mantoux/IGRA + røntgen thorax",
            "SYSVAK-sjekk av BCG-status for nærkontakter",
            "Vurder profylaktisk INH-behandling til risikogrupper (barn <5 år, immunsupprimerte)",
            "Resistensbestemmelse av alle stammer – ekskluder MDR-TB",
            "Varsle FHI og Statsforvalter ved klynge (≥2 tilfeller med felles eksponering)",
            "Samarbeid med UDI ved utbrudd på asylmottak",
        ],
        "veiledere": ["FHI: TB-veilederen", "Hdir: Nasjonal TB-strategi", "WHO: TB management guidelines"],
    },
    "meningokokk": {
        "sykdom": "Meningokokksykdom (Neisseria meningitidis)",
        "meldeplikt": "Gruppe A – meldes UMIDDELBART til kommuneoverlege og MSIS. Svært tidskritisk!",
        "inkubasjonstid": "2–10 dager (vanligvis 3–4 dager)",
        "smitteperiode": "Smittsom fra 7 dager før sykdomsdebut til 24 timer etter påbegynt antibiotikabehandling.",
        "smitteveier": [
            "Dråpesmitte ved nærkontakt <1 meter i >1 time",
            "Direkte kontakt med sekret fra munn/nese",
            "IKKE via luft over avstand eller overflatekontakt",
        ],
        "tiltak": [
            "RING 113 umiddelbart – livsfarlig sykdom!",
            "Definer nærkontakter: husstand og øvrige med ≥1 time ansikt-til-ansikt kontakt",
            "Profylaktisk antibiotika til nærkontakter INNEN 24 TIMER (Ciprofloksacin/Rifampicin)",
            "Meld til kommuneoverlege umiddelbart – ikke vent på prøvesvar",
            "Meld til MSIS – gruppe A",
            "Varsle skole/barnehage/arbeidsgiver ved relevante eksponeringer",
            "Vurder vaksine til nærkontakter (serogruppe-avhengig)",
            "Informer foreldre/foresatte ved skoleutbrudd",
            "Statsforvalter varsles ved klynge (≥2 tilfeller innen 4 uker)",
        ],
        "veiledere": ["FHI: Meningokokk-veilederen", "Hdir: Antibiotikabehandling meningitt", "NICE: Meningococcal disease"],
    },
    "e_coli": {
        "sykdom": "EHEC / VTEC (E. coli O157 og andre verotoksigene stammer)",
        "meldeplikt": "Gruppe A – meldes til kommuneoverlege og MSIS. Varsle Mattilsynet umiddelbart.",
        "inkubasjonstid": "1–10 dager (vanligvis 3–4 dager)",
        "smitteperiode": "Smittsom i perioden med symptomer og inntil 2 negative avføringsprøver (minst 24t mellom prøvene).",
        "smitteveier": [
            "Smittet mat: rå/understekt kjøtt, upasteurisert melk/juice, fersk frukt/grønt",
            "Forurenset drikkevann eller badevannn",
            "Kontaktsmitte (avføring–munn) – svært lav infeksiøs dose (<100 bakterier)",
        ],
        "tiltak": [
            "INGEN antibiotika – øker risiko for HUS!",
            "Varsle Mattilsynet umiddelbart for matkildesporing",
            "Isoler pasienter og barn i barnehage/skole til 2 negative prøver",
            "Meld til MSIS innen 24 timer (gruppe A)",
            "Kartlegg felles mateksponering de siste 10 dagene",
            "Identifiser og trekk tilbake mistenkt matvare",
            "Streng håndhygiene og kontaktsmittevern",
            "Overvåk for HUS – særlig hos barn og eldre (blodprøver: kreatinin, hematologi)",
            "Varsle Folkehelseinstituttet – kan rekvirere referansediagnostikk",
        ],
        "veiledere": ["FHI: EHEC-veilederen", "Mattilsynet: Matkildesporing", "ECDC: STEC/VTEC guidance"],
    },
}

# In-memory state
aktiv_hendelse = None
hendelseslogg = []
smittetilfeller = []
situasjonsrapporter = []
smitte_tiltak = []
eksponeringer = []

def neste_id(liste):
    if not liste:
        return 1
    return max(x["id"] for x in liste) + 1


# ── Demo-scenarioer ──────────────────────────────────────────────────────────

DEMO_SCENARIOER = [
    {
        "id": "norovirus_dønski",
        "navn": "🦠 Norovirusutbrudd – Dønski bo- og behandlingssenter",
        "lat": 59.9088, "lon": 10.5452,
        "beskrivelse": (
            "Norovirusutbrudd med 14 bekreftede tilfeller og 22 nærkontakter under oppfølging. "
            "Utbruddet startet på Skogly-avdelingen (2. etasje) og har spredt seg til Lunden-avdelingen. "
            "Tre ansatte har symptomer. Kohortering er iverksatt. FHI er varslet."
        ),
        "hendelse": {
            "type_id": "smitteutbrudd",
            "tittel": "Norovirusutbrudd – Dønski bo- og behandlingssenter",
            "beskrivelse": "14 bekreftede tilfeller, mulig felles smittekilde i kantine. Spredning til to avdelinger.",
            "lokasjon": "Dønski bo- og behandlingssenter, Halvard Birkelandsvei 31, Gjettum",
            "alvorlighetsgrad": "høy",
        },
        "logg": [
            {"type": "observasjon", "tittel": "Første varsling fra sykehjemsleder", "tekst": "Sykehjemsleder Anne Lie kontakter legevakt kl. 07:42. 3 beboere med akutt oppkast og diaré på Skogly-avdelingen siden natten.", "bruker": "Kommuneoverlege", "offset_min": -310},
            {"type": "beslutning", "tittel": "Smittevern iverksatt – kohortering Skogly", "tekst": "Besluttet kohortering av Skogly-avdeling (2. etg). Besøksforbud innført. Ansatte pålagt bruk av fullt smittevernsutstyr.", "bruker": "Kommuneoverlege", "offset_min": -280},
            {"type": "varsling", "tittel": "FHI varslet", "tekst": "Vakthavende lege hos FHI kontaktet kl. 08:30. Vurderer som sannsynlig norovirus-utbrudd. Anbefaler prøvetaking av minimum 3 tilfeller.", "bruker": "Kommuneoverlege", "offset_min": -250},
            {"type": "varsling", "tittel": "Statsforvalter varslet", "tekst": "Statsforvalter i Oslo og Viken varslet per telefon. Loggfører hendelsen i NOIS (Norsk overvåkingssystem for infeksjoner i helsetjenesten).", "bruker": "Beredskapskoordinator", "offset_min": -230},
            {"type": "tiltak", "tittel": "Prøver sendt Fürst Medisinsk Laboratorium", "tekst": "Avføringsprøver fra 3 beboere sendt med budbil til Fürst. Svar forventet innen 24 timer. Klinisk bilde sterkt forenlig med norovirus.", "bruker": "Bærum legevakt", "offset_min": -200},
            {"type": "observasjon", "tittel": "Nye tilfeller – Lunden-avdeling", "tekst": "Sykehjemsleder melder 4 nye tilfeller på Lunden-avdeling (3. etg). Mulig smittevei via felles kantine eller smittet ansatt. Kohortering utvides.", "bruker": "Kommuneoverlege", "offset_min": -150},
            {"type": "beslutning", "tittel": "Kantine stengt – felles smittekilde ikke utelukket", "tekst": "Kantinen stengt inntil videre. Kjøkkenrutiner gjennomgås. Mattilsynet orientert. Prøver av mat fra gårsdagens middag sikres.", "bruker": "Kommuneoverlege", "offset_min": -120},
            {"type": "møte", "tittel": "Kriseledelsesmøte – rådhuset Sandvika", "tekst": "Møte med kommunedirektør, helse- og omsorgssjef og beredskapskoordinator. Situasjonsbilde gjennomgått. Ekstra renhold bestilt. Plan for ansattvarsling vedtatt.", "bruker": "Kommunedirektør", "offset_min": -90},
            {"type": "tiltak", "tittel": "Ekstra renholdsressurser mobilisert", "tekst": "Avtalepartneren Nor-Clean innkalt med 6 ekstra renholdere. Klorbasert desinfeksjon av berørte arealer starter kl. 14:00.", "bruker": "Beredskapskoordinator", "offset_min": -60},
            {"type": "varsling", "tittel": "Pårørende informert", "tekst": "SMS sendt til pårørende til alle 88 beboere via Visma Viva. Besøksforbud informert. Telefon bemannet 08-20 for spørsmål.", "bruker": "Informasjonsansvarlig", "offset_min": -30},
            {"type": "observasjon", "tittel": "Laboratoriesvar bekreftet – Norovirus GII", "tekst": "Fürst bekrefter Norovirus genogruppe II i 2 av 3 prøver. Diagnosen sikret. FHI og Statsforvalter orientert. Fortsetter smittesporing.", "bruker": "Kommuneoverlege", "offset_min": -5},
        ],
        "smitte": [
            {"navn": "Bjørn Haugen", "alder": 84, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-23", "smittekilde_id": None, "lokasjon": "Dønski – Skogly-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "bekreftet"},
            {"navn": "Astrid Moen", "alder": 79, "kjønn": "Kvinne", "prøvedato": "2026-06-24", "symptomstart": "2026-06-23", "smittekilde_id": None, "lokasjon": "Dønski – Skogly-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "bekreftet"},
            {"navn": "Olav Sørensen", "alder": 91, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-24", "smittekilde_id": 1, "lokasjon": "Dønski – Skogly-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "bekreftet"},
            {"navn": "Randi Christensen", "alder": 77, "kjønn": "Kvinne", "prøvedato": "2026-06-24", "symptomstart": "2026-06-24", "smittekilde_id": None, "lokasjon": "Dønski – Lunden-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "bekreftet"},
            {"navn": "Per Johansen", "alder": 86, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-24", "smittekilde_id": 4, "lokasjon": "Dønski – Lunden-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "bekreftet"},
            {"navn": "Ingrid Bakke", "alder": 82, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": "2026-06-24", "smittekilde_id": 4, "lokasjon": "Dønski – Lunden-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "bekreftet"},
            {"navn": "Hjelper Anne Tveit (ansatt)", "alder": 34, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": "2026-06-24", "smittekilde_id": 1, "lokasjon": "Dønski – Skogly-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "bekreftet"},
            {"navn": "Kari Danielsen", "alder": 80, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": "2026-06-25", "smittekilde_id": 1, "lokasjon": "Dønski – Skogly-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "mistenkt"},
            {"navn": "Hans Eriksen", "alder": 88, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": "2026-06-25", "smittekilde_id": 4, "lokasjon": "Dønski – Lunden-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "mistenkt"},
            {"navn": "Sykepleier Lars Vik (ansatt)", "alder": 28, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": "2026-06-25", "smittekilde_id": 7, "lokasjon": "Dønski – Skogly-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "mistenkt"},
            {"navn": "Tor Strand", "alder": 75, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Dønski – Skogly-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "nærkontakt"},
            {"navn": "Marit Olsen", "alder": 83, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 4, "lokasjon": "Dønski – Lunden-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "nærkontakt"},
            {"navn": "Hjelper Nina Berg (ansatt)", "alder": 41, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 7, "lokasjon": "Dønski – Skogly-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "nærkontakt"},
            {"navn": "Gunnar Lie", "alder": 90, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 2, "lokasjon": "Dønski – Skogly-avd.", "institusjon": "Dønski bo- og behandlingssenter", "status": "nærkontakt"},
        ],
    },
    {
        "id": "strombortfall_rykkinn",
        "navn": "⚡ Langvarig strømbrudd – Rykkinn og Gommerud",
        "lat": 59.9289, "lon": 10.4794,
        "beskrivelse": (
            "Transformatorhavari kl. 03:12 medførte strømbrudd for ~4 200 husstander i Rykkinn og Gommerud-området. "
            "Rykkinn bo- og behandlingssenter er berørt. Nødaggregat er aktivert, men dekker kun akutte funksjoner. "
            "Elvia melder gjenopprettingstid tidligst kl. 18:00. Temperaturfall varslet."
        ),
        "hendelse": {
            "type_id": "strombortfall",
            "tittel": "Langvarig strømbrudd – Rykkinn / Gommerud (~4200 husstander)",
            "beskrivelse": "Transformatorhavari kl. 03:12. Rykkinn bo- og behandlingssenter på nødaggregat. Estimert gjenoppretting 18:00.",
            "lokasjon": "Rykkinn og Gommerud, Bærum – ~4200 husstander berørt",
            "alvorlighetsgrad": "høy",
        },
        "logg": [
            {"type": "observasjon", "tittel": "Strømbortfall meldt kl. 03:12", "tekst": "Elvia melder transformatorhavari ved Gommerud transformatorstasjon. Berørt område: Rykkinn, Gommerud, deler av Eiksmarka. Anslått 4 200 husstander.", "bruker": "Beredskapskoordinator", "offset_min": -430},
            {"type": "tiltak", "tittel": "Rykkinn bo- og behandlingssenter – nødaggregat aktivert", "tekst": "Sykehjemsleder bekrefter nødaggregat aktivert kl. 03:19. Dekker medisinsk utstyr, nødlys og varmeanlegg. Kjølerom for legemidler operativt.", "bruker": "Beredskapskoordinator", "offset_min": -420},
            {"type": "varsling", "tittel": "Kommunedirektør varslet", "tekst": "Kommunedirektør Erik Bjørnsen orientert kl. 04:00. Beslutter at kommuneoverlegen og beredskapskoordinator aktiveres.", "bruker": "Kommunedirektør", "offset_min": -390},
            {"type": "beslutning", "tittel": "Kriseledelse aktiv – koordinering fra rådhuset", "tekst": "Kommunal kriseledelse samles kl. 06:00 i rådhuset, Sandvika. Situasjonsbilde etablert. Prioritet: sårbare beboere på Rykkinn sykehjem og hjemmeboende med pleie- og omsorgsbehov.", "bruker": "Kommunedirektør", "offset_min": -360},
            {"type": "tiltak", "tittel": "Kartlegging – hjemmeboende med oksygenbehov", "tekst": "Hjemmetjenesten sender ut liste over 18 brukere med medisinsk utstyr (oksygen, respirator, ernæringspumpe) i berørt område. 6 kontaktes umiddelbart for status.", "bruker": "Helse- og omsorgssjef", "offset_min": -300},
            {"type": "varsling", "tittel": "Statsforvalter varslet kl. 07:30", "tekst": "Statsforvalter i Oslo og Viken varslet. Situasjonen beskrives som krevende men under kontroll. Ny statusoppdatering avtalt kl. 12:00.", "bruker": "Beredskapskoordinator", "offset_min": -270},
            {"type": "tiltak", "tittel": "Sivilforsvaret mobilisert – varmerom etablert", "tekst": "Sivilforsvaret Bærum setter opp varmerom på Rykkinn skole (gymsal) fra kl. 09:00. Røde Kors bistår med bemanning og forpleining.", "bruker": "Beredskapskoordinator", "offset_min": -240},
            {"type": "observasjon", "tittel": "Elvia oppdaterer estimat – forsinkelse", "tekst": "Elvia melder at reparasjon er mer omfattende enn antatt. Ny estimert gjenopprettingstid: kl. 20:00–22:00. Reservedeler er på vei fra Drammen.", "bruker": "Beredskapskoordinator", "offset_min": -180},
            {"type": "beslutning", "tittel": "Evakuering av 3 kritisk avhengige hjemmeboende", "tekst": "3 brukere med respiratoravhengighet evakueres til Bærum sykehus som forebyggende tiltak. Transport koordinert med AMK. Sykehuset bekrefter mottak.", "bruker": "Kommuneoverlege", "offset_min": -120},
            {"type": "tiltak", "tittel": "Kommunikasjon til innbyggere", "tekst": "Pressemelding publisert på baerum.kommune.no. SMS-varsling sendt til 4 318 telefonnummer i berørt sone via kommunens varslingssystem. NRK Oslo kontaktet.", "bruker": "Informasjonsansvarlig", "offset_min": -60},
        ],
        "smitte": [],
    },
    {
        "id": "meningitt_valler",
        "navn": "🦠 Meningokokksykdom – Valler videregående skole",
        "lat": 59.9205, "lon": 10.5812,
        "beskrivelse": (
            "Bekreftet tilfelle av meningokokksykdom type B hos 17-åring fra Valler videregående skole. "
            "Pasienten innlagt Bærum sykehus i kritisk tilstand. 280 nærkontakter på skolen identifisert. "
            "Masseprofylakse (Ciprofloxacin) iverksettes for 63 nærkontakter i klassen og berørte."
        ),
        "hendelse": {
            "type_id": "smitteutbrudd",
            "tittel": "Bekreftet meningokokksykdom type B – Valler VGS",
            "beskrivelse": "17-åring kritisk syk. 280 nærkontakter identifisert ved Valler VGS. Masseprofylakse iverksettes.",
            "lokasjon": "Valler videregående skole, Eiksmarka – Bærum sykehus",
            "alvorlighetsgrad": "kritisk",
        },
        "logg": [
            {"type": "varsling", "tittel": "Bærum sykehus varsler kommuneoverlegen", "tekst": "Infeksjonsavdelingen ved Bærum sykehus kontakter kommuneoverlegen kl. 22:45. 17-åring innlagt med klinisk meningitt, petekkier og septisk sjokk. Lumbal punksjon bekrefter meningokokker.", "bruker": "Kommuneoverlege", "offset_min": -480},
            {"type": "varsling", "tittel": "FHI varslet – meldepliktig sykdom", "tekst": "Meningokokksykdom er meldepliktig gruppe A. FHI varslet kl. 23:10. Nasjonalt referanselaboratorium kobles inn for typebestemmelse.", "bruker": "Kommuneoverlege", "offset_min": -460},
            {"type": "beslutning", "tittel": "Smittesporing startet – klasseliste innhentet", "tekst": "Rektor ved Valler VGS kontaktet. Klasseliste og fraværsregistre for Vg2A innhentet. 28 elever + 4 lærere definert som nærkontakter klasse 1.", "bruker": "Kommuneoverlege", "offset_min": -420},
            {"type": "tiltak", "tittel": "Masseprofylakse vedtatt – 63 nærkontakter", "tekst": "I samråd med FHI vedtatt profylaktisk Ciprofloxacin til 63 nærkontakter (klasse + venner + familie i husstand). Bærum legevakt forbereder utdeling fra kl. 08:00.", "bruker": "Kommuneoverlege", "offset_min": "380"},
            {"type": "varsling", "tittel": "Foresatte til berørte elever varslet – SMS og telefon", "tekst": "28 foresatte kontaktet per telefon kl. 06:30–07:30. Informasjon om profylakse, symptomer og oppmøte legevakt. Ingen andre med symptomer foreløpig.", "bruker": "Beredskapskoordinator", "offset_min": -300},
            {"type": "tiltak", "tittel": "Legevakt – utdeling profylakse starter kl. 08:00", "tekst": "Bærum legevakt har mottatt 120 kurer Ciprofloxacin 500mg fra sykehusapoteket. Eget mottaksrom etablert. 41 av 63 nærkontakter møtt innen kl. 10:00.", "bruker": "Bærum legevakt", "offset_min": -240},
            {"type": "varsling", "tittel": "Rektor og skolens ansatte orientert", "tekst": "Felles møte med rektor, rådgiver og tillitsvalgte kl. 09:00. Informasjon om smittevern, hvem som er nærkontakter og forventede tiltak. Skolen holdes åpen.", "bruker": "Kommuneoverlege", "offset_min": -200},
            {"type": "observasjon", "tittel": "FHI bekrefter type B – ingen lokal serogruppe-klynge", "tekst": "Nasjonalt referanselaboratorium bekrefter Neisseria meningitidis serogruppe B. Ingen andre kjente tilfeller i Bærum siste 6 måneder. Sporadisk tilfelle.", "bruker": "Kommuneoverlege", "offset_min": -120},
            {"type": "beslutning", "tittel": "Pressemelding publisert – åpenhetsstrategi", "tekst": "Pressemelding publisert i samråd med kommunedirektør. Ingen navn. Fokus på at tiltak er iverksatt og at risikoen for øvrige elever er lav. NRK, Budstikka og Aftenposten kontaktet.", "bruker": "Informasjonsansvarlig", "offset_min": -60},
        ],
        "smitte": [
            {"navn": "Indekspasient (anonymisert)", "alder": 17, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-23", "smittekilde_id": None, "lokasjon": "Eiksmarka, Bærum", "institusjon": "Valler videregående skole", "status": "bekreftet"},
            {"navn": "Nærkontakt 1 – klassekamerat", "alder": 17, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Eiksmarka, Bærum", "institusjon": "Valler VGS – Vg2A", "status": "nærkontakt"},
            {"navn": "Nærkontakt 2 – klassekamerat", "alder": 17, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Hosle, Bærum", "institusjon": "Valler VGS – Vg2A", "status": "nærkontakt"},
            {"navn": "Nærkontakt 3 – klassekamerat", "alder": 16, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Eiksmarka, Bærum", "institusjon": "Valler VGS – Vg2A", "status": "nærkontakt"},
            {"navn": "Nærkontakt 4 – faglærer", "alder": 44, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Bekkestua, Bærum", "institusjon": "Valler VGS", "status": "nærkontakt"},
            {"navn": "Nærkontakt 5 – søsken i husstand", "alder": 14, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Eiksmarka, Bærum", "institusjon": "Eiksmarka ungdomsskole", "status": "nærkontakt"},
        ],
    },
    {
        "id": "brann_østerås",
        "navn": "🔥 Brann – Østerås sykehjem (pågående evakuering)",
        "lat": 59.9257, "lon": 10.5694,
        "beskrivelse": (
            "Brann i teknisk rom i kjeller ved Østerås sykehjem kl. 14:33. "
            "Brannvesen på stedet. 75 beboere evakuert til parkeringsplassen. "
            "Ingen bekreftet omkomne, men 4 beboere har røykskader og er transportert til Bærum sykehus. "
            "Bygningsmessig vurdering pågår – bygget kan bli ubeboelig."
        ),
        "hendelse": {
            "type_id": "brann_sykehjem",
            "tittel": "Brann i kjeller – Østerås sykehjem (75 beboere evakuert)",
            "beskrivelse": "Brann i teknisk rom kl. 14:33. 75 beboere evakuert. 4 med røykskader til Bærum sykehus. Gjeninnflytting usikker.",
            "lokasjon": "Østerås sykehjem, Østerås, Bærum",
            "alvorlighetsgrad": "kritisk",
        },
        "logg": [
            {"type": "observasjon", "tittel": "Brannalarm utløst – kjeller Østerås sykehjem kl. 14:33", "tekst": "Automatisk brannalarm varsler 110. Ansatte starter evakuering i henhold til brannplan. Brannvesen rykker ut fra Bærum brannstasjon.", "bruker": "Sykehjemsleder", "offset_min": -180},
            {"type": "tiltak", "tittel": "Evakuering fullført – 75 beboere ute kl. 14:51", "tekst": "Alle 75 beboere evakuert til parkeringsplassen i løpet av 18 minutter. 12 i rullestol, 4 sengeliggende transportert på rullemadrass. Brannvesen bekrefter alle ute.", "bruker": "Sykehjemsleder", "offset_min": -162},
            {"type": "varsling", "tittel": "AMK 113 – 4 beboere med røykskader", "tekst": "4 beboere med røykinnånding: Kari (82 år), Helge (91 år), Solveig (77 år), Oddvar (88 år). AMK sender 3 ambulanser. Alle våkne og kontaktbare.", "bruker": "Sykehjemsleder", "offset_min": -155},
            {"type": "varsling", "tittel": "Kommuneoverlege og kommunedirektør varslet", "tekst": "Kommuneoverlege og kommunedirektør Erik Bjørnsen varslet kl. 14:55. Kriseledelse aktiveres.", "bruker": "Beredskapskoordinator", "offset_min": -150},
            {"type": "beslutning", "tittel": "Beboere til midlertidig husly – Østerås skole åpnes", "tekst": "Ordfører og kommunedirektør beslutter å åpne Østerås skole som midlertidig husly. Rektor kontaktet. Sivilforsvaret og Røde Kors mobiliseres for støtte.", "bruker": "Kommunedirektør", "offset_min": -130},
            {"type": "tiltak", "tittel": "Medisinliste og journaler sikret", "tekst": "Sykepleier bekrefter medisinliste hentet ut (papirkopi på vaktrom) og nettbrett med Gerica-tilgang. Alle faste medisiner kan gjenopprettes. Bærum legevakt varslet for støtte.", "bruker": "Sykehjemsleder", "offset_min": -110},
            {"type": "varsling", "tittel": "Statsforvalter varslet – alvorlig hendelse", "tekst": "Statsforvalter i Oslo og Viken varslet kl. 15:30. Hendelsen vurderes som alvorlig. Fylkeslegen ønsker løpende oppdateringer. Kommunen rapporterer hver 2. time.", "bruker": "Beredskapskoordinator", "offset_min": -90},
            {"type": "observasjon", "tittel": "Brannteknikere: bygget kan ikke benyttes i natt", "tekst": "Brannsjef melder at brannskade er begrenset til kjeller, men røyk- og vannskader i 1. etg gjør bygget ubeboelig minimum 48–72 timer. Langsiktig løsning må avklares.", "bruker": "Brannvesen", "offset_min": -60},
            {"type": "beslutning", "tittel": "Innleggelse/omplassering av alle 75 beboere vedtatt", "tekst": "Kommunedirektør beslutter omplassering av alle 75 beboere. 28 til Dønski, 19 til Rykkinn, 14 til Sandvika sykehjem. 14 beboere hjem til pårørende. Koordinering starter.", "bruker": "Kommunedirektør", "offset_min": -30},
            {"type": "tiltak", "tittel": "Pårørende varslet – SMS og telefon", "tekst": "SMS til 68 pårørenderegistrerte via Visma. Telefon til pårørende til de 4 sykehusinnlagte. Informasjon om midlertidig plassering sendes ut så snart det er avklart.", "bruker": "Informasjonsansvarlig", "offset_min": -10},
        ],
        "smitte": [],
    },
    {
        "id": "influensa_bekkestua",
        "navn": "🦠 Influensa A(H3N2) – Bekkestua barneskole",
        "lat": 59.9127, "lon": 10.5621,
        "beskrivelse": (
            "18 elever med influensalignende sykdom fordelt på 3 klasser (3A, 3B, 4A). "
            "Skolefravær på 34%. 2 lærere syke. Mulig felles smittekilde i kantinen fredag."
        ),
        "hendelse": {
            "type_id": "smitteutbrudd",
            "tittel": "Influensa A(H3N2) – Bekkestua barneskole",
            "beskrivelse": "18 elever med influensalignende sykdom i 3 klasser. 34% fravær. 2 lærere syke. Mulig kantinesmitte.",
            "lokasjon": "Bekkestua barneskole, Magnus Smidsrødsvei 1, Bekkestua",
            "alvorlighetsgrad": "middels",
        },
        "logg": [
            {"type": "varsling", "tittel": "Rektor varsler kommunehelsetjenesten", "tekst": "Rektor Hanne Lund ved Bekkestua barneskole kontakter kommunehelsetjenesten kl. 08:15. Uvanlig høyt fravær i 3A og 3B – over 10 elever ikke møtt. Klassekontakter melder om influensasymptomer.", "bruker": "Kommuneoverlege", "offset_min": -420},
            {"type": "varsling", "tittel": "FHI orientert om mulig utbrudd", "tekst": "FHIs influensaovervåkingsseksjon orientert per telefon. Vurderer som forenlig med sirkulerende H3N2-variant. Anbefaler prøvetaking og kartlegging av smittekilde.", "bruker": "Kommuneoverlege", "offset_min": -380},
            {"type": "observasjon", "tittel": "Massefravær kartlagt – 18 elever, 2 lærere", "tekst": "Oppdatert fraværsliste: 18 elever i 3A (8), 3B (6), 4A (4) har influensasymptomer. Faglærer Tor Bakken (3A) og kontaktlærer Mette Holm (3B) er syke. Samlet skolefravær 34%.", "bruker": "Beredskapskoordinator", "offset_min": -340},
            {"type": "varsling", "tittel": "Foreldre varslet via SMS", "tekst": "SMS sendt til alle foresatte i 3A, 3B og 4A via Visma InSchool kl. 10:30. Informasjon om symptomer, karanteneråd og råd om legekontakt ved forverring.", "bruker": "Informasjonsansvarlig", "offset_min": -300},
            {"type": "varsling", "tittel": "Kommunehelsetjeneste kontaktet – prøveplan", "tekst": "Bærum legevakt bistår med hurtigtester for influensa for syke elever og lærere som møter til legen. 5 prøver tatt første dag, svar forventet i morgen.", "bruker": "Bærum legevakt", "offset_min": -260},
            {"type": "beslutning", "tittel": "Vurdering av stenging av berørte klasser", "tekst": "Kommuneoverlege og rektor vurderer midlertidig stenging av 3A og 3B i 3 dager. Beslutning utsatt til prøvesvar foreligger. Renhold av klasserom iverksatt.", "bruker": "Kommuneoverlege", "offset_min": -220},
            {"type": "tiltak", "tittel": "Prøver sendt til analyse – Fürst lab", "tekst": "Nasofaryngsprøver fra 5 elever med mest uttalte symptomer sendt Fürst Medisinsk Laboratorium for PCR-analyse. Svar forventet innen 24 timer.", "bruker": "Bærum legevakt", "offset_min": -180},
            {"type": "tiltak", "tittel": "Smitteverntiltak iverksatt ved skolen", "tekst": "Ekstra håndhygienestasjoner plassert ved innganger og klasseromskorridorer. Kantinen innfører enkeltporsjonering. Renhold av kontaktflater tre ganger daglig. Elever med symptomer sendes hjem.", "bruker": "Sykehjemsleder", "offset_min": -60},
        ],
        "smitte": [
            {"navn": "Oliver Dahl", "alder": 9, "kjønn": "Mann", "prøvedato": "2026-06-23", "symptomstart": "2026-06-22", "smittekilde_id": None, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3A", "status": "bekreftet"},
            {"navn": "Sofie Andersen", "alder": 9, "kjønn": "Kvinne", "prøvedato": "2026-06-23", "symptomstart": "2026-06-23", "smittekilde_id": 1, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3A", "status": "bekreftet"},
            {"navn": "Noah Berg", "alder": 8, "kjønn": "Mann", "prøvedato": "2026-06-23", "symptomstart": "2026-06-23", "smittekilde_id": 1, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3A", "status": "bekreftet"},
            {"navn": "Faglærer Tor Bakken (ansatt)", "alder": 42, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-23", "smittekilde_id": 1, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3A", "status": "bekreftet"},
            {"navn": "Emma Kristiansen", "alder": 8, "kjønn": "Kvinne", "prøvedato": "2026-06-24", "symptomstart": "2026-06-23", "smittekilde_id": 1, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3B", "status": "bekreftet"},
            {"navn": "Liam Johansen", "alder": 9, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-24", "smittekilde_id": 5, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3B", "status": "bekreftet"},
            {"navn": "Kontaktlærer Mette Holm (ansatt)", "alder": 35, "kjønn": "Kvinne", "prøvedato": "2026-06-24", "symptomstart": "2026-06-24", "smittekilde_id": 5, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3B", "status": "mistenkt"},
            {"navn": "Maja Larsen", "alder": 9, "kjønn": "Kvinne", "prøvedato": "2026-06-24", "symptomstart": "2026-06-24", "smittekilde_id": 1, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 4A", "status": "mistenkt"},
            {"navn": "Lukas Halvorsen", "alder": 9, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": "2026-06-25", "smittekilde_id": 3, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3A", "status": "mistenkt"},
            {"navn": "Ingrid Nygaard", "alder": 8, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3A", "status": "nærkontakt"},
            {"navn": "Filip Olsen", "alder": 9, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 5, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3B", "status": "nærkontakt"},
            {"navn": "Astrid Mikkelsen", "alder": 9, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": None, "smittekilde_id": 4, "lokasjon": "Bekkestua", "institusjon": "Bekkestua barneskole – 3A", "status": "nærkontakt"},
        ],
    },
    {
        "id": "meslinger_fornebu",
        "navn": "🦠 Meslinger – Fornebu International School",
        "lat": 59.8950, "lon": 10.6198,
        "beskrivelse": (
            "Bekreftet meslingtilfelle hos 8-åring. Uvaksinert familie. "
            "180 nærkontakter kartlagt på skolen. Vaksinasjonsdekning under 85% i denne aldersgruppen på Fornebu. FHI aktivert."
        ),
        "hendelse": {
            "type_id": "smitteutbrudd",
            "tittel": "Bekreftet meslinger – Fornebu International School",
            "beskrivelse": "Bekreftet meslingtilfelle hos 8-åring. 180 nærkontakter kartlagt. Vaksinasjonsdekning <85%. FHI aktivert.",
            "lokasjon": "Fornebu International School, Fornebu, Bærum",
            "alvorlighetsgrad": "kritisk",
        },
        "logg": [
            {"type": "varsling", "tittel": "Bærum sykehus varsler kommuneoverlegen – bekreftet meslinger", "tekst": "Barneavdelingen ved Bærum sykehus bekrefter meslingdiagnose hos 8-åring innlagt med høy feber, koplik-flekker og karakteristisk utslett. Familie er uvaksinert. Kommuneoverlege varslet umiddelbart.", "bruker": "Kommuneoverlege", "offset_min": -580},
            {"type": "varsling", "tittel": "FHI varslet – meldepliktig gruppe A", "tekst": "Meslinger er meldepliktig gruppe A (§ 2-1 smittevernloven). FHI varslet kl. 16:20. Nasjonalt referanselaboratorium kobles inn. WHO-varsling vurderes via FHI. Sak opprettet i MSIS.", "bruker": "Kommuneoverlege", "offset_min": -540},
            {"type": "beslutning", "tittel": "Smittesporing – skolens liste innhentet", "tekst": "Rektor ved Fornebu International School kontaktet kl. 17:00. Fullstendig elevliste og fraværsregistre utlevert. 180 elever og 22 ansatte definert som mulige nærkontakter.", "bruker": "Beredskapskoordinator", "offset_min": -500},
            {"type": "tiltak", "tittel": "SYSVAK-sjekk igangsatt", "tekst": "FHI bistår med oppslag i SYSVAK (nasjonalt vaksinasjonsregister) for alle nærkontakter. Foreløpig resultat: vaksinasjonsdekning i aktuell aldersgruppe på Fornebu er 82% – under anbefalt terskel på 95%.", "bruker": "Kommuneoverlege", "offset_min": -460},
            {"type": "tiltak", "tittel": "Vaksinasjonstilbud til nærkontakter – MMR innen 72 timer", "tekst": "Bærum legevakt tilbyr posteksponeringsimmunisering (MMR-vaksine) til alle uvaksinerte nærkontakter under 40 år innen 72 timer etter eksponering. 31 personer har allerede møtt.", "bruker": "Bærum legevakt", "offset_min": -420},
            {"type": "varsling", "tittel": "Alle foreldre på skolen varslet – brev og SMS", "tekst": "Rektor sendte skriftlig varsel til alle 340 foresatte på skolen med informasjon om meslingtilfelle, symptomer, vaksinasjonsstatus og hva man skal gjøre. FHIs informasjonsmateriell vedlagt.", "bruker": "Informasjonsansvarlig", "offset_min": -380},
            {"type": "beslutning", "tittel": "Uvaksinerte nærkontakter ekskludert fra skolen", "tekst": "I henhold til FHIs veileder ekskluderes uvaksinerte nærkontakter fra skolen i 21 dager. 18 elever og 2 ansatte berørt. Rektor informert. Hjemmeopplæring organiseres.", "bruker": "Kommuneoverlege", "offset_min": -300},
            {"type": "varsling", "tittel": "Mediehenvendelser – koordinert kommunikasjon", "tekst": "NRK Oslo, Budstikka og to internasjonale medier har henvendt seg. Pressemelding publisert i koordinering med FHI. Kommuneoverlege stiller til intervju kl. 14:00.", "bruker": "Informasjonsansvarlig", "offset_min": -200},
            {"type": "tiltak", "tittel": "Immunoglobulin til sårbare grupper", "tekst": "Immunoglobulin gis til spedbarn under 6 måneder og immunsupprimerte nærkontakter innen 6 dager etter eksponering. 3 personer identifisert. Sykehuset administrerer behandlingen.", "bruker": "Bærum sykehus", "offset_min": -120},
            {"type": "observasjon", "tittel": "To nye mistenkte tilfeller meldt", "tekst": "Fastlege melder to nye tilfeller med meslinglignende utslett – begge uvaksinerte barn fra skolen. Prøver tatt og sendt til referanselaboratoriet. Smittesporing utvides.", "bruker": "Kommuneoverlege", "offset_min": -30},
        ],
        "smitte": [
            {"navn": "Indekspasient (anonymisert)", "alder": 8, "kjønn": "Kvinne", "prøvedato": "2026-06-22", "symptomstart": "2026-06-19", "smittekilde_id": None, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu International School", "status": "bekreftet"},
            {"navn": "Nærkontakt – uvaksinert klassekamerat 1", "alder": 7, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-24", "smittekilde_id": 1, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu International School", "status": "mistenkt"},
            {"navn": "Nærkontakt – uvaksinert klassekamerat 2", "alder": 9, "kjønn": "Kvinne", "prøvedato": "2026-06-24", "symptomstart": "2026-06-24", "smittekilde_id": 1, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu International School", "status": "mistenkt"},
            {"navn": "Nærkontakt – elev trinn 1", "alder": 7, "kjønn": "Mann", "prøvedato": "2026-06-23", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu International School", "status": "nærkontakt"},
            {"navn": "Nærkontakt – elev trinn 2", "alder": 8, "kjønn": "Kvinne", "prøvedato": "2026-06-23", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu International School", "status": "nærkontakt"},
            {"navn": "Nærkontakt – elev trinn 3", "alder": 10, "kjønn": "Mann", "prøvedato": "2026-06-23", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu International School", "status": "nærkontakt"},
            {"navn": "Nærkontakt – elev trinn 4", "alder": 8, "kjønn": "Kvinne", "prøvedato": "2026-06-23", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu International School", "status": "nærkontakt"},
            {"navn": "Nærkontakt – elev trinn 5", "alder": 9, "kjønn": "Mann", "prøvedato": "2026-06-23", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu International School", "status": "nærkontakt"},
        ],
    },
    {
        "id": "matforgiftning_sandvika",
        "navn": "💧 Matforgiftning – Restaurant Smaken, Sandvika",
        "lat": 59.8897, "lon": 10.5220,
        "beskrivelse": (
            "23 gjester med gastroenteritt etter selskapsarrangement lørdag kveld. "
            "Staphylococcus aureus mistenkt. Mattilsynet har stengt kjøkkenet. "
            "6 innlagt Bærum sykehus med alvorlig dehydrering."
        ),
        "hendelse": {
            "type_id": "matbaren",
            "tittel": "Matforgiftning – Restaurant Smaken, Sandvika (23 tilfeller)",
            "beskrivelse": "23 gjester syke etter selskapsarrangement. Staphylococcus aureus mistenkt. Kjøkken stengt av Mattilsynet. 6 sykehusinnlagt.",
            "lokasjon": "Restaurant Smaken, Rådhusgata 14, Sandvika",
            "alvorlighetsgrad": "høy",
        },
        "logg": [
            {"type": "varsling", "tittel": "Mattilsynet varslet – matbåren sykdom", "tekst": "Kommuneoverlege mottar melding søndag morgen om 8 personer med akutt oppkast og diaré etter middag på Restaurant Smaken lørdag kveld. Mattilsynet region øst varslet umiddelbart.", "bruker": "Kommuneoverlege", "offset_min": -480},
            {"type": "beslutning", "tittel": "Kjøkken stengt – Mattilsynet", "tekst": "Mattilsynet gjennomfører strakstilsyn og stenger kjøkkenet ved Restaurant Smaken kl. 10:30. Meny og råvarelogistikk gjennomgås. Kjøkkenansatte intervjues.", "bruker": "Mattilsynet", "offset_min": -420},
            {"type": "tiltak", "tittel": "Prøver av matrester tatt til analyse", "tekst": "Mattilsynet sikrer matrester fra kveldens meny: rekesalat, hollandaisesaus og dessertbuffé. Prøver sendt til Folkehelseinstituttets matlaboratorium. Svar forventet 48-72 timer.", "bruker": "Mattilsynet", "offset_min": "380"},
            {"type": "tiltak", "tittel": "Gjesteliste fra arrangementet innhentet", "tekst": "Restauranten leverer gjesteliste for selskapsarrangementet – 87 gjester totalt. Alle kontaktes per telefon for registrering av symptomer. 23 bekrefter mage-tarmsymptomer.", "bruker": "Beredskapskoordinator", "offset_min": -340},
            {"type": "varsling", "tittel": "6 gjester innlagt Bærum sykehus", "tekst": "AMK melder 6 innleggelser ved Bærum sykehus med alvorlig dehydrering og oppkast. Alle stabile per nå. Medisinsk avdeling er orientert om mulig matforgiftning.", "bruker": "Bærum legevakt", "offset_min": -300},
            {"type": "observasjon", "tittel": "Staphylococcus aureus mistenkt – rask inkubasjonstid", "tekst": "FHI konsultert: inkubasjonstid på 2–4 timer og dominerende oppkastsymptomer peker mot Staphylococcus aureus enterotoksin. Hollandaisesausen er høyrisikoprodukt – manglende kjøling mistenkt.", "bruker": "Kommuneoverlege", "offset_min": -240},
            {"type": "tiltak", "tittel": "Smittesporing av matkjeden", "tekst": "Leverandør av reker og egg til restauranten er identifisert. Mattilsynet varsler leverandøren og starter sporingsarbeid bakover i matkjeden.", "bruker": "Mattilsynet", "offset_min": -180},
            {"type": "varsling", "tittel": "Mediehåndtering – pressemelding", "tekst": "Pressemelding publisert i samarbeid med Mattilsynet. Ingen navn på restaurant nevnt i første runde. NRK og Budstikka har fått bekreftet at det pågår en etterforskning.", "bruker": "Informasjonsansvarlig", "offset_min": -90},
            {"type": "observasjon", "tittel": "Sykehusinnlagte stabilisert – 2 utskrevet", "tekst": "Bærum sykehus melder at 2 av 6 innlagte er utskrevet etter rehydrering. Resterende 4 har det bra. Ingen intensivinnleggelser. Rask bedring forenlig med Staph-enterotoksin.", "bruker": "Bærum sykehus", "offset_min": -30},
        ],
        "smitte": [
            {"navn": "Gjest 1 – Kari Lie (arrangement)", "alder": 52, "kjønn": "Kvinne", "prøvedato": "2026-06-22", "symptomstart": "2026-06-21", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": "Restaurant Smaken", "status": "bekreftet"},
            {"navn": "Gjest 2 – Per Andersen (arrangement)", "alder": 48, "kjønn": "Mann", "prøvedato": "2026-06-22", "symptomstart": "2026-06-21", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": "Restaurant Smaken", "status": "bekreftet"},
            {"navn": "Gjest 3 – Anne Marte Gundersen", "alder": 61, "kjønn": "Kvinne", "prøvedato": "2026-06-22", "symptomstart": "2026-06-21", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": "Restaurant Smaken", "status": "bekreftet"},
            {"navn": "Gjest 4 – Bjørn Hagen", "alder": 55, "kjønn": "Mann", "prøvedato": "2026-06-22", "symptomstart": "2026-06-22", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": "Restaurant Smaken", "status": "bekreftet"},
            {"navn": "Gjest 5 – Silje Bakken", "alder": 39, "kjønn": "Kvinne", "prøvedato": "2026-06-22", "symptomstart": "2026-06-22", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": "Restaurant Smaken", "status": "bekreftet"},
            {"navn": "Gjest 6 – Trond Moe (innlagt sykehus)", "alder": 65, "kjønn": "Mann", "prøvedato": "2026-06-22", "symptomstart": "2026-06-21", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": None, "status": "mistenkt"},
            {"navn": "Gjest 7 – Hilde Karlsen (innlagt sykehus)", "alder": 72, "kjønn": "Kvinne", "prøvedato": "2026-06-22", "symptomstart": "2026-06-21", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": None, "status": "mistenkt"},
            {"navn": "Gjest 8 – Lars Christensen", "alder": 25, "kjønn": "Mann", "prøvedato": "2026-06-23", "symptomstart": "2026-06-22", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": None, "status": "mistenkt"},
            {"navn": "Gjest 9 – Ingrid Sørensen", "alder": 44, "kjønn": "Kvinne", "prøvedato": "2026-06-23", "symptomstart": "2026-06-22", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": None, "status": "mistenkt"},
            {"navn": "Gjest 10 – Erik Haugen (partner av gjest)", "alder": 50, "kjønn": "Mann", "prøvedato": "2026-06-23", "symptomstart": None, "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": None, "status": "nærkontakt"},
        ],
    },
    {
        "id": "cyberangrep_baerum",
        "navn": "💻 Cyberangrep – Bærum kommunes IT-systemer",
        "lat": 59.8893, "lon": 10.5214,
        "beskrivelse": (
            "Ransomware-angrep oppdaget kl. 02:14. Journalsystemer (Gerica, DIPS), epost og Teams utilgjengelig. "
            "Sykehjem og legevakt på papirbaserte rutiner. NSM og Datatilsynet varslet. Politiet etterforsker."
        ),
        "hendelse": {
            "type_id": "cyberangrep",
            "tittel": "Ransomware-angrep – Bærum kommunes IT-infrastruktur",
            "beskrivelse": "Ransomware oppdaget kl. 02:14. Gerica, DIPS, epost og Teams nede. Papirbaserte rutiner aktivert. NSM varslet.",
            "lokasjon": "Bærum rådhus / IT-infrastruktur, Sandvika",
            "alvorlighetsgrad": "kritisk",
        },
        "logg": [
            {"type": "observasjon", "tittel": "Ransomware oppdaget kl. 02:14 – IT-vakt varsler", "tekst": "IT-vakten ved Bærum kommune oppdager kl. 02:14 at servere er kryptert med ransomware. Løsepengekrav på 3 millioner kroner vises på skjermer. Gerica og DIPS (journalsystemer), epost og Teams er utilgjengelige.", "bruker": "IT-avdelingen", "offset_min": -600},
            {"type": "beslutning", "tittel": "Isolering av berørte systemer", "tekst": "IT-sjef beslutter kl. 02:30 å isolere alle infiserte servere fra nettverket. Internett-tilgang til rådhuset og alle kommunale bygg kuttes midlertidig. Dette stopper videre spredning.", "bruker": "IT-avdelingen", "offset_min": -570},
            {"type": "varsling", "tittel": "Kommunedirektør og krisestab varslet", "tekst": "Kommunedirektør Erik Bjørnsen varslet kl. 03:00. Krisestab innkalles til møte kl. 07:00 i rådhuset. Beredskapskoordinator og kommuneoverlege orientert.", "bruker": "Kommunedirektør", "offset_min": -540},
            {"type": "tiltak", "tittel": "Papirbaserte rutiner aktivert – sykehjem og legevakt", "tekst": "Alle 7 sykehjem og Bærum legevakt instruert om overgang til papirbaserte prosedyrer. Medisinlister printes fra siste tilgjengelige backup. Ansatte kontaktes via privat mobiltelefon.", "bruker": "Helse- og omsorgssjef", "offset_min": -480},
            {"type": "varsling", "tittel": "NSM varslet – nasjonal cybersikkerhetsmyndighet", "tekst": "Nasjonal sikkerhetsmyndighet (NSM) varslet kl. 05:00. NSM sender bistandsteam (NorCERT) til Sandvika. Datatilsynet varslet om mulig personvernbrudd. Politiets cyberkriminalitetssenter (NC3) etterforsker.", "bruker": "IT-avdelingen", "offset_min": -420},
            {"type": "tiltak", "tittel": "Kommunikasjon til ansatte via privat mobil", "tekst": "Alle avdelingsledere instruert om alternativ kommunikasjon. Ny midlertidig SMS-varslingskanal opprettet. Ansatte bes ikke bruke kommunens nettverk eller enheter inntil videre.", "bruker": "Informasjonsansvarlig", "offset_min": -360},
            {"type": "tiltak", "tittel": "Backup-systemer og DR-plan aktivert", "tekst": "IT-sjef bekrefter at siste rene backup er fra 3 dager tilbake. Disaster Recovery-plan aktivert. Ekstern IT-leverandør (Sopra Steria) innkalt for krisehjelp. Forventet gjenopprettingstid vurderes.", "bruker": "IT-avdelingen", "offset_min": -300},
            {"type": "observasjon", "tittel": "Smittevernmodulen og pasientdata potensielt eksfiltrert", "tekst": "NSM tekniker varsler at angriperne trolig har eksfiltrert data før kryptering. Personopplysninger om kommunens innbyggere, ansatte og pasienter kan være kompromittert. Datatilsynet ønsker full rapport.", "bruker": "NSM", "offset_min": -200},
            {"type": "varsling", "tittel": "Pressemelding publisert – åpenhetsstrategi", "tekst": "Kommunedirektør beslutter full åpenhet. Pressemelding publisert kl. 09:00 med bekreftelse av angrepet. Fokus på at helsetjenestene fungerer med manuelle rutiner og at innbyggerne ikke trenger å bekymre seg.", "bruker": "Informasjonsansvarlig", "offset_min": -120},
            {"type": "observasjon", "tittel": "Estimat gjenoppretting: 5–10 virkedager", "tekst": "NSM og Sopra Steria estimerer 5–10 virkedager for full gjenoppretting. Prioritet 1: Gerica og legevaktsystemene. Prioritet 2: Epost og Teams. Prioritet 3: Administrative systemer.", "bruker": "IT-avdelingen", "offset_min": -30},
        ],
        "smitte": [],
    },
    {
        "id": "forurenset_vann_fornebu",
        "navn": "💧 Forurenset drikkevann – Fornebu-området",
        "lat": 59.8950, "lon": 10.6198,
        "beskrivelse": (
            "Kokevarsel utstedt for Fornebu og deler av Høvik etter funn av E. coli i rutineprøver fra Fornebupumpestasjonen. "
            "~18 000 innbyggere berørt. Vannverket jobber med å lokalisere forurensningspunktet. "
            "Legevakten melder økt pågang av pasienter med mage-/tarmsymptomer siden i går."
        ),
        "hendelse": {
            "type_id": "forurenset_vann",
            "tittel": "E. coli i drikkevann – kokevarsel Fornebu og Høvik (~18 000 innb.)",
            "beskrivelse": "Kokevarsel utstedt. E. coli påvist i rutinemåling Fornebupumpestasjon. Legevakt melder økt pågang mageplager.",
            "lokasjon": "Fornebu og Høvik, Bærum – ~18 000 innbyggere",
            "alvorlighetsgrad": "høy",
        },
        "logg": [
            {"type": "observasjon", "tittel": "Bærum Vann melder positivt prøvesvar", "tekst": "Bærum Vann kontakter kommuneoverlegen kl. 09:15. Rutineprøve fra Fornebupumpestasjon tatt 23. juni viser E. coli 42 CFU/100ml. Bekreftende analyse pågår.", "bruker": "Kommuneoverlege", "offset_min": -360},
            {"type": "beslutning", "tittel": "Kokevarsel utstedt kl. 09:45", "tekst": "Kokevarsel utstedt for Fornebu og Høvik (kartreferanse Bærum Vann forsyningssone 4B). Alle som bruker vann til drikke, matlaging og tannpuss skal koke vannet.", "bruker": "Kommuneoverlege", "offset_min": -330},
            {"type": "varsling", "tittel": "SMS-varsling sendt til 18 420 mottakere", "tekst": "Kommunens SMS-varslingssystem aktivert kl. 09:52. Melding sendt til alle registrerte mobilnummer i berørt sone. Melding også publisert på baerum.kommune.no og Facebook.", "bruker": "Informasjonsansvarlig", "offset_min": -320},
            {"type": "varsling", "tittel": "Mattilsynet varslet – tilsynssak opprettet", "tekst": "Mattilsynet region øst varslet kl. 10:00. Tilsynssak opprettet. Mattilsynet vil bistå Bærum Vann med prøvetaking og kildelokalisering.", "bruker": "Kommuneoverlege", "offset_min": -300},
            {"type": "tiltak", "tittel": "Barnehager og skoler på Fornebu varslet", "tekst": "Alle 6 barnehager og 2 skoler på Fornebu direkte kontaktet per telefon. Samtlige bekrefter mottatt kokevarsel. Matlaging stanset. Flaskevannslevering fra kommunal lager igangsatt.", "bruker": "Beredskapskoordinator", "offset_min": -280},
            {"type": "varsling", "tittel": "Statsforvalter varslet", "tekst": "Statsforvalter orientert kl. 10:30. Situasjonen vurderes som alvorlig men håndterbar. Ny oppdatering avtalt når kilde er lokalisert.", "bruker": "Kommuneoverlege", "offset_min": -260},
            {"type": "observasjon", "tittel": "Legevakt – 23 pasienter med mage-/tarmsymptomer", "tekst": "Legevaktlege melder 23 pasienter med gastroenteritt siden gårsdagen fra Fornebu-adressen. Prøver tatt av 8 pasienter for VTEC-analyse. Mulig allerede pågående utbrudd.", "bruker": "Bærum legevakt", "offset_min": -200},
            {"type": "tiltak", "tittel": "Vanndistribusjon – Sivilforsvaret og butikker", "tekst": "Sivilforsvaret setter opp 3 distribusjonsstasjoner for tappevann (Fornebuporten, Telenor-campus, Fornebu senter). Bunnpris og Rema 1000 på Fornebu tømmer flaskevanns-lager.", "bruker": "Beredskapskoordinator", "offset_min": -150},
            {"type": "observasjon", "tittel": "Mulig kilde identifisert – tilbakesugventil", "tekst": "Bærum Vann teknikere finner defekt tilbakesugventil ved Fornebu pumpestasjonen. Pumpestasjonen isoleres kl. 14:00. Vann reroutes via alternativ ledning.", "bruker": "Bærum Vann", "offset_min": -60},
        ],
        "smitte": [
            {"navn": "Pasient 1 – Fornebu (anonymisert)", "alder": 34, "kjønn": "Kvinne", "prøvedato": "2026-06-24", "symptomstart": "2026-06-23", "smittekilde_id": None, "lokasjon": "Fornebu, Bærum", "institusjon": None, "status": "bekreftet"},
            {"navn": "Pasient 2 – Fornebu (anonymisert)", "alder": 7, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-23", "smittekilde_id": None, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu barnehage", "status": "bekreftet"},
            {"navn": "Pasient 3 – Høvik (anonymisert)", "alder": 45, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-24", "smittekilde_id": None, "lokasjon": "Høvik, Bærum", "institusjon": None, "status": "bekreftet"},
            {"navn": "Pasient 4 – Fornebu (anonymisert)", "alder": 5, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": "2026-06-24", "smittekilde_id": None, "lokasjon": "Fornebu, Bærum", "institusjon": "Fornebu barnehage", "status": "bekreftet"},
            {"navn": "Pasient 5 – Fornebu (anonymisert)", "alder": 72, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": "2026-06-24", "smittekilde_id": None, "lokasjon": "Fornebu, Bærum", "institusjon": None, "status": "mistenkt"},
            {"navn": "Pasient 6 – Høvik (anonymisert)", "alder": 38, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": "2026-06-25", "smittekilde_id": None, "lokasjon": "Høvik, Bærum", "institusjon": None, "status": "mistenkt"},
        ],
    },
    {
        "id": "legionella_bad",
        "navn": "🚿 Legionella – Bærum bad, Sandvika",
        "lat": 59.8910, "lon": 10.5248,
        "beskrivelse": (
            "7 tilfeller av legionellapneumoni, alle med besøk til Bærum bad siste 2 uker. "
            "2 pasienter innlagt intensivavdeling Bærum sykehus. Badesenteret stengt umiddelbart. "
            "Vannprøver fra boblebad og dusjsystemer tatt. FHI bistår med etterforskning."
        ),
        "hendelse": {
            "type_id": "smitteutbrudd",
            "tittel": "Legionellaklynge – 7 tilfeller tilknyttet Bærum bad",
            "beskrivelse": "7 pneumonitilfeller med Legionella pneumophila. Felles eksponering: Bærum bad. 2 intensivinnlagt.",
            "lokasjon": "Bærum bad, Rådhusveien 4, Sandvika",
            "alvorlighetsgrad": "kritisk",
        },
        "logg": [
            {"type": "varsling", "tittel": "Bærum sykehus varsler – Legionella-klynge", "tekst": "Infeksjonsavdelingen melder 3 pneumonipasienter med Legionella pneumophila serogruppe 1 på 6 dager. Alle bosatt i Bærum. Kommuneoverlegen kontaktes kl. 14:30.", "bruker": "Bærum sykehus", "offset_min": -720},
            {"type": "tiltak", "tittel": "Bærum bad stengt umiddelbart", "tekst": "Kommuneoverlege beslutter stenging av Bærum bad kl. 15:00 etter konferanse med FHI. Alle gjester og ansatte informeres. Skiltting på plass. Bookinger avlyses.", "bruker": "Kommuneoverlege", "offset_min": -680},
            {"type": "tiltak", "tittel": "Vannprøver tatt – boblebad, dusjer, kjøletårn", "tekst": "VVS-ekspert og Mattilsynet tar vannprøver fra alle vannkilder: boblebad (3 stk), varmebasseng, dusjer (12 stk) og luftkjølingsanlegg på taket. Svar forventet 2–3 virkedager.", "bruker": "Mattilsynet", "offset_min": -640},
            {"type": "varsling", "tittel": "FHI varslet – Legionella-etterforskning", "tekst": "FHI opprettet MSIS-sak. Legionella pneumophila er meldepliktig (gruppe A). FHI smittevernekspert flyr til Bærum for bistand. Nasjonalt referanselaboratorium typifiserer stammer for å bekrefte felles kilde.", "bruker": "Kommuneoverlege", "offset_min": -600},
            {"type": "observasjon", "tittel": "4 nye tilfeller identifisert – total 7", "tekst": "Systematisk gjennomgang av sykehusinnleggelser siste 14 dager avdekker ytterligere 4 pneumonipasienter. Alle intervjues om eksponeringshistorikk. 6 av 7 bekrefter besøk Bærum bad siste 10 dager.", "bruker": "Kommuneoverlege", "offset_min": -480},
            {"type": "varsling", "tittel": "Statsforvalter varslet – alvorlig folkehelsehendelse", "tekst": "Statsforvalter Oslo og Viken varslet. 2 intensivinnleggelser gjør dette til en alvorlig hendelse. Statsforvalter støtter stenging og er klar for å bistå med ekstra ressurser.", "bruker": "Beredskapskoordinator", "offset_min": -420},
            {"type": "observasjon", "tittel": "Boblebad nr. 2 – høy Legionella-titer", "tekst": "Foreløpig svar fra Mattilsynet: vannprøve fra boblebad nr. 2 viser Legionella >10 000 CFU/L (normalgrense <100). Sannsynlig kilde identifisert. Temperaturlogg viste 30°C – optimalt for Legionella-vekst.", "bruker": "Mattilsynet", "offset_min": -240},
            {"type": "beslutning", "tittel": "Termisk desinfeksjon og full renovering boblebad", "tekst": "Kommuneoverlege beslutter termisk desinfeksjon (70°C) av hele anlegget og full renovering av boblebadsystem. Bærum bad forblir stengt minimum 3 uker. Teknisk ansvarlig er igangsatt.", "bruker": "Kommuneoverlege", "offset_min": -120},
            {"type": "tiltak", "tittel": "Innbyggerinformasjon – hvem bør oppsøke lege", "tekst": "Pressemelding og nettartikkel publisert. Alle som har besøkt Bærum bad 10.–24. juni og har feber og/eller hoste bes kontakte fastlege eller legevakt. Telefonnummer for spørsmål opprettet.", "bruker": "Informasjonsansvarlig", "offset_min": -60},
        ],
        "smitte": [
            {"navn": "Pasient 1 (indeks)", "alder": 67, "kjønn": "Mann", "prøvedato": "2026-06-18", "symptomstart": "2026-06-15", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": "Bærum bad", "status": "bekreftet"},
            {"navn": "Pasient 2", "alder": 72, "kjønn": "Kvinne", "prøvedato": "2026-06-19", "symptomstart": "2026-06-16", "smittekilde_id": None, "lokasjon": "Høvik", "institusjon": "Bærum bad", "status": "bekreftet"},
            {"navn": "Pasient 3 (intensiv)", "alder": 58, "kjønn": "Mann", "prøvedato": "2026-06-20", "symptomstart": "2026-06-17", "smittekilde_id": None, "lokasjon": "Bekkestua", "institusjon": "Bærum bad", "status": "bekreftet"},
            {"navn": "Pasient 4 (intensiv)", "alder": 81, "kjønn": "Kvinne", "prøvedato": "2026-06-21", "symptomstart": "2026-06-18", "smittekilde_id": None, "lokasjon": "Gjettum", "institusjon": "Bærum bad", "status": "bekreftet"},
            {"navn": "Pasient 5", "alder": 64, "kjønn": "Mann", "prøvedato": "2026-06-22", "symptomstart": "2026-06-19", "smittekilde_id": None, "lokasjon": "Rykkinn", "institusjon": "Bærum bad", "status": "bekreftet"},
            {"navn": "Pasient 6", "alder": 55, "kjønn": "Kvinne", "prøvedato": "2026-06-23", "symptomstart": "2026-06-20", "smittekilde_id": None, "lokasjon": "Fornebu", "institusjon": "Bærum bad", "status": "bekreftet"},
            {"navn": "Pasient 7", "alder": 45, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": "2026-06-21", "smittekilde_id": None, "lokasjon": "Sandvika", "institusjon": "Bærum bad", "status": "bekreftet"},
            {"navn": "Meldt med symptomer – avventer prøvesvar", "alder": 49, "kjønn": "Kvinne", "prøvedato": "2026-06-25", "symptomstart": "2026-06-23", "smittekilde_id": None, "lokasjon": "Bekkestua", "institusjon": "Bærum bad", "status": "mistenkt"},
            {"navn": "Meldt med symptomer – avventer prøvesvar", "alder": 70, "kjønn": "Mann", "prøvedato": "2026-06-25", "symptomstart": "2026-06-23", "smittekilde_id": None, "lokasjon": "Høvik", "institusjon": "Bærum bad", "status": "mistenkt"},
        ],
    },
    {
        "id": "tuberkulose_mottak",
        "navn": "🫁 Tuberkulose – asylmottak Fornebu",
        "lat": 59.9010, "lon": 10.6150,
        "beskrivelse": (
            "Aktiv lungetuberkulose påvist hos 3 beboere ved Fornebu transittmottak. "
            "280 beboere og 45 ansatte eksponert. Systematisk screening (mantoux/IGRA + røntgen) igangsatt. "
            "DOTS-behandling startet. FHI og Statsforvalter varslet."
        ),
        "hendelse": {
            "type_id": "smitteutbrudd",
            "tittel": "Tuberkuloseutbrudd – Fornebu transittmottak (3 aktive + 280 eksponerte)",
            "beskrivelse": "3 bekreftet aktiv TB. 280 beboere og 45 ansatte eksponert. Systematisk screening pågår.",
            "lokasjon": "Fornebu transittmottak, Martin Lingesvei 25, Fornebu",
            "alvorlighetsgrad": "høy",
        },
        "logg": [
            {"type": "varsling", "tittel": "Bærum sykehus melder 3 TB-tilfeller – felles bosted", "tekst": "Lungemedisinsk avdeling varsler kommuneoverlegen om 3 bekreftede tilfeller av smittsom lungetuberkulose med felles bosted på Fornebu transittmottak. TB er meldepliktig gruppe A.", "bruker": "Bærum sykehus", "offset_min": -960},
            {"type": "varsling", "tittel": "FHI varslet – meldepliktig sykdom gruppe A", "tekst": "Tuberkulose meldes til MSIS umiddelbart. FHI smittevernrådgiver kontaktet. FHI anbefaler systematisk screening av alle beboere og ansatte med Mantoux-test og/eller IGRA.", "bruker": "Kommuneoverlege", "offset_min": -900},
            {"type": "beslutning", "tittel": "Screeningplan for 325 eksponerte vedtatt", "tekst": "Kommuneoverlege beslutter i samråd med FHI å screene alle 280 beboere og 45 ansatte. Mantoux-test og IGRA for voksne, BCG-status kontrolleres for barn. Bærum legevakt og Bærum sykehus samarbeider om kapasitet.", "bruker": "Kommuneoverlege", "offset_min": -840},
            {"type": "tiltak", "tittel": "DOTS-behandling startet – 3 indekspasienter", "tekst": "Direkte observert behandling (DOTS) med standard 4-regime (HRZE) startet for alle 3 indekspasienter innlagt Bærum sykehus. Smittsom til behandling har effekt (vanligvis 2–4 uker).", "bruker": "Bærum sykehus", "offset_min": -780},
            {"type": "tiltak", "tittel": "Screeningklinikk etablert på mottaket", "tekst": "Mobil screeningklinikk satt opp på mottaket med bistand fra Bærum legevakt og Helse Sør-Øst. 85 beboere testet dag 1. Positive mantoux-prøver (>15mm) sendes til røntgen.", "bruker": "Bærum legevakt", "offset_min": -720},
            {"type": "varsling", "tittel": "UDI og IMDi varslet om screeningbehov", "tekst": "Utlendingsdirektoratet og IMDi orientert om utbruddet. UDI bistår med tolkehjelp og identifisering av beboere for screening. Helsekort-register gjennomgås.", "bruker": "Beredskapskoordinator", "offset_min": -600},
            {"type": "observasjon", "tittel": "Screening dag 2 – 14 positive mantoux", "tekst": "14 beboere med positiv mantoux-test (>15mm) etter dag 2. Alle sendt til røntgen thorax. 2 viser infiltrat forenlig med aktiv TB. Prøver til dyrkning og resistensbestemmelse tatt.", "bruker": "Kommuneoverlege", "offset_min": -480},
            {"type": "beslutning", "tittel": "Latent TB-behandling tilbys høyrisikoeksponerte", "tekst": "Kommuneoverlege beslutter preventiv INH-behandling (9 mnd) til alle mantoux-positive barn under 5 år og immunsupprimerte voksne i påvente av fullstendig avklaring.", "bruker": "Kommuneoverlege", "offset_min": -240},
            {"type": "observasjon", "tittel": "Resistenstesting – sensitiv TB bekreftet", "tekst": "FHI referanselaboratorium bekrefter: alle 3 stammer er multisensitive (ikke MDR-TB). Standard HRZE-behandling gir godt prognose. Smittesporing utenfor mottaket ikke nødvendig.", "bruker": "FHI", "offset_min": -60},
        ],
        "smitte": [
            {"navn": "Indekspasient 1 (anonymisert)", "alder": 32, "kjønn": "Mann", "prøvedato": "2026-06-10", "symptomstart": "2026-05-20", "smittekilde_id": None, "lokasjon": "Fornebu", "institusjon": "Fornebu transittmottak", "status": "bekreftet"},
            {"navn": "Indekspasient 2 (anonymisert)", "alder": 28, "kjønn": "Mann", "prøvedato": "2026-06-12", "symptomstart": "2026-06-01", "smittekilde_id": 1, "lokasjon": "Fornebu", "institusjon": "Fornebu transittmottak", "status": "bekreftet"},
            {"navn": "Indekspasient 3 (anonymisert)", "alder": 45, "kjønn": "Kvinne", "prøvedato": "2026-06-14", "symptomstart": "2026-06-05", "smittekilde_id": 1, "lokasjon": "Fornebu", "institusjon": "Fornebu transittmottak", "status": "bekreftet"},
            {"navn": "Mantoux-positiv beboer (anonymisert)", "alder": 19, "kjønn": "Mann", "prøvedato": "2026-06-23", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Fornebu", "institusjon": "Fornebu transittmottak", "status": "mistenkt"},
            {"navn": "Mantoux-positiv beboer (anonymisert)", "alder": 35, "kjønn": "Kvinne", "prøvedato": "2026-06-23", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Fornebu", "institusjon": "Fornebu transittmottak", "status": "mistenkt"},
            {"navn": "Eksponert ansatt (anonymisert)", "alder": 41, "kjønn": "Kvinne", "prøvedato": "2026-06-24", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Fornebu", "institusjon": "Fornebu transittmottak", "status": "nærkontakt"},
            {"navn": "Eksponert beboer gruppe 1 (anonymisert)", "alder": 8, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Fornebu", "institusjon": "Fornebu transittmottak", "status": "nærkontakt"},
            {"navn": "Eksponert beboer gruppe 2 (anonymisert)", "alder": 52, "kjønn": "Mann", "prøvedato": "2026-06-24", "symptomstart": None, "smittekilde_id": 2, "lokasjon": "Fornebu", "institusjon": "Fornebu transittmottak", "status": "nærkontakt"},
        ],
    },
    {
        "id": "storulykke_e18",
        "navn": "🚑 Storulykke – E18 Sandvika tunnel (massekasualistikk)",
        "lat": 59.8870, "lon": 10.5100,
        "beskrivelse": (
            "Frontkollisjon mellom buss og vogntog i E18 Sandvika-tunnelen kl. 07:43. "
            "28 skadde, 4 bekreftet omkomne. AMK har erklært masseskade. "
            "Bærum sykehus på rød beredskap. Legevakt åpnet ekstra mottak for lettere skadde. "
            "Tunnelen stengt i begge retninger."
        ),
        "hendelse": {
            "type_id": "storulykke",
            "tittel": "Masseskade E18 Sandvika-tunnelen – 28 skadde, 4 omkomne",
            "beskrivelse": "Frontkollisjon buss/vogntog kl. 07:43. AMK masseskade-erklæring. Bærum sykehus rød beredskap.",
            "lokasjon": "E18 Sandvika-tunnelen, Bærum",
            "alvorlighetsgrad": "kritisk",
        },
        "logg": [
            {"type": "varsling", "tittel": "AMK erklærer masseskade kl. 07:45", "tekst": "AMK Akershus mottar meldinger om frontkollisjon i E18 Sandvika-tunnelen kl. 07:43. Minst 20 skadde meldt. AMK erklærer masseskade og aktiverer katastrofeplanen. 8 ambulanser beordret til stedet.", "bruker": "AMK Akershus", "offset_min": -180},
            {"type": "varsling", "tittel": "Bærum sykehus – rød beredskap aktivert", "tekst": "Bærum sykehus aktiverer rød beredskap kl. 07:52. Elektive operasjoner stanset. Ekstra kirurger og anestesipersonell innkalles. Traumepoliklinikken utvidet. 28 senger klargjøres.", "bruker": "Bærum sykehus", "offset_min": -170},
            {"type": "varsling", "tittel": "Kommuneoverlege og kriseledelse varslet", "tekst": "Kommuneoverlege og kommunedirektør varslet kl. 07:55. Beredskapskoordinator aktiverer kommunal kriseledelse. Møte på rådhuset kl. 09:00.", "bruker": "Beredskapskoordinator", "offset_min": -165},
            {"type": "observasjon", "tittel": "Oppdatert situasjon kl. 08:20 – 4 omkomne bekreftet", "tekst": "Politi bekrefter 4 omkomne på stedet: 3 i bussen, 1 sjåfør vogntog. 28 skadde: 6 kritisk, 9 alvorlig, 13 lettere skadd. Tunnel stengt i begge retninger. E18 totalt blokkert.", "bruker": "Politi – Asker og Bærum", "offset_min": -150},
            {"type": "tiltak", "tittel": "Legevakt – ekstra mottak lettere skadde åpnet", "tekst": "Bærum legevakt åpner ekstra mottaksrom for lettere skadde busspassasjerer. Lege og 4 sykepleiere omdirigert fra normale oppgaver. Psykolog kontaktes for kriseteam.", "bruker": "Bærum legevakt", "offset_min": -140},
            {"type": "tiltak", "tittel": "Pårørendesenter etablert – Sandvika rådhus", "tekst": "Pårørendesenter åpnet på rådhuset kl. 09:00 med bistand fra Røde Kors og kommunalt kriseteam. Telefonnummer annonsert på NRK, baerum.kommune.no og sosiale medier.", "bruker": "Kommunedirektør", "offset_min": -120},
            {"type": "observasjon", "tittel": "Identifisering pågår – bussen var skolerettur", "tekst": "Politiet bekrefter at bussen var en skolerettur fra Valler VGS med 22 elever og 2 lærere om bord. Rektor varslet. Pårørende til elever prioriteres i pårørendesenteret.", "bruker": "Politi – Asker og Bærum", "offset_min": -90},
            {"type": "varsling", "tittel": "Statsforvalter varslet – krise med omkomne", "tekst": "Statsforvalter Oslo og Viken varslet. Krisen klassifiseres som hendelse med omkomne. Statsforvalter tilbyr bistand med krisepsykologer.", "bruker": "Beredskapskoordinator", "offset_min": -60},
            {"type": "tiltak", "tittel": "Kriseteam til Valler VGS", "tekst": "Kommunalt kriseteam og 2 skolepsykologer sendt til Valler VGS for oppfølging av elever og ansatte. Skolen holder en samling kl. 11:00 for alle klasser.", "bruker": "Kommuneoverlege", "offset_min": -30},
            {"type": "møte", "tittel": "Pressekonferanse kl. 11:00 – rådhuset", "tekst": "Felles pressekonferanse med ordfører, kommunedirektør og politiinspektør. Bekrefter 4 omkomne og 28 skadde. Fokus på at pårørendestøtte er på plass og at situasjonen er under kontroll.", "bruker": "Ordfører", "offset_min": -10},
        ],
        "smitte": [],
    },
    {
        "id": "pandemi_start",
        "navn": "🌍 Pandemistart – ukjent respirasjonssykdom",
        "lat": 59.8893, "lon": 10.5214,
        "beskrivelse": (
            "WHO-pandemivarsel aktivert. Ukjent respirasjonssykdom med høy smittsomhet (R0 estimert 3–4) "
            "og alvorlighetsgrad. 14 bekreftede tilfeller i Bærum, eksponering via internasjonal flyrute (Oslo–Dubai). "
            "Kommuneoverlegen aktiverer pandemiplan. Legevakt og sykehjem på høy beredskap."
        ),
        "hendelse": {
            "type_id": "pandemi",
            "tittel": "Pandemistart – ukjent respirasjonssykdom (14 bekreftede i Bærum)",
            "beskrivelse": "WHO-pandemivarsel. R0 3–4. 14 bekreftet via flyrute Oslo–Dubai. Pandemiplan aktivert.",
            "lokasjon": "Bærum kommune – bredt geografisk område",
            "alvorlighetsgrad": "kritisk",
        },
        "logg": [
            {"type": "varsling", "tittel": "WHO pandemivarsel – fase 6", "tekst": "WHO erklærer pandemi kl. 08:00. Ukjent respirasjonsvirus med symptomer likt SARS og høy CFR (tidlig estimat 2–4%). FHI varsler alle norske kommuner. Kommuneoverlegen kontakter beredskapskoordinator.", "bruker": "FHI", "offset_min": -1440},
            {"type": "beslutning", "tittel": "Pandemiplan Bærum aktivert", "tekst": "Kommuneoverlege beslutter å aktivere Bærum kommunes pandemiplan kl. 09:00. Alle beredskapsplaner gjennomgås. Kriseledelse innkalles til møte kl. 10:00 i rådhuset.", "bruker": "Kommuneoverlege", "offset_min": -1380},
            {"type": "varsling", "tittel": "14 bekreftede tilfeller i Bærum – flyrute tilknyttet", "tekst": "FHI bekrefter 14 tilfeller med tilknytning til Oslo–Dubai rute QR178 15. juni. Passasjerliste innhentet. 67 passasjerer fra Bærum på listen. Alle kontaktes for testing og karantene.", "bruker": "FHI", "offset_min": -1200},
            {"type": "tiltak", "tittel": "Sykehjem og omsorgsinstitusjoner – besøksforbud", "tekst": "Kommuneoverlege innfører besøksforbud på alle 7 sykehjem og omsorgsinstitusjoner i Bærum fra kl. 14:00. Ansatte instrueres om smitteverntiltak og symptomovervåking.", "bruker": "Kommuneoverlege", "offset_min": -1140},
            {"type": "tiltak", "tittel": "Testkapasitet skaleres opp – drive-in teststed", "tekst": "Drive-in teststed etablert på Sandvika P-hus fra kl. 16:00. Kapasitet 200 prøver/dag. FHI sender 10 000 tester og PPE (verneutstyr) til Bærum. Legevakt styrket med 5 ekstra leger.", "bruker": "Beredskapskoordinator", "offset_min": -1080},
            {"type": "varsling", "tittel": "Statsforvalter og Helsedirektoratet varslet", "tekst": "Statsforvalter Oslo og Viken varslet. Helsedirektoratets nasjonale kriseledelse orientert. Bærum rapporterer daglig til Statsforvalter. Kapasitetsplaner for ekstra sykehusplasser diskuteres.", "bruker": "Kommunedirektør", "offset_min": -960},
            {"type": "observasjon", "tittel": "R0 estimat økt til 4–5 – raskere spredning enn antatt", "tekst": "FHI oppdaterer R0-estimat til 4–5. Modellering viser 500–1000 nye tilfeller i Bærum innen 14 dager uten tiltak. Kommuneoverlegen vurderer strengere lokale tiltak.", "bruker": "FHI", "offset_min": -720},
            {"type": "beslutning", "tittel": "Lokale smitteverntiltak innført – skoler og barnehager", "tekst": "Kommunedirektør og ordfører beslutter stengning av alle barnehager og grunnskoler i Bærum fra mandag. Videregående skole vurderes. Hjemmekontor anbefales sterkt.", "bruker": "Kommunedirektør", "offset_min": -480},
            {"type": "møte", "tittel": "Daglig situasjonsoppdatering – kriseledelsen", "tekst": "Kriseledelsen møtes daglig kl. 08:00 og 16:00. Situasjonsrapport sendes Statsforvalter og Helsedirektorate kl. 09:00 og 17:00. Pressekonferanse kl. 12:00.", "bruker": "Kommunedirektør", "offset_min": -240},
            {"type": "tiltak", "tittel": "Pandemi-hotline for innbyggere åpnet", "tekst": "Bærum kommune åpner pandemi-hotline 67 50 50 99 fra kl. 08:00–22:00. 12 operatører bemannet. Nettside baerum.kommune.no/pandemi oppdateres fortløpende med råd og informasjon.", "bruker": "Informasjonsansvarlig", "offset_min": -120},
        ],
        "smitte": [
            {"navn": "Flypasient 1 (QR178) – Sandvika", "alder": 45, "kjønn": "Mann", "prøvedato": "2026-06-16", "symptomstart": "2026-06-15", "smittekilde_id": None, "lokasjon": "Sandvika, Bærum", "institusjon": None, "status": "bekreftet"},
            {"navn": "Flypasient 2 (QR178) – Bekkestua", "alder": 38, "kjønn": "Kvinne", "prøvedato": "2026-06-16", "symptomstart": "2026-06-15", "smittekilde_id": None, "lokasjon": "Bekkestua, Bærum", "institusjon": None, "status": "bekreftet"},
            {"navn": "Flypasient 3 (QR178) – Fornebu", "alder": 52, "kjønn": "Mann", "prøvedato": "2026-06-17", "symptomstart": "2026-06-16", "smittekilde_id": None, "lokasjon": "Fornebu, Bærum", "institusjon": None, "status": "bekreftet"},
            {"navn": "Husstandsmedlem av pasient 1", "alder": 42, "kjønn": "Kvinne", "prøvedato": "2026-06-17", "symptomstart": "2026-06-17", "smittekilde_id": 1, "lokasjon": "Sandvika, Bærum", "institusjon": None, "status": "bekreftet"},
            {"navn": "Husstandsmedlem av pasient 1 (barn)", "alder": 11, "kjønn": "Mann", "prøvedato": "2026-06-18", "symptomstart": "2026-06-17", "smittekilde_id": 1, "lokasjon": "Sandvika, Bærum", "institusjon": "Bekkestua barneskole", "status": "bekreftet"},
            {"navn": "Kollega av pasient 2 – arbeidsrelatert smitte", "alder": 36, "kjønn": "Mann", "prøvedato": "2026-06-18", "symptomstart": "2026-06-17", "smittekilde_id": 2, "lokasjon": "Lysaker, Bærum", "institusjon": "Telenor-campus", "status": "bekreftet"},
            {"navn": "Kollega av pasient 2 – arbeidsrelatert smitte", "alder": 29, "kjønn": "Kvinne", "prøvedato": "2026-06-18", "symptomstart": "2026-06-18", "smittekilde_id": 2, "lokasjon": "Lysaker, Bærum", "institusjon": "Telenor-campus", "status": "bekreftet"},
            {"navn": "Husstandsmedlem av pasient 3", "alder": 48, "kjønn": "Mann", "prøvedato": "2026-06-18", "symptomstart": "2026-06-17", "smittekilde_id": 3, "lokasjon": "Fornebu, Bærum", "institusjon": None, "status": "bekreftet"},
            {"navn": "Klassekamerat til pasient 5", "alder": 10, "kjønn": "Kvinne", "prøvedato": "2026-06-19", "symptomstart": "2026-06-18", "smittekilde_id": 5, "lokasjon": "Bekkestua, Bærum", "institusjon": "Bekkestua barneskole", "status": "bekreftet"},
            {"navn": "Karantene – nærkontakt pasient 1 (fly)", "alder": 34, "kjønn": "Kvinne", "prøvedato": "2026-06-19", "symptomstart": None, "smittekilde_id": 1, "lokasjon": "Høvik, Bærum", "institusjon": None, "status": "nærkontakt"},
            {"navn": "Karantene – nærkontakt pasient 2 (fly)", "alder": 55, "kjønn": "Mann", "prøvedato": "2026-06-19", "symptomstart": None, "smittekilde_id": 2, "lokasjon": "Rykkinn, Bærum", "institusjon": None, "status": "nærkontakt"},
            {"navn": "Karantene – nærkontakt pasient 3 (fly)", "alder": 61, "kjønn": "Kvinne", "prøvedato": "2026-06-19", "symptomstart": None, "smittekilde_id": 3, "lokasjon": "Sandvika, Bærum", "institusjon": None, "status": "nærkontakt"},
            {"navn": "Karantene – ansatt Telenor-campus", "alder": 40, "kjønn": "Mann", "prøvedato": "2026-06-20", "symptomstart": None, "smittekilde_id": 6, "lokasjon": "Lysaker, Bærum", "institusjon": "Telenor-campus", "status": "nærkontakt"},
            {"navn": "Karantene – lærer Bekkestua barneskole", "alder": 44, "kjønn": "Kvinne", "prøvedato": "2026-06-20", "symptomstart": None, "smittekilde_id": 5, "lokasjon": "Bekkestua, Bærum", "institusjon": "Bekkestua barneskole", "status": "nærkontakt"},
        ],
    },
]


DEMO_TILTAK = {
    "norovirus_dønski": [
        {"kategori": "testing", "tittel": "Prøvetaking beboere Skogly-avd.", "beskrivelse": "Avføringsprøver fra alle beboere med symptomer sendes Fürst lab.", "ansvarlig": "Bærum legevakt", "status": "fullført"},
        {"kategori": "kohortering", "tittel": "Kohortering Skogly-avdeling", "beskrivelse": "Smittede beboere samlet i egne rom. Personale delt i grupper.", "ansvarlig": "Sykehjemsleder", "status": "pågår"},
        {"kategori": "isolasjon", "tittel": "Isolasjon bekreftet tilfeller", "beskrivelse": "6 bekreftet smittede i isolasjon på enerom med toalett.", "ansvarlig": "Kommuneoverlege", "status": "pågår"},
        {"kategori": "varsling", "tittel": "Pårørendevarsling alle 88 beboere", "beskrivelse": "SMS sendt via Visma til alle registrerte pårørende.", "ansvarlig": "Informasjonsansvarlig", "status": "fullført"},
        {"kategori": "annet", "tittel": "Kantine stengt og desinfisert", "beskrivelse": "Kantinen stengt inntil videre. Nor-Clean desinfiserer.", "ansvarlig": "Beredskapskoordinator", "status": "fullført"},
    ],
    "influensa_bekkestua": [
        {"kategori": "testing", "tittel": "Influensa-PCR 5 elever og 2 lærere", "beskrivelse": "Nasofaryngsprøver sendt Fürst lab for PCR-analyse. Svar forventet 24 timer.", "ansvarlig": "Bærum legevakt", "status": "pågår"},
        {"kategori": "isolasjon", "tittel": "Syke elever sendes hjem umiddelbart", "beskrivelse": "Elever med feber, hoste eller muskelsmerter sendes hjem og holdes hjemme til symptomfri.", "ansvarlig": "Rektor Bekkestua barneskole", "status": "pågår"},
        {"kategori": "varsling", "tittel": "SMS til alle foresatte i 3A, 3B, 4A", "beskrivelse": "Informasjon om utbruddet, symptomer og karanteneregler sendt via Visma InSchool.", "ansvarlig": "Informasjonsansvarlig", "status": "fullført"},
        {"kategori": "annet", "tittel": "Forsterket renhold kontaktflater", "beskrivelse": "Tre daglige rengjøringsrunder av klasserom, toaletter og korridorer.", "ansvarlig": "Renholdstjenesten", "status": "pågår"},
        {"kategori": "annet", "tittel": "Vurdering stenging 3A og 3B", "beskrivelse": "Avventer prøvesvar før beslutning om midlertidig stengning i 3 dager.", "ansvarlig": "Kommuneoverlege", "status": "planlagt"},
    ],
    "meslinger_fornebu": [
        {"kategori": "isolasjon", "tittel": "Isolasjon av indekspasient", "beskrivelse": "Indekspasient isolert på Bærum sykehus. Familie i hjemmekarantene.", "ansvarlig": "Bærum sykehus", "status": "fullført"},
        {"kategori": "testing", "tittel": "SYSVAK-sjekk alle nærkontakter", "beskrivelse": "FHI sjekker vaksinasjonsstatus for alle 180 nærkontakter via SYSVAK.", "ansvarlig": "FHI / Kommuneoverlege", "status": "pågår"},
        {"kategori": "varsling", "tittel": "MMR-vaksinasjonstilbud innen 72 timer", "beskrivelse": "Posteksponeringsimmunisering tilbys alle uvaksinerte nærkontakter under 40 år.", "ansvarlig": "Bærum legevakt", "status": "pågår"},
        {"kategori": "isolasjon", "tittel": "Ekskludering uvaksinerte fra skolen", "beskrivelse": "18 uvaksinerte elever og 2 ansatte ekskludert i 21 dager. Hjemmeopplæring organiseres.", "ansvarlig": "Rektor / Kommuneoverlege", "status": "fullført"},
        {"kategori": "varsling", "tittel": "Informasjon alle 340 foresatte", "beskrivelse": "Brev og SMS til alle foresatte med FHIs meslinginformasjon.", "ansvarlig": "Informasjonsansvarlig", "status": "fullført"},
    ],
    "matforgiftning_sandvika": [
        {"kategori": "annet", "tittel": "Kjøkkenstenging – Mattilsynet", "beskrivelse": "Restaurant Smakens kjøkken stengt etter strakstilsyn. Ingen matservering inntil videre.", "ansvarlig": "Mattilsynet", "status": "fullført"},
        {"kategori": "testing", "tittel": "Matprøver til FHI-laboratoriet", "beskrivelse": "Rekesalat, hollandaise og dessertbuffé analyseres for Staph-enterotoksin.", "ansvarlig": "Mattilsynet", "status": "pågår"},
        {"kategori": "varsling", "tittel": "Kontakt alle 87 gjester fra arrangementet", "beskrivelse": "Alle gjester kontaktes per telefon for symptomregistrering og råd om legekontakt.", "ansvarlig": "Beredskapskoordinator", "status": "pågår"},
        {"kategori": "annet", "tittel": "Matkjedesporing – leverandør reker/egg", "beskrivelse": "Mattilsynet sporer leverandørkjeden bakover for å avdekke smittekilde.", "ansvarlig": "Mattilsynet", "status": "pågår"},
    ],
    "legionella_bad": [
        {"kategori": "annet", "tittel": "Bærum bad stengt – umiddelbar stenging", "beskrivelse": "Bærum bad stengt etter kommuneoverlegens beslutning. Skilting og informasjon til gjester og ansatte.", "ansvarlig": "Kommuneoverlege / Driftsansvarlig", "status": "fullført"},
        {"kategori": "testing", "tittel": "Vannprøver – alle vannkilder i anlegget", "beskrivelse": "Vannprøver fra boblebad (3 stk), varmebasseng, dusjanlegg (12 stk) og kjøletårn tatt av Mattilsynet og VVS-ekspert.", "ansvarlig": "Mattilsynet", "status": "fullført"},
        {"kategori": "varsling", "tittel": "FHI varslet – Legionella gruppe A", "beskrivelse": "Legionella pneumophila meldt til MSIS. FHI smittevernekspert bistår med etterforskning og kildesporing.", "ansvarlig": "Kommuneoverlege", "status": "fullført"},
        {"kategori": "varsling", "tittel": "Innbyggerinformasjon – symptomer og råd", "beskrivelse": "Pressemelding og baerum.kommune.no: besøkende 10.–24. juni med feber/hoste bes kontakte fastlege.", "ansvarlig": "Informasjonsansvarlig", "status": "fullført"},
        {"kategori": "annet", "tittel": "Termisk desinfeksjon – 70°C behandling", "beskrivelse": "Hele VVS-anlegget varmebehandles til 70°C. Boblebad nr. 2 rives og erstattes. Anlegg stengt min. 3 uker.", "ansvarlig": "Teknisk avdeling / Driftsansvarlig", "status": "pågår"},
        {"kategori": "testing", "tittel": "Oppfølging av alle 9 pasienter", "beskrivelse": "Klinisk oppfølging av alle bekreftede pasienter. 2 intensivpasienter prioriteres. Prøvesvar fra referanselaboratoriet avventes.", "ansvarlig": "Bærum sykehus", "status": "pågår"},
    ],
    "tuberkulose_mottak": [
        {"kategori": "testing", "tittel": "Mantoux-test og IGRA – 280 beboere + 45 ansatte", "beskrivelse": "Systematisk screening av alle på mottaket. Dag 1: 85 testet. Positive (>15mm) sendes til røntgen thorax.", "ansvarlig": "Bærum legevakt / Bærum sykehus", "status": "pågår"},
        {"kategori": "isolasjon", "tittel": "DOTS-behandling – 3 indekspasienter", "beskrivelse": "Direkte observert behandling med standard HRZE-regime. Pasienter innlagt Bærum sykehus frem til ikke-smittsomme.", "ansvarlig": "Bærum sykehus", "status": "pågår"},
        {"kategori": "varsling", "tittel": "FHI og MSIS-melding – gruppe A sykdom", "beskrivelse": "TB meldt til MSIS. FHI opprettet sak. FHI-smittevernekspert bistår kommuneoverlegen med screeningplan.", "ansvarlig": "Kommuneoverlege", "status": "fullført"},
        {"kategori": "varsling", "tittel": "UDI og IMDi varslet", "beskrivelse": "UDI bistår med tolkehjelp og identifisering av beboere. Helsekort-register gjennomgås for BCG-dokumentasjon.", "ansvarlig": "Beredskapskoordinator", "status": "fullført"},
        {"kategori": "annet", "tittel": "Preventiv INH-behandling – høyrisikoeksponerte", "beskrivelse": "Profylaktisk isoniazid (INH) 9 mnd tilbys mantoux-positive barn <5 år og immunsupprimerte voksne.", "ansvarlig": "Kommuneoverlege", "status": "planlagt"},
    ],
    "pandemi_start": [
        {"kategori": "isolasjon", "tittel": "Besøksforbud – alle 7 sykehjem i Bærum", "beskrivelse": "Umiddelbart besøksforbud innført på alle sykehjem og omsorgsinstitusjoner. Ansatte instruert om PPE og symptomovervåking.", "ansvarlig": "Kommuneoverlege", "status": "fullført"},
        {"kategori": "testing", "tittel": "Drive-in teststed – Sandvika P-hus", "beskrivelse": "Kapasitet 200 prøver/dag. FHI har levert 10 000 tester og PPE. Bærum legevakt bemanner med 5 ekstra leger.", "ansvarlig": "Beredskapskoordinator", "status": "pågår"},
        {"kategori": "annet", "tittel": "Stengning barnehager og grunnskoler", "beskrivelse": "Alle barnehager og grunnskoler i Bærum stengt fra mandag. Digitalt undervisningsopplegg etableres.", "ansvarlig": "Kommunedirektør", "status": "pågår"},
        {"kategori": "varsling", "tittel": "Pandemi-hotline – 67 50 50 99", "beskrivelse": "Innbyggerhotline åpen 08:00–22:00, 12 operatører. Nettside baerum.kommune.no/pandemi fortløpende oppdatert.", "ansvarlig": "Informasjonsansvarlig", "status": "pågår"},
        {"kategori": "kohortering", "tittel": "Daglig situasjonsrapport til Statsforvalter og FHI", "beskrivelse": "Kriseledelsen møtes kl. 08:00 og 16:00. Rapport sendes kl. 09:00 og 17:00. Pressekonferanse kl. 12:00.", "ansvarlig": "Kommunedirektør", "status": "pågår"},
        {"kategori": "varsling", "tittel": "Smittesporing – 67 Bærum-passasjerer fra QR178", "beskrivelse": "Alle 67 Bærum-passasjerer fra Oslo–Dubai-flyet 15. juni kontaktes for testing og karantene.", "ansvarlig": "Kommuneoverlege / FHI", "status": "pågår"},
    ],
}

DEMO_EKSPONERINGER = {
    "norovirus_dønski": [
        {"sted": "Kantine – Dønski bo- og behandlingssenter", "adresse": "Halvard Birkelandsvei 31, Gjettum", "dato": "2026-06-22", "tidspunkt": "12:00–13:00", "type": "annet", "antall_eksponert": 52, "beskrivelse": "Felles lunsj i kantinen. Mulig smittekilde – matrester undersøkes."},
    ],
    "influensa_bekkestua": [
        {"sted": "Kantine – Bekkestua barneskole", "adresse": "Magnus Smidsrødsvei 1, Bekkestua", "dato": "2026-06-20", "tidspunkt": "11:30–12:30", "type": "skole", "antall_eksponert": 120, "beskrivelse": "Felles lunsjpause fredag. Mulig felles smittekilde – 3A og 3B satt i samme hall."},
    ],
    "matforgiftning_sandvika": [
        {"sted": "Restaurant Smaken – selskapsarrangement", "adresse": "Rådhusgata 14, Sandvika", "dato": "2026-06-21", "tidspunkt": "18:00–23:00", "type": "restaurant", "antall_eksponert": 87, "beskrivelse": "Selskapsarrangement lørdag kveld. 23 av 87 gjester syke. Rekesalat og hollandaisesaus mistenkt."},
    ],
    "legionella_bad": [
        {"sted": "Bærum bad – boblebad nr. 2", "adresse": "Rådhusveien 4, Sandvika", "dato": "2026-06-10", "tidspunkt": "08:00–20:00", "type": "annet", "antall_eksponert": 420, "beskrivelse": "Boblebad nr. 2 identifisert som sannsynlig kilde. Legionella >10 000 CFU/L. Estimert 420 besøkende i perioden 10.–24. juni."},
        {"sted": "Bærum bad – dusjrom herrer", "adresse": "Rådhusveien 4, Sandvika", "dato": "2026-06-10", "tidspunkt": "08:00–20:00", "type": "annet", "antall_eksponert": 380, "beskrivelse": "Dusjrom med gammel rørinstallasjon. Prøver tatt – avventer svar."},
    ],
    "tuberkulose_mottak": [
        {"sted": "Fornebu transittmottak – fellesrom", "adresse": "Martin Lingesvei 25, Fornebu", "dato": "2026-05-01", "tidspunkt": "00:00–23:59", "type": "annet", "antall_eksponert": 280, "beskrivelse": "Beboere eksponert i fellesrom (spisesal, oppholdsrom, felles bad) over lang periode. Indekspasienter smittsomme i 4–6 uker."},
        {"sted": "Fornebu transittmottak – ansatte", "adresse": "Martin Lingesvei 25, Fornebu", "dato": "2026-05-01", "tidspunkt": "07:00–21:00", "type": "arbeidsplass", "antall_eksponert": 45, "beskrivelse": "45 ansatte med nærkontakt med beboere. Særlig vaktpersonell med daglig kontakt risikoutsatt."},
    ],
    "pandemi_start": [
        {"sted": "Fly QR178 – Oslo Gardermoen til Dubai", "adresse": "Oslo Lufthavn, Gardermoen", "dato": "2026-06-15", "tidspunkt": "10:30–18:45", "type": "transport", "antall_eksponert": 312, "beskrivelse": "312 passasjerer på flyet. 67 fra Bærum. Alle kontaktes for testing. Indekspasienter satt i midtseksjon (rad 15–22)."},
        {"sted": "Telenor-campus Fornebu – åpent kontorlandskap", "adresse": "Snarøyveien 30, Fornebu", "dato": "2026-06-16", "tidspunkt": "08:00–17:00", "type": "arbeidsplass", "antall_eksponert": 180, "beskrivelse": "Pasient 2 på jobb 16. juni. Åpent kontorlandskap med 180 ansatte. 2 kolleger bekreftet smittet."},
        {"sted": "Bekkestua barneskole – alle klasser", "adresse": "Magnus Smidsrødsvei 1, Bekkestua", "dato": "2026-06-17", "tidspunkt": "08:15–14:00", "type": "skole", "antall_eksponert": 340, "beskrivelse": "Pasient 5 (barn) på skole 17. juni. 340 elever og 28 ansatte potensielt eksponert. Skolen stengt fra mandag."},
    ],
}


def last_demo_scenario(scenario_id: str):
    """Laster et demo-scenario inn i in-memory state."""
    global aktiv_hendelse, hendelseslogg, smittetilfeller, smitte_tiltak, eksponeringer

    scenario = next((s for s in DEMO_SCENARIOER if s["id"] == scenario_id), None)
    if not scenario:
        return None

    # Sett aktiv hendelse
    ht = next(h for h in HENDELSESTYPER if h["id"] == scenario["hendelse"]["type_id"])
    aktiv_hendelse = {
        "id": 1,
        "type_id": ht["id"],
        "type_navn": ht["navn"],
        "ikon": ht["ikon"],
        "tittel": scenario["hendelse"]["tittel"],
        "beskrivelse": scenario["hendelse"]["beskrivelse"],
        "lokasjon": scenario["hendelse"]["lokasjon"],
        "alvorlighetsgrad": scenario["hendelse"]["alvorlighetsgrad"],
        "opprettet": datetime.now().isoformat(),
        "status": "aktiv",
    }

    # Bygg logg med realistiske tidspunkter
    from datetime import timedelta
    now = datetime.now()
    hendelseslogg = []
    for i, entry in enumerate(scenario["logg"]):
        offset = int(entry.get("offset_min", -i * 15))
        if offset > 0:
            offset = -offset
        tid = (now + timedelta(minutes=offset)).isoformat()
        hendelseslogg.append({
            "id": i + 1,
            "tidspunkt": tid,
            "type": entry["type"],
            "tittel": entry["tittel"],
            "tekst": entry["tekst"],
            "bruker": entry["bruker"],
        })
    hendelseslogg.sort(key=lambda x: x["tidspunkt"], reverse=True)

    # Legg til smittetilfeller
    smittetilfeller = []
    for i, s in enumerate(scenario["smitte"]):
        smittetilfeller.append({
            "id": i + 1,
            "navn": s["navn"],
            "alder": s["alder"],
            "kjønn": s["kjønn"],
            "prøvedato": s["prøvedato"],
            "symptomstart": s.get("symptomstart"),
            "smittekilde_id": s.get("smittekilde_id"),
            "lokasjon": s["lokasjon"],
            "institusjon": s.get("institusjon"),
            "status": s["status"],
            "registrert": datetime.now().isoformat(),
        })

    # Legg til tiltak for relevante scenarioer
    smitte_tiltak = []
    for i, t in enumerate(DEMO_TILTAK.get(scenario_id, [])):
        smitte_tiltak.append({
            "id": i + 1,
            **t,
            "frist": None,
            "opprettet": datetime.now().isoformat(),
        })

    # Legg til eksponeringer for relevante scenarioer
    eksponeringer = []
    for i, e in enumerate(DEMO_EKSPONERINGER.get(scenario_id, [])):
        eksponeringer.append({
            "id": i + 1,
            **e,
            "opprettet": datetime.now().isoformat(),
        })

    return aktiv_hendelse
