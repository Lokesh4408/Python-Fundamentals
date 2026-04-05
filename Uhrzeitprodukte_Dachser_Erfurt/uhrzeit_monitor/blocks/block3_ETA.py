# blocks/block3_eta.py
import sys, os
from datetime import datetime, timezone, timedelta
from math import radians, sin, cos, sqrt, atan2

USE_REAL_API = False  # ← flip to True when you have a Maps API key

AVG_SPEED_KMH = 40   # Urban delivery average for stub calculation

def haversine_km(lat1, lon1, lat2, lon2) -> float:
    R = 6371
    phi1, phi2 = radians(lat1), radians(lat2)
    a = (sin((phi2-phi1)/2)**2
         + cos(phi1)*cos(phi2)*sin((radians(lon2-lon1))/2)**2)
    return R * 2 * atan2(sqrt(a), sqrt(1-a))

def get_eta(
    origin_lat: float, origin_lon: float,
    dest_lat: float,   dest_lon: float
) -> tuple[datetime, float]:
    """Returns (eta_datetime, distance_km)."""

    if USE_REAL_API:
        import googlemaps
        gmaps = googlemaps.Client(key=os.environ["GOOGLE_MAPS_KEY"])
        result = gmaps.distance_matrix(  # type: ignore[attr-defined]
            origins=[(origin_lat, origin_lon)],
            destinations=[(dest_lat, dest_lon)],
            mode="driving", departure_time="now"
        )
        el = result["rows"][0]["elements"][0]
        secs = el["duration_in_traffic"]["value"]
        dist_km = el["distance"]["value"] / 1000
        eta = datetime.now(timezone.utc) + timedelta(seconds=secs)
        return eta, dist_km
    else:
        dist_km = haversine_km(origin_lat, origin_lon, dest_lat, dest_lon)
        # Add 25% for road routing vs straight line
        road_km = dist_km * 1.25
        drive_minutes = (road_km / AVG_SPEED_KMH) * 60
        eta = datetime.now(timezone.utc) + timedelta(minutes=drive_minutes)
        return eta, road_km

# ── Standalone test ──────────────────────────────────────────────
if __name__ == "__main__":
    # Dresden Hbf → Prager Str.
    eta, dist = get_eta(51.0404, 13.7320, 51.0508, 13.7395)
    print(f"✅  Block 3 OK — ETA: {eta.strftime('%H:%M')}  Distanz: {dist:.2f} km")