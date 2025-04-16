import streamlit as st
import time
from utils.data_handler import load_data


# home page & session state logic.

import streamlit as st

# --------------USES_states--------------------

# ✅ Initialize all session keys here
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout" not in st.session_state:
    st.session_state.lockout = False
if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = None



# _____________________________WhispNote_________________________________
# Encrypted notes that vanish like a whisper.


# --------------------Page-Configs------------------------------
st.set_page_config(
    page_icon="🔐",
    page_title="WhispNote | Aqsaa Qaazi",
    layout="centered"
)

st.title("WhispNote")
st.subheader("Encrypted notes that vanish like a whisper.")


# ---------- lockoutLogic-----------------------

if st.session_state["lockout"]:
    elapsed = time.time() - st.session_state['lockout_time']
    if elapsed < 300:
        st.error("You are locked out due to too many failed attempts. Please wait a few minutes.")
        st.stop()
    else:
        # reset
        st.session_state['failed_attempts'] = 0
        st.session_state['lockout_time'] = None

# navigation options...
st.markdown("---")
st.markdown("### Where do you want to go?")
col1, col2 = st.columns(2)

with col1:
    if st.button("Store New Note"):
        st.switch_page("pages/01_Encrypt_data.py")
with col2:
    if st.button("Retrieve My Note"):
        st.switch_page("pages/02_decrypt_data.py")



# Login access 
# (only after failure or log out)
if st.session_state['failed_attempts'] >= 3:
    st.warning("Too many failed attempts. Please reauthorize.")
    if st.button("Reauthorize (Login)"):
        st.switch_page("pages/03_login.py")

# Footer
st.markdown("---")
st.caption("Built for privacy • No database • Your secrets stay in memory")