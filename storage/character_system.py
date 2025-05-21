import json
import os

class CharacterSystem:
    def __init__(self, filepath='characters.json'):
        self.filepath = filepath
        self.characters = self._load_characters()

    def create_character(self, name, attributes, skills=None, items=None):
        if name in self.characters:
            raise ValueError(f"Character with name '{name}' already exists.")
        
        if skills is None:
            skills = []
        if items is None:
            items = []
            
        self.characters[name] = {
            'attributes': attributes,
            'skills': skills,
            'items': items
        }
        self._save_characters()
        return self.characters[name]

    def get_character(self, name):
        return self.characters.get(name)

    def update_character(self, name, updates):
        if name not in self.characters:
            return False  # Or raise an error, depending on desired behavior
        
        character = self.characters[name]
        for key, value in updates.items():
            if key in character:
                if isinstance(character[key], dict) and isinstance(value, dict):
                    character[key].update(value)
                elif isinstance(character[key], list) and isinstance(value, list):
                    character[key].extend(value) # Or replace: character[key] = value
                else:
                    character[key] = value
            else:
                # Optionally, handle new keys if allowed
                character[key] = value 
                
        self._save_characters()
        return True

    def _load_characters(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}  # Return empty dict if file is corrupted or empty
        return {}

    def _save_characters(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.characters, f, indent=4)
