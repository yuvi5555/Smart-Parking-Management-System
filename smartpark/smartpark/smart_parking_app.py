# smart_parking_app.py

import streamlit as st
from users_db import create_user_table, add_user, login_user

st.set_page_config(page_title="Smart Parking Login", layout="centered")
st.title("🚗 Smart Parking System - Login/Register")

# DB setup
create_user_table()

# Session variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Sidebar options
menu = st.selectbox("Choose Option", ["Login", "Register"])

if menu == "Register":
    st.subheader("Create a New Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    if st.button("Register"):
        if add_user(new_user, new_pass):
            st.success("✅ Account created. Please login.")
        else:
            st.error("❌ User already exists.")

elif menu == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.is_admin = True
            st.success("✅ Admin login successful")
            st.switch_page("pages/admin_panel.py")

        elif login_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.is_admin = False
            st.success(f"✅ Welcome {username}")
            st.switch_page("pages/user_dashboard.py")
        else:
            st.error("❌ Invalid credentials")
