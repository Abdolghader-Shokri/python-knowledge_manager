# services/storage_service.py
import json
import os

FILE_PATH = "data/notes.json"

def ensure_directory():
    if not os.path.exists("data"):
        os.makedirs("data")

def load_notes():
    ensure_directory()
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_notes(notes):
    ensure_directory()
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4)
