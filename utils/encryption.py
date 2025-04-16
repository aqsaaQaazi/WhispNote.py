from cryptography.fernet import Fernet

# Fernet-based encryption & decryption utilities

# Fernet/Hashing utilities

# WARNING: In a real app, never hardcode the key.
# Here, we use a fixed key for simplicity since data is not stored long-term.

FERNET_KEY = Fernet.generate_key()
fernet = Fernet(FERNET_KEY)


def encrypt_text(plain_text: str) -> str:
    """Encrypts a plain text string using Fernet."""
    return fernet.encrypt(plain_text.encode()).decode()

def decrypt_text(encrypted_text: str) -> str:
    """Decrypts a Fernet-encrypted string."""
    return fernet.decrypt(encrypted_text.encode()).decode()