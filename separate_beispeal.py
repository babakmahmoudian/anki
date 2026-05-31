"""Splits up the 'beispiel' field into separate sentences."""

import re
import requests

ANKI_CONNECT_URL = "http://localhost:8765"


def get_notes():
    response = requests.post(
        ANKI_CONNECT_URL,
        json={"action": "findNotes", "version": 6, "params": {"query": "note:My-German-Note"}},
        timeout=10,
    )
    return response.json()["result"]


def get_note_fields(note_id):
    response = requests.post(
        ANKI_CONNECT_URL,
        json={"action": "notesInfo", "version": 6, "params": {"notes": [note_id]}},
        timeout=10,
    )
    return response.json()["result"][0]["fields"]


def update_note_fields(note_id, fields_dict):
    response = requests.post(
        ANKI_CONNECT_URL,
        json={
            "action": "updateNoteFields",
            "version": 6,
            "params": {"note": {"id": note_id, "fields": fields_dict}},
        },
        timeout=10,
    )
    return response.json()


note_ids = get_notes()
print(f"Total of {len(note_ids)} notes to process.")

total_updated = 0

for note_id in note_ids:
    fields = get_note_fields(note_id)
    beispiel_content = fields.get("beispiel", {}).get("value", "")

    if not beispiel_content:
        continue

    examples = re.split(r'<br\s*/?>', beispiel_content, flags=re.IGNORECASE)

    cleaned_examples = []
    for ex in examples:
        cleaned = ex.strip()
        cleaned = re.sub(r'<[^>]+>', '', cleaned)
        if cleaned:
            cleaned_examples.append(cleaned)

    cleaned_examples = cleaned_examples[:10]

    if not cleaned_examples:
        continue

    update_dict = {}
    for idx, example in enumerate(cleaned_examples, start=1):
        update_dict[f"beispiel_{idx}"] = example

    result = update_note_fields(note_id, update_dict)

    if result.get("error") is None:  # Success case
        total_updated += 1
        print(f"Updated note {note_id}: {len(cleaned_examples)} examples")
    else:
        print(f"Error updating note {note_id}: {result['error']}")

print(f"\nThe total of {total_updated} notes were updated." if total_updated else "No changes were made.")
