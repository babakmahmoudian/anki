"""For the notes of type My-German-Noun replaces the 'deutsch' field value with 'full_noun'."""

import requests

note_ids = requests.post(
    "http://127.0.0.1:8765",
    json={"action": "findNotes", "version": 6, "params": {"query": "(deck:My-German::My-German-Nouns)"}},
    timeout=10,
).json()["result"]

note_info = requests.post(
    "http://127.0.0.1:8765",
    json={"action": "notesInfo", "version": 6, "params": {"notes": note_ids}},
    timeout=10,
).json()["result"]

print(f"Total of {len(note_info)} notes need revision.")

total = 0
for note in note_info:
    full_noun = note["fields"]["full_noun"]["value"]

    requests.post(
        "http://127.0.0.1:8765",
        json={
            "action": "updateNoteFields",
            "version": 6,
            "params": {"note": {"id": note["noteId"], "fields": {"Deutsch": full_noun}}},
        },
        timeout=10,
    )

    total += 1

print(f"The total of {total} notes were updated." if total else "No changes were made.")
