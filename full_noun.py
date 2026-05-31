"""For the notes of the type My-German-Noun, merges the article and the noun into a single field."""

import requests

note_ids = requests.post(
    "http://127.0.0.1:8765",
    json={"action": "findNotes", "version": 6, "params": {"query": "note:My-German-Noun"}},
    timeout=10,
).json()["result"]

note_info = requests.post(
    "http://127.0.0.1:8765",
    json={"action": "notesInfo", "version": 6, "params": {"notes": note_ids}},
    timeout=10,
).json()["result"]

notes_to_update = (note for note in note_info if not note["fields"]["full_noun"]["value"].strip())

total = 0
for note in notes_to_update:
    genus = note["fields"]["Genus"]["value"]
    deutsch = note["fields"]["Deutsch"]["value"]

    full_noun = f"{genus} {deutsch}" if genus else f"{deutsch}"

    requests.post(
        "http://127.0.0.1:8765",
        json={
            "action": "updateNoteFields",
            "version": 6,
            "params": {"note": {"id": note["noteId"], "fields": {"full_noun": full_noun}}},
        },
        timeout=10,
    )

    total += 1

print(f"full_noun updated for {total} notes." if total else "No notes needed updating.")
