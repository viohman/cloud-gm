from agents.game_master import GameMaster
from agents.painter import Painter
from agents.team_members import TeamMember
from storage.story_memory import StoryMemory
from storage.character_system import CharacterSystem
from web_ui import create_app

# Initialize core components
story_memory = StoryMemory()
game_master = GameMaster()
painter = Painter()
character_system = CharacterSystem()

# Initialize NPCs
npc1 = TeamMember(name="Guard Errol")
npc2 = TeamMember(name="Shady Informant")
npcs = [npc1, npc2]

# Create and run the Flask app
app = create_app(story_memory, game_master, painter, character_system, npcs)

if __name__ == '__main__':
    app.run(debug=True)
