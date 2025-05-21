from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
from agents.game_master import GameMaster
from agents.painter import Painter
from agents.team_members import TeamMember
from storage.story_memory import StoryMemory
from storage.character_system import CharacterSystem

app = Flask(__name__)

story_memory = StoryMemory()
game_master = GameMaster()
painter = Painter()
character_system = CharacterSystem()

# Initialize NPCs
npc1 = TeamMember(name="Guard Errol")
npc2 = TeamMember(name="Shady Informant")
npcs = [npc1, npc2]

@app.route('/')
def index():
    narration_text = game_master.narrate(story_memory)
    image_url = painter.generate_image(narration_text)
    # story_memory.add_entry('image', image_url)

    npc_reactions = []
    for npc in npcs:
        reaction = npc.act(narration_text)
        npc_reactions.append(reaction)
        # story_memory.add_entry('npc_reaction', reaction)

    # Get or create player character
    player_char_name = "Argus_Stonebeard"
    player_character = character_system.get_character(player_char_name)
    if not player_character:
        default_attributes = {'WS': 35, 'BS': 30, 'S': 4, 'T': 3, 'Ag': 30, 'Int': 25, 'WP': 20, 'Fel': 25, 'A': 1, 'W': 10, 'M': 4}
        default_skills = ["Dodge Blow", "Basic Melee Weapons"]
        default_items = ["Hand Weapon (Sword)", "Leather Jerkin"]
        character_system.create_character(player_char_name, default_attributes, default_skills, default_items)
        player_character = character_system.get_character(player_char_name) # Fetch it again

    # For debugging: display story log
    # print(story_memory.get_log())

    map_image_url = 'https://picsum.photos/seed/map/300/200' # Placeholder map URL

    return render_template('index.html', 
                           narration_text=narration_text, 
                           image_url=image_url, 
                           npc_reactions=npc_reactions,
                           player_character=player_character,
                           map_image_url=map_image_url)

@app.route('/player_action', methods=['POST'])
def player_action():
    if request.method == 'POST':
        player_input_text = request.form.get('player_input_text')
        input_type = request.form.get('input_type')

        print(f"Player Input: [{input_type}] {player_input_text}")
        story_memory.add_entry(f'player_{input_type}', player_input_text)
        
        # In a real scenario, this input would trigger new GM narration, NPC reactions, image generation etc.
        # For now, redirecting to index will re-run the existing narration and image generation.
        return redirect(url_for('index'))

@app.route('/roll_dice/<string:dice_type>')
def roll_dice_action(dice_type):
    result = 0
    roll_description = ""
    if dice_type == 'd100':
        result = random.randint(1, 100)
        roll_description = "d100"
    # Add more dice types here later if needed (e.g., '2d6')
    else:
        return jsonify({'error': 'Invalid dice type'}), 400

    # Log the dice roll to story memory
    log_message = f"Dice roll ({roll_description}): {result}"
    story_memory.add_entry('dice_roll', log_message)
    print(log_message) # Also print to server console

    return jsonify({'dice_type': roll_description, 'result': result, 'log_message': log_message})

if __name__ == '__main__':
    app.run(debug=True)
