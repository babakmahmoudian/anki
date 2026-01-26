import requests

# Retrieve note IDs
note_ids = requests.post("http://127.0.0.1:8765", json={
    "action": "findNotes",
    "version": 6,
    "params": {"query": '(deck:My-German::My-German-Verbs) AND (Perfekt:)'}
}).json()['result']

# Fetch note info
note_info = requests.post("http://127.0.0.1:8765", json={
    "action": "notesInfo",
    "version": 6,
    "params": {"notes": note_ids}
}).json()['result']

print(f"Total of {len(note_info)} notes need revision.")

# Fill in the "Perfekt" field's value
total = 0
for note in note_info:
    # Retrieve the Hilfsverb and Partizip II values
    hilfsverb = note['fields']['Hilfsverb']['value']
    partizip_ii = note['fields']['Partizip II']['value']

    # Form the Perfekt value:
    perfekt = f"{hilfsverb} + {partizip_ii}"

    # Save the changes into the DB
    requests.post("http://127.0.0.1:8765", json={
        "action": "updateNoteFields",
        "version": 6,
        "params": {
            "note": {
                "id": note['noteId'],
                "fields": {"Perfekt": perfekt}
            }
        }
    })

    total += 1

print(f"The total of {total} notes were updated." if total else "No changes were made.")
