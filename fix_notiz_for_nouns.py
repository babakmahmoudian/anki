import json
import requests

ANKI_CONNECT_URL = "http://localhost:8765"


def invoke(action, params=None):
    request = json.dumps({"action": action, "version": 6, "params": params or {}})
    return requests.post(ANKI_CONNECT_URL, data=request, timeout=10).json()["result"]


note_ids = invoke("findNotes", {"query": '"note:My-German-Note"'})

updated_count = 0
for note_id in note_ids:
    note = invoke("notesInfo", {"notes": [note_id]})[0]
    current = note["fields"]["notiz"]["value"].strip()

    # Only update if it's a single word (no spaces)
    if current and " " not in current:
        invoke("updateNoteFields", {"note": {"id": note_id, "fields": {"notiz": f"Plural: {current}"}}})
        print(f"Updated: '{current}' -> 'Plural: {current}'")
        updated_count += 1

print(f"Done! Updated {updated_count} notes.")
