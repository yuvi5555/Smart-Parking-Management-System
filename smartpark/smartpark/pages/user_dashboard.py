### pages/user_dashboard.py

import streamlit as st
import os
import pandas as pd
from number_plate_detection import detect_plate
from parking_db import (
    create_tables, add_vehicle, get_all_vehicles, remove_vehicle_by_slot
)
from datetime import datetime

st.set_page_config(page_title="Smart Parking | Dashboard", layout="centered")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login from the main page.")
    st.stop()

create_tables()

username = st.session_state.username
st.title(f"Welcome, {username} 👋")

slots = [f"Slot-{i+1}" for i in range(9)]
existing = get_all_vehicles()
occupied_slots = [r[3] for r in existing]

st.subheader("🅿️ Slot Availability")
cols = st.columns(3)
for i, slot in enumerate(slots):
    col = cols[i % 3]
    if slot in occupied_slots:
        col.button(f"{slot} ❌", disabled=True, key=slot)
    else:
        col.button(f"{slot} ✅", disabled=True, key=slot)

st.subheader("📷 Upload Vehicle Image")

uploaded_file = st.file_uploader("Upload image of vehicle (number plate visible)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    os.makedirs("vehicle_images", exist_ok=True)
    filepath = os.path.join("vehicle_images", uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    plate = detect_plate(filepath)
    if plate:
        st.success(f"✅ Detected Number Plate: `{plate}`")
    else:
        st.warning("⚠️ Number plate not detected properly.")

    if st.button("Book Slot"):
        available = [s for s in slots if s not in occupied_slots]
        if available:
            selected_slot = available[0]
            add_vehicle(username, plate, selected_slot)
            st.success(f"🎉 Slot `{selected_slot}` booked for `{username}` with plate `{plate}`")
            st.rerun()
        else:
            st.error("❌ All slots are occupied")

st.subheader("📋 Current Parked Vehicles")
data = get_all_vehicles()
if data:
    df = pd.DataFrame(data, columns=["ID", "Username", "Plate", "Slot", "Entry", "Exit", "Duration"])
    st.dataframe(df[["Username", "Plate", "Slot", "Entry", "Exit", "Duration"]])
else:
    st.info("🅿️ No vehicles parked yet.")

