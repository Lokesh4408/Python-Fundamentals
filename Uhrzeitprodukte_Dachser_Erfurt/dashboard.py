import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time

# --- MOCK DATA GENERATOR (In reality, Olaf provides this) ---
def get_logistics_data():
    data = {
        "Tour": ["T-101", "T-105", "T-202", "T-305"],
        "Customer": ["Bayer GmbH", "Metro Cash & Carry", "DHL Express", "Continental"],
        "Product": ["Speed10", "Speed11", "Speed12", "Speed10"],
        "SLA_Time": ["10:00", "11:00", "12:00", "10:00"],
        "Status": ["Driving", "At Site", "Driving", "Driving"],
        "ETA_Minutes": [8, 0, 25, 45] # Real-time calc based on GPS
    }
    return pd.DataFrame(data)

# --- STATUS LOGIC ---
def apply_color(row):
    # Convert SLA to a datetime object for today
    now = datetime.now()
    sla_h, sla_m = map(int, row['SLA_Time'].split(':'))
    sla_dt = now.replace(hour=sla_h, minute=sla_m, second=0, microsecond=0)
    
    # Calculate Buffer
    arrival_time = now + timedelta(minutes=row['ETA_Minutes'])
    buffer_seconds = (sla_dt - arrival_time).total_seconds()
    buffer_mins = buffer_seconds / 60

    if row['Status'] == "At Site":
        return 'background-color: #28a745; color: white;' # GREEN
    elif buffer_mins < 15:
        return 'background-color: #dc3545; color: white;' # RED
    elif 15 <= buffer_mins <= 30:
        return 'background-color: #ffc107; color: black;' # YELLOW
    else:
        return 'background-color: #ffffff; color: black;' # WHITE/NEUTRAL

# --- GUI LAYOUT ---
st.set_page_config(layout="wide", page_title="Uhrzeit Produkte Monitor")
st.title("🚛 Real-Time Delivery Monitor (Fahrertresen)")

# Auto-refresh every 60 seconds
placeholder = st.empty()

while True:
    df = get_logistics_data()
    
    with placeholder.container():
        # KPI Summary
        col1, col2, col3 = st.columns(3)
        col1.metric("Critical (Red)", len(df[df['ETA_Minutes'] > 30])) # Simplified logic for mock
        col2.metric("On Site", len(df[df['Status'] == "At Site"]))
        col3.metric("Total Tours", len(df))

        # Main Table
        st.subheader("Current Tour Status")
        styled_df = df.style.apply(lambda row: [apply_color(row)] * len(row), axis=1)
        st.table(styled_df)
        
        st.caption(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
    
    time.sleep(60) # Refresh cycle