from flask import Flask, render_template
from agents.game_master import GameMaster
from agents.painter import Painter
from agents.team_members import TeamMember
from storage.story_memory import StoryMemory

app = Flask(__name__)

story_memory = StoryMemory()
game_master = GameMaster()
painter = Painter()

# Initialize NPCs
npc1 = TeamMember(name="Guard Errol")
npc2 = TeamMember(name="Shady Informant")
npcs = [npc1, npc2]

@app.route('/')
def index():
    narration_text = game_master.narrate(story_memory)
    image_url = painter.generate_image(narration_text)
    story_memory.add_entry('image', image_url)

    npc_reactions = []
    for npc in npcs:
        reaction = npc.act(narration_text)
        npc_reactions.append(reaction)
        story_memory.add_entry('npc_reaction', reaction) # Log NPC reaction

    return render_template('index.html', 
                           narration_text=narration_text, 
                           image_url=image_url, 
                           npc_reactions=npc_reactions)

if __name__ == '__main__':
    app.run(debug=True)
