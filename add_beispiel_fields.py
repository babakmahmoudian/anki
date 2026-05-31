import requests
import time

ANKI_CONNECT_URL = "http://localhost:8765"


def add_field(note_type: str, idx: int) -> None:
    for suffix in [f"beispiel_{idx}", f"beispiel_audio_{idx}"]:
        resp = requests.post(
            ANKI_CONNECT_URL,
            json={
                "action": "modelFieldAdd",
                "version": 6,
                "params": {"modelName": note_type, "fieldName": suffix},
            },
            timeout=10,
        )
        result = resp.json()
        if result.get("error"):
            print(f"Error adding {suffix} to {note_type}: {result['error']}")
        else:
            print(f"Added {suffix} to {note_type}")
        time.sleep(0.1)  # Small delay to be safe


# Get all note types
note_types = requests.post(ANKI_CONNECT_URL, json={"action": "modelNames", "version": 6}, timeout=10).json()["result"]

# Add fields
for note_type in note_types:
    for idx in range(6, 11):
        add_field(note_type, idx)
