# data/test_data.py
from datetime import datetime, timezone, timedelta

TODAY = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

def get_test_fahrzeuge():
    """Simulates the GPS feed from Fahrzeuglokalisierung."""
    return [
        {
            "fahrzeug_id": "LKW-001",
            "pen_device_id": "PEN-A1",
            # Parked near Dresden Hauptbahnhof
            "latitude": 51.0404, "longitude": 13.7320,
            "timestamp": datetime.now(timezone.utc),
            "geschwindigkeit_kmh": 0.0
        },
        {
            "fahrzeug_id": "LKW-002",
            "pen_device_id": "PEN-B2",
            # Driving near Leipzig
            "latitude": 51.3397, "longitude": 12.3731,
            "timestamp": datetime.now(timezone.utc),
            "geschwindigkeit_kmh": 52.0
        },
        {
            "fahrzeug_id": "LKW-003",
            "pen_device_id": "PEN-C3",
            # Already on-site at destination (within 200m)
            "latitude": 51.0508, "longitude": 13.7395,
            "timestamp": datetime.now(timezone.utc),
            "geschwindigkeit_kmh": 0.0
        },
    ]

def get_test_reisen():
    """Simulates the Reisen/Tours feed."""
    return [
        {"tour_nummer": "T-001", "fahrzeug_id": "LKW-001",
         "fahrer_name": "Hans Müller", "tour_start": TODAY.replace(hour=6),
         "geplante_stopps": 3},
        {"tour_nummer": "T-002", "fahrzeug_id": "LKW-002",
         "fahrer_name": "Klaus Weber", "tour_start": TODAY.replace(hour=6),
         "geplante_stopps": 4},
        {"tour_nummer": "T-003", "fahrzeug_id": "LKW-003",
         "fahrer_name": "Petra Schmidt", "tour_start": TODAY.replace(hour=6),
         "geplante_stopps": 2},
    ]

def get_test_auftraege():
    """
    Simulates Einzelaufträge. Deadlines are set relative to NOW
    so the color coding is always meaningful during testing.
    """
    now = datetime.now(timezone.utc)
    return [
        {   # RED: deadline in 10 minutes, truck is far away
            "auftrag_id": "AUF-001", "nve_sscc": "340123456789012345",
            "tour_nummer": "T-001", "stopp_sequenz": 1,
            "kunde_name": "Industriepark Dresden GmbH",
            "lieferadresse": "Hamburger Str. 63, 01067 Dresden",
            "ziel_latitude": 51.0600, "ziel_longitude": 13.7200,
            "service_produkt": "Speed10",
            "sla_deadline": now + timedelta(minutes=10),
            "zugestellt_am": None
        },
        {   # YELLOW: deadline in 22 minutes
            "auftrag_id": "AUF-002", "nve_sscc": "340123456789012346",
            "tour_nummer": "T-002", "stopp_sequenz": 1,
            "kunde_name": "Logistik Center Leipzig AG",
            "lieferadresse": "Berliner Str. 12, 04105 Leipzig",
            "ziel_latitude": 51.3380, "ziel_longitude": 12.3850,
            "service_produkt": "Speed11",
            "sla_deadline": now + timedelta(minutes=22),
            "zugestellt_am": None
        },
        {   # GREEN: truck on-site (LKW-003 position ≈ destination)
            "auftrag_id": "AUF-003", "nve_sscc": "340123456789012347",
            "tour_nummer": "T-003", "stopp_sequenz": 1,
            "kunde_name": "Medizintechnik Sachsen KG",
            "lieferadresse": "Prager Str. 10, 01069 Dresden",
            "ziel_latitude": 51.0508, "ziel_longitude": 13.7395,
            "service_produkt": "Speed12",
            "sla_deadline": now + timedelta(minutes=55),
            "zugestellt_am": None
        },
        {   # DELIVERED: already done
            "auftrag_id": "AUF-004", "nve_sscc": "340123456789012348",
            "tour_nummer": "T-001", "stopp_sequenz": 2,
            "kunde_name": "Bäckerei Hoffmann",
            "lieferadresse": "Königsbrücker Str. 5, 01099 Dresden",
            "ziel_latitude": 51.0680, "ziel_longitude": 13.7540,
            "service_produkt": "Speed10",
            "sla_deadline": now - timedelta(minutes=30),
            "zugestellt_am": now - timedelta(minutes=45)
        },
    ]