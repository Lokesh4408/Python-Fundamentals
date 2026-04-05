# blocks/block2_gps.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

USE_REAL_API = False  # ← flip to True when Olaf's feed is ready

def get_fahrzeug_positions() -> list[dict]:
    if USE_REAL_API:
        # Replace with real HTTP/database call to Fahrzeuglokalisierung
        raise NotImplementedError("Wire up Olaf's GPS endpoint here")
    else:
        from dataset.test_data import get_test_fahrzeuge
        return get_test_fahrzeuge()

# ── Standalone test ──────────────────────────────────────────────
if __name__ == "__main__":
    positions = get_fahrzeug_positions()
    print(f"✅  Block 2 OK — {len(positions)} Fahrzeuge geladen")
    for p in positions:
        print(f"   {p['fahrzeug_id']}  →  {p['latitude']}, {p['longitude']}")