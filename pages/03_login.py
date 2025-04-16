# Reauthorization/Login

import streamlit as st
from utils.auth import reset_attempts, hash_passkey

st.title("Reauthorize Access")

# Simple in-memory login system (can be extended)
admin_username = "admin"
admin_password_hash = hash_passkey("admin123")  # You can change this!

username = st.text_input("Admin Username")
password = st.text_input("Admin Password", type="password")

if st.button("Login"):
    if username == admin_username and hash_passkey(password) == admin_password_hash:
        reset_attempts()
        st.success("Reauthorization successful. You may now retry decryption.")
        st.info("Return to 'Retrieve & Decrypt' page.")
    else:
        st.error("Invalid credentials.")
