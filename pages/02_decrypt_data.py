# Retrieve & decrypt data

import streamlit as st
import time
from utils.data_handler import load_data
from utils.auth import validate_user, handle_failed_attempt, reset_attempts
from utils.encryption import decrypt_text

st.title("Retrieve & Decrypt Your Notes")

# Session state init
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = None

LOCKOUT_DURATION = 60  # seconds

# Lockout check
if st.session_state.lockout_time:
    elapsed = time.time() - st.session_state.lockout_time
    if elapsed < LOCKOUT_DURATION:
        st.warning(f"Locked out for {int(LOCKOUT_DURATION - elapsed)}s due to too many failed attempts.")
        st.stop()
    else:
        # Reset lockout
        reset_attempts()

# Input fields
username = st.text_input("Enter your username")
passkey = st.text_input("Enter your passkey", type="password")

if st.button("Decrypt"):
    data = load_data()

    if username not in data:
        st.error("User not found.")
    elif validate_user(username, passkey):
        encrypted_text = data[username]["encrypted_text"]
        decrypted = decrypt_text(encrypted_text)
        st.success("Decryption successful!")
        st.text_area("Your Note:", decrypted, height=150)
        reset_attempts()
    else:
        still_allowed = handle_failed_attempt()
        if not still_allowed:
            st.switch_page("pages/03_login.py")  # Reauthorization
