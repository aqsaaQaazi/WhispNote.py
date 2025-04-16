# Read/write JSON, in-memory logic

# Load/save encrypted data to storage.json

import json
import os

# json data file path;
DATA_FILE = "data/storage.json"


def load_data():
    """Loads user data from the storage.json file into a Python dictionary."""
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            else:
                return {}
    except json.JSONDecodeError:
        return {}

def save_data(data):
    """Saves the current dictionary to the storage.json file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)