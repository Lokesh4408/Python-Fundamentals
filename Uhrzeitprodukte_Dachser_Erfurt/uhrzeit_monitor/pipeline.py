# pipeline.py  — wires all blocks together
from dataset.test_data   import get_test_auftraege, get_test_reisen
from blocks.block2_GPS import get_fahrzeug_positions
from blocks.block4_SLA import berechne_status, SLAResult

def run_pipeline() -> list[SLAResult]:
    fahrzeuge  = {f["fahrzeug_id"]: f for f in get_fahrzeug_positions()}
    reisen     = {r["tour_nummer"]: r["fahrzeug_id"] for r in get_test_reisen()}
    auftraege  = get_test_auftraege()

    results = []
    for a in auftraege:
        fzg_id = reisen.get(a["tour_nummer"])
        if fzg_id and fzg_id in fahrzeuge:
            results.append(berechne_status(a, fahrzeuge[fzg_id]))
    return results