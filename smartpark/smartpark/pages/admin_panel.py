import streamlit as st
import pandas as pd
from parking_db import (
    create_tables, get_all_vehicles, remove_vehicle_by_slot
)
from io import BytesIO

ADMIN_USER = "admin"
ADMIN_PASS = "admin123"

st.set_page_config(page_title="Admin Panel | Smart Parking", layout="centered")
st.title("🔐 Admin Panel")

create_tables()

admin_user = st.text_input("Admin Username")
admin_pass = st.text_input("Admin Password", type="password")

if st.button("Login"):
    if admin_user == ADMIN_USER and admin_pass == ADMIN_PASS:
        st.success("✅ Access Granted")

        st.subheader("📋 All Parked Vehicles")
        data = get_all_vehicles()
        if data:
            df = pd.DataFrame(data, columns=["ID", "Username", "Plate", "Slot", "Entry", "Exit", "Duration"])
            st.dataframe(df[["Username", "Plate", "Slot", "Entry", "Exit", "Duration"]])

            st.subheader("🛑 Remove Vehicle")
            slots_in_use = df[df["Exit"].isnull()]["Slot"].tolist()
            selected_remove = st.selectbox("Select slot to remove", slots_in_use)
            if st.button("Remove Vehicle"):
                remove_vehicle_by_slot(selected_remove)
                st.success(f"✅ Vehicle from `{selected_remove}` removed.")
                st.rerun()

            st.subheader("📤 Export to Excel")
            output = BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df.to_excel(writer, index=False)
            st.download_button(
                label="Download Excel",
                data=output.getvalue(),
                file_name="parking_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.info("ℹ️ No vehicles parked.")
    else:
        st.error("❌ Invalid Admin Credentials")
