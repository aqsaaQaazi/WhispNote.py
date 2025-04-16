# Auth logic, hashing, login validation

# Login, hashing, lockout, and validation

import hashlib
import time
import streamlit as st
from utils.data_handler import load_data

def hash_passkey(passkey: str) -> str:
    """Hashes a passkey using SHA-256."""
    return hashlib.sha256(passkey.encode()).hexdigest()

def validate_user(username: str, passkey: str) -> bool:
    """Checks if a username and passkey match the stored hashed value."""
    data = load_data()
    hashed_input = hash_passkey(passkey)

    if username in data:
        stored_hash = data[username]["passkey"]
        return hashed_input == stored_hash
    return False

def handle_failed_attempt():
    """Increments failed attempt counter and triggers lockout if needed."""
    st.session_state['failed_attempts'] += 1
    attempts = st.session_state['failed_attempts']
    
    if attempts >= 3:
        st.session_state['lockout_time'] = time.time()
        st.warning("Too many failed attempts. You’ve been locked out.")
        return False

    st.warning(f"Incorrect passkey. Attempt {attempts}/3.")
    return True

def reset_attempts():
    """Resets failed attempts after successful login."""
    st.session_state['failed_attempts'] = 0
    st.session_state['lockout_time'] = None