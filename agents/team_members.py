class TeamMember:
    def __init__(self, name):
        self.name = name

    def act(self, narration_text):
        # Placeholder reaction, narration_text is not used yet
        return f"{self.name} looks around cautiously."

# Example of managing multiple team members (optional)
# team_members = {
# "member1": TeamMember(name="Generic Member 1"),
# "member2": TeamMember(name="Generic Member 2"),
# }
