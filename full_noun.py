import requests

# Step 1: Get all notes of your note type
note_ids = requests.post("http://127.0.0.1:8765", json={
    "action": "findNotes",
    "version": 6,
    "params": {"query": "note:My-German-Noun"}
}).json()['result']

# Step 2: Get info for each note
note_info = requests.post("http://127.0.0.1:8765", json={
    "action": "notesInfo",
    "version": 6,
    "params": {"notes": note_ids}
}).json()['result']

# Step 3: Create a generator for notes where FullNoun is empty
notes_to_update = (
    note for note in note_info 
    if not note['fields']['full_noun']['value'].strip()
)

# Step 4: Update only the filtered notes
for note in notes_to_update:
    genus = note['fields']['Genus']['value']
    deutsch = note['fields']['Deutsch']['value']
    
    full_noun = f"{genus} {deutsch}" if genus else f"{deutsch}"

    requests.post("http://127.0.0.1:8765", json={
        "action": "updateNoteFields",
        "version": 6,
        "params": {
            "note": {
                "id": note['noteId'],
                "fields": {"full_noun": full_noun}
            }
        }
    })

print("full_noun updated for all notes where it was empty.")
