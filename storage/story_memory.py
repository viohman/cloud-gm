import json
import os

class StoryMemory:
    def __init__(self, filepath='story_log.json'):
        self.filepath = filepath
        self.log = self._load_log()

    def add_entry(self, entry_type, content):
        entry = {
            'type': entry_type,
            'content': content,
            'timestamp': self._get_timestamp() 
        }
        self.log.append(entry)
        self._save_log()

    def get_log(self):
        return self.log

    def _load_log(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []  # Return empty list if file is corrupted or empty
        return []

    def _save_log(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.log, f, indent=4)

    def _get_timestamp(self):
        import datetime
        return datetime.datetime.now().isoformat()
