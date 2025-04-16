## Project Structure:

whispnote/
├── app.py                     # Main Streamlit entry point
├── pages/
│   ├── 1_Encrypt_Data.py      # Encrypt & store data
│   ├── 2_Decrypt_Data.py      # Retrieve & decrypt data
│   ├── 3_Login.py             # Reauthorization/Login
├── utils/
│   ├── encryption.py          # Fernet/Hashing utilities
│   ├── auth.py                # Auth logic, hashing, login validation
│   └── data_handler.py        # Read/write JSON, in-memory logic
├── data/
│   └── storage.json           # Data saved in JSON for persistence
├── assets/                    # (Optional) Custom CSS/logo etc.
└── requirements.txt           # Dependencies


whispnote/ ├── app.py # Main Streamlit entry point ├── pages/ │ ├── 1_Encrypt_Data.py # Encrypt & store data │ ├── 2_Decrypt_Data.py # Retrieve & decrypt data │ ├── 3_Login.py # Reauthorization/Login ├── utils/ │ ├── encryption.py # Fernet/Hashing utilities │ ├── auth.py # Auth logic, hashing, login validation │ └── data_handler.py # Read/write JSON, in-memory logic ├── data/ │ └── storage.json # Data saved in JSON for persistence ├── assets/ # (Optional) Custom CSS/logo etc. └── requirements.txt # Dependencies