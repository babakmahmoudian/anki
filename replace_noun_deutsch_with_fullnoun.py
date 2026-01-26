import requests

# Retrieve note IDs
note_ids = requests.post("http://127.0.0.1:8765", json={
    "action": "findNotes",
    "version": 6,
    "params": {"query": '(deck:My-German::My-German-Nouns)'}
}).json()['result']

# Fetch note info
note_info = requests.post("http://127.0.0.1:8765", json={
    "action": "notesInfo",
    "version": 6,
    "params": {"notes": note_ids}
}).json()['result']

print(f"Total of {len(note_info)} notes need revision.")

# Clean up the "Deutsch" field's value
total = 0
for note in note_info:
    # Retrieve the value of 'full_noun' (Article + Noune)
    full_noun = note['fields']['full_noun']['value']
    
    # Update and Save the changes into the DB
    requests.post("http://127.0.0.1:8765", json={
        "action": "updateNoteFields",
        "version": 6,
        "params": {
            "note": {
                "id": note['noteId'],
                "fields": {"Deutsch": full_noun}
            }
        }
    })

    total += 1

print(f"The total of {total} notes were updated." if total else "No changes were made.")
