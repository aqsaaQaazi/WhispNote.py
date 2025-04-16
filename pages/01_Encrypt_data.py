# encrypt & store data;

import streamlit as st
from utils.data_handler import load_data, save_data
from utils.auth import hash_passkey
from utils.encryption import encrypt_text

st.title("Encrypt & Store Your private Notes")

# Input fields
username = st.text_input("Enter your username")
text_to_encrypt = st.text_area("Enter text to encrypt")
passkey = st.text_input("Enter a secure passkey", type="password")

if st.button("Encrypt & Save"):
    if not username or not text_to_encrypt or not passkey:
        st.warning("All fields are required.")
    else:
        data = load_data()
        hashed_pass = hash_passkey(passkey)
        encrypted_text = encrypt_text(text_to_encrypt)

        # Store in dictionary
        data[username] = {
            "encrypted_text": encrypted_text,
            "passkey": hashed_pass
        }

        save_data(data)
        st.success("Data encrypted and saved successfully!")
