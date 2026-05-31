"""For the notes of the type 'My-German-Verb merges the values of 'hilfsverb' and 'partizip_ii' into a single filed 'perfekt'."""

import requests

note_ids = requests.post(
    "http://127.0.0.1:8765",
    json={
        "action": "findNotes",
        "version": 6,
        "params": {"query": "(deck:My-German::My-German-Verbs) AND (Perfekt:)"},
    },
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
    hilfsverb = note["fields"]["Hilfsverb"]["value"]
    partizip_ii = note["fields"]["Partizip II"]["value"]

    perfekt = f"{hilfsverb} + {partizip_ii}"

    requests.post(
        "http://127.0.0.1:8765",
        json={
            "action": "updateNoteFields",
            "version": 6,
            "params": {"note": {"id": note["noteId"], "fields": {"Perfekt": perfekt}}},
        },
        timeout=10,
    )

    total += 1

print(f"The total of {total} notes were updated." if total else "No changes were made.")
