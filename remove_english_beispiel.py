"""Removes the english translation from the 'beispiel' field."""

import requests
import re

note_ids = requests.post(
    "http://127.0.0.1:8765",
    json={"action": "findNotes", "version": 6, "params": {"query": "(deck:My-German) AND (Beispiel:<b>*)"}},
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
    beispiel_full = note["fields"]["Beispiel"]["value"]

    # Reformat the value:
    # - Deleting the english translations.
    # - Removing the <b> tag.
    # - Leaving a single <br> between every two examples.
    beispiel_de = "<br>".join(re.findall(pattern="<b>(.*?)</b>", string=beispiel_full))

    requests.post(
        "http://127.0.0.1:8765",
        json={
            "action": "updateNoteFields",
            "version": 6,
            "params": {"note": {"id": note["noteId"], "fields": {"Beispiel": beispiel_de}}},
        },
        timeout=10,
    )

    total += 1

print(f"'Beispiel' values updated for {total} notes." if total else "No changes were made.")
