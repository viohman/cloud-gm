class GameMaster:
    def __init__(self):
        pass

    def narrate(self, story_memory):
        placeholder_narration_string = "The adventure begins in a dimly lit tavern..."
        story_memory.add_entry('narration', placeholder_narration_string)
        return placeholder_narration_string
