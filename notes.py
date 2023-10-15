import json
import datetime

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

notes = load_notes()

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)
