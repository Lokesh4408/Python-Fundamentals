# blocks/block4_sla.py
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from datetime import datetime, timezone
from dataclasses import dataclass
from typing import TypedDict
from blocks.block3_ETA import get_eta, haversine_km

class _Base(TypedDict):
    auftrag_id:      str
    tour_nummer:     str
    kunde_name:      str
    service_produkt: str
    sla_deadline:    datetime
    eta_at_kunde:    datetime | None
    buffer_minutes:  float | None
    distance_km:     float | None

ON_SITE_RADIUS_KM  = 0.2   # 200 metres
BUFFER_RED_MIN     = 15
BUFFER_YELLOW_MIN  = 30

@dataclass
class SLAResult:
    auftrag_id:      str
    tour_nummer:     str
    kunde_name:      str
    service_produkt: str
    sla_deadline:    datetime
    eta_at_kunde:    datetime | None
    buffer_minutes:  float | None
    distance_km:     float | None
    status:          str   # GREEN / YELLOW / RED / DELIVERED / ON_SITE / NO_DATA

def berechne_status(auftrag: dict, fahrzeug: dict) -> SLAResult:
    base = _Base(
        auftrag_id      = str(auftrag["auftrag_id"]),
        tour_nummer     = str(auftrag["tour_nummer"]),
        kunde_name      = str(auftrag["kunde_name"]),
        service_produkt = str(auftrag["service_produkt"]),
        sla_deadline    = auftrag["sla_deadline"],
        eta_at_kunde    = None,
        buffer_minutes  = None,
        distance_km     = None,
    )

    if auftrag["zugestellt_am"] is not None:
        return SLAResult(**base, status="DELIVERED")

    dist_km = haversine_km(
        fahrzeug["latitude"],  fahrzeug["longitude"],
        auftrag["ziel_latitude"], auftrag["ziel_longitude"]
    )

    if dist_km <= ON_SITE_RADIUS_KM:
        base["distance_km"] = dist_km
        base["eta_at_kunde"] = datetime.now(timezone.utc)
        return SLAResult(**base, status="ON_SITE")

    try:
        eta, road_km = get_eta(
            fahrzeug["latitude"],  fahrzeug["longitude"],
            auftrag["ziel_latitude"], auftrag["ziel_longitude"]
        )
    except Exception:
        base["distance_km"] = dist_km
        return SLAResult(**base, status="NO_DATA")

    buffer = (auftrag["sla_deadline"] - eta).total_seconds() / 60

    if buffer < BUFFER_RED_MIN:
        status = "RED"
    elif buffer < BUFFER_YELLOW_MIN:
        status = "YELLOW"
    else:
        status = "GREEN"

    base["eta_at_kunde"]   = eta
    base["buffer_minutes"] = round(buffer, 1)
    base["distance_km"]    = round(road_km, 2)
    return SLAResult(**base, status=status)

# ── Standalone test ──────────────────────────────────────────────
if __name__ == "__main__":
    from dataset.test_data import get_test_auftraege, get_test_fahrzeuge

    auftraege  = get_test_auftraege()
    fahrzeuge  = {f["fahrzeug_id"]: f for f in get_test_fahrzeuge()}
    reisen_map = {"T-001": "LKW-001", "T-002": "LKW-002", "T-003": "LKW-003"}

    print("✅  Block 4 SLA Test Results:")
    print(f"{'ID':<8} {'Kunde':<30} {'Produkt':<8} {'Puffer':>8}  Status")
    print("─" * 70)
    for a in auftraege:
        fzg_id = reisen_map[a["tour_nummer"]]
        r = berechne_status(a, fahrzeuge[fzg_id])
        buf = f"{r.buffer_minutes:.0f} Min" if r.buffer_minutes else "—"
        print(f"{r.auftrag_id:<8} {r.kunde_name:<30} {r.service_produkt:<8}"
              f" {buf:>8}  {r.status}")