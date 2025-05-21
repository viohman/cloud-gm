# Agentic Game Master

## Description
An AI-powered, agent-based game master application designed to run interactive role-playing game sessions. It utilizes separate agents for narration, image generation, NPC interactions, and game system management, based on Warhammer Fantasy RPG 1st Edition rules.

## Current Status
The project is in its initial development phase. Basic UI and placeholder functionalities for core components are being implemented.

## Features (Current & Planned)

**Core Components:**
*   [x] **Narration (Game Master):** Provides story narration (current: placeholder text).
*   [x] **Image Generation (Painter):** Generates scene/character images (current: placeholder images).
*   [x] **Team Members (NPCs):** Agents acting as NPCs (current: placeholder reactions).
*   [x] **Story Storage:** Logs narration, player actions, NPC interactions (current: JSON file).
*   [x] **The System (Character Sheets):** Manages character attributes, skills, items based on WFRP 1st ed. (current: JSON file, basic display).
*   [x] **Backlog:** Tracks ideas and improvements (`BACKLOG.md`).

**User Interface:**
*   [x] Text-based narration display.
*   [x] Image display window.
*   [x] NPC reaction window.
*   [x] Player input window (text + action type dropdown).
*   [x] Map display (current: placeholder image).
*   [x] Character sheet display.
*   [x] Dice rolling interface (d100).
*   [ ] Interactive map.
*   [ ] Advanced character sheet interaction (history/rules queries).

**Planned Enhancements:**
*   Integration with actual AI models for Langchain agents.
*   Deeper WFRP 1st edition rule integration.
*   More sophisticated AI for Game Master, Painter, and NPCs.
*   Database integration for storage.
*   User authentication and multiple campaign support.

## Setup and Running

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows
    # venv\Scripts\activate
    # On macOS/Linux
    # source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install Flask
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```
    The application will typically be available at `http://127.0.0.1:5000/`.

## Project Structure
*   `app.py`: Main Flask application file.
*   `agents/`: Contains the different AI agent modules (GameMaster, Painter, TeamMembers).
*   `storage/`: Handles data persistence (StoryMemory, CharacterSystem).
*   `templates/`: HTML files for the UI.
*   `static/`: CSS and JavaScript files.
*   `BACKLOG.md`: Document for tracking ideas and potential improvements.
*   `story_log.json`: (Generated) Log of game events.
*   `characters.json`: (Generated) Stores character sheet data.
```
