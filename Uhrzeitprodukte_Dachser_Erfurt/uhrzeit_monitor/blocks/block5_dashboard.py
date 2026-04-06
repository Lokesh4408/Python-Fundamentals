# blocks/block5_dashboard.py
import streamlit as st
from datetime import datetime
from pipeline import run_pipeline

st.set_page_config(page_title="Uhrzeit Monitor PoC", layout="wide")

st.markdown("""<style>
.red    {background:#c0392b;color:white;padding:14px;border-radius:8px;
         font-size:1.25rem;font-weight:bold;margin-bottom:8px}
.yellow {background:#f39c12;color:#1a1a1a;padding:14px;border-radius:8px;
         font-size:1.25rem;font-weight:bold;margin-bottom:8px}
.green  {background:#27ae60;color:white;padding:14px;border-radius:8px;
         font-size:1.25rem;font-weight:bold;margin-bottom:8px}
.grey   {background:#7f8c8d;color:white;padding:14px;border-radius:8px;
         font-size:1.25rem;font-weight:bold;margin-bottom:8px}
</style>""", unsafe_allow_html=True)

STYLE = {
    "RED":       ("red",    "🔴 KRITISCH"),
    "YELLOW":    ("yellow", "🟡 ACHTUNG"),
    "GREEN":     ("green",  "🟢 OK"),
    "ON_SITE":   ("green",  "📍 VOR ORT"),
    "DELIVERED": ("grey",   "✅ ZUGESTELLT"),
    "NO_DATA":   ("grey",   "⚪ KEINE DATEN"),
}

SORT_ORDER = {"RED":0,"YELLOW":1,"ON_SITE":2,"GREEN":3,"NO_DATA":4,"DELIVERED":5}

st.title(f"🚛 Uhrzeit Produkte Monitor  |  {datetime.now().strftime('%d.%m.%Y %H:%M')}")
st.caption("PoC — Testdaten  |  Aktualisierung alle 60 Sekunden")
st.divider()

results = sorted(run_pipeline(), key=lambda r: SORT_ORDER.get(r.status, 9))

for r in results:
    css, label = STYLE.get(r.status, STYLE["NO_DATA"])
    buf  = f"Puffer: {r.buffer_minutes:.0f} Min" if r.buffer_minutes is not None else ""
    eta  = r.eta_at_kunde.strftime("%H:%M") if r.eta_at_kunde else "—"
    dead = r.sla_deadline.strftime("%H:%M")
    dist = f"{r.distance_km:.1f} km" if r.distance_km else ""

    st.markdown(f"""
    <div class="{css}">
        {label} &nbsp;|&nbsp; <b>{r.kunde_name}</b> &nbsp;|&nbsp;
        {r.service_produkt} &nbsp;|&nbsp;
        Deadline: {dead} &nbsp;|&nbsp; ETA: {eta} &nbsp;|&nbsp;
        {buf} &nbsp; {dist}
    </div>""", unsafe_allow_html=True)

st.divider()
if st.button("🔄 Manuell aktualisieren"):
    st.rerun()

# Auto-refresh via meta tag
st.markdown('<meta http-equiv="refresh" content="60">', unsafe_allow_html=True)