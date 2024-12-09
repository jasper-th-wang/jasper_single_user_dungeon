<div align="center">
<h1 align="center">
<br>JASPER_SINGLE_USER_DUNGEON</h1>
<h3>◦ a Simple Text-Based Adventure Game</h3>
<h3>◦ Developed with Just Plain Old Python.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
</p>
<img src="https://img.shields.io/github/license/jasper-th-wang/jasper_single_user_dungeon?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/jasper-th-wang/jasper_single_user_dungeon?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/jasper-th-wang/jasper_single_user_dungeon?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/jasper-th-wang/jasper_single_user_dungeon?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📂 repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running jasper_single_user_dungeon](#-running-jasper_single_user_dungeon)
  - [🧪 Tests](#-tests)

---

## 📍 Overview

My single user dungeon is a text-based adventure game where players embark on a dungeon quest, engage with dynamic dialogues, and make choices that influence the game's narrative and their character's attributes. With each level, players interact with a detailed ASCII map, face monster encounters, and progress through a story-driven experience. Character stats such as Wisdom and Fury evolve based on player decisions, offering a personalized gaming outcome. Designed for single-player engagement, the game blends rich storytelling and interactivity, emphasizing decision-making in an immersive dungeon environment.

---

## 📂 Repository Structure

```sh
└── jasper_single_user_dungeon/
    ├── deliverables/
    ├── game.py
    ├── game_utils/
    │   ├── handle_input.py
    │   └── render_text.py
    ├── gameplay/
    │   ├── board.py
    │   ├── character.py
    │   ├── constants.py
    │   ├── level.py
    │   └── monster.py
    ├── narrative/
    │   ├── dialogue.py
    │   └── options.py

```

---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [game.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/game.py) | The `game.py` module drives a text-based adventure game with opening sequences and level progression. Dialogues from an external file are played using the `narrative.dialogue` module at each level start, and characters are manipulated and progressed through different levels with `gameplay.character` and `gameplay.level`. The game concludes with a tailored message reflecting the character's attributes, displaying either a positive or negative outcome based on the character's Wisdom and Fury values. The game loop supports multiple levels and ends if the character is not present. |

</details>

<details closed><summary>Game_utils</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [render_text.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/game_utils/render_text.py)   | The `render_text.py` module within the `game_utils` directory of jasper_single_user_dungeon game provides text rendering functionalities. It includes applying color-coded prefixes to player, NPC, and highlighted text, printing text with a typewriter effect, and managing timed delays after displaying text based on word count, ensuring the effect doesn't exceed two seconds. The typewriter effect includes a brief pause after commas and periods for added realism. |
| [handle_input.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/game_utils/handle_input.py) | This `handle_input.py` module manages user interactions for a text-based game, validating and processing player input. It offers a loop to prompt the player, captures their choice, displays character stats on request (!), and reassures input correctness based on integers within range or predefined character sets. Input is treated case-insensitively and validated to match the game's requirements before being accepted.                                            |

</details>

<details closed><summary>Narrative</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [options.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/narrative/options.py)   | The `narrative/options.py` module includes functions for a single-player dungeon game to display and handle player choices within dialogues. It enables printing of a menu with interactive options and executes the interactions, which may result in different dialogues and character stat alterations. The module interacts with `narrative.dialogue` for dialogue rendering and `game_utils.handle_input` for input validation. It supports multiple-choice interactions and can terminate the options loop based on the player's selection.                                                  |
| [dialogue.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/narrative/dialogue.py) | The code is for a text-based adventure game, handling dialogue interaction with a game character. It reads dialogues and options from a file, processes them into a consumable structure, manages character stats changes triggered by dialogue choices, and renders text to the player. It supports character-based dialogue decisions affecting player stats, with an option-handling flow for branching narratives. Core features include file I/O, error handling, dialogue parsing into structured dictionaries, text rendering, and interactive player choices with game state consequences. |

</details>

<details closed><summary>Gameplay</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [board.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/gameplay/board.py)         | The `gameplay/board.py` module in the `jasper_single_user_dungeon` game defines methods for creating and interacting with a game board. It includes creating boards with dimensions and contents based on level info, rendering ASCII maps with player and NPC placements, validating player moves to ensure they stay within the map's boundaries, and handling scenario-specific dialogues when the player's location coincides with an NPC. The board is represented as a dictionary with coordinates as keys. Functions are defined for operations such as board generation, move validation, and scenario description.   |
| [constants.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/gameplay/constants.py) | The `constants.py` module in the `gameplay` directory defines text formatting constants for a game, specifying markers for content beginnings and options, as well as ANSI escape codes for color and style to be used in the game's text-based interface.                                                                                                                                                                                                                                                                                                                                                                    |
| [level.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/gameplay/level.py)         | The `level.py` module, part of a single-user dungeon game, facilitates level management and progression. It includes functions to fetch level data from JSON files (`get_game_level_info`), randomly determine monster encounters (`check_for_monsters`), generate a random monster (`generate_monster`), and orchestrate gameplay for a level (`play_level`). The gameplay function initializes the level, manages character navigation, encounters, and checks for quest completion, updating the character's status and coordinates, and ultimately returns the character's state if they survive and accomplish the goal. |
| [monster.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/gameplay/monster.py)     | The `monster.py` module manages monster encounters in a game, where players guess a number or choose to kill the monster, affecting their stats. A player's wisdom affects their guessing range. Correct guesses deter the monster, increasing wisdom. Incorrect guesses result in essence loss. Killing a monster increases fury. Character stats are modified accordingly. Auxiliary functions render text and handle input.                                                                                                                                                                                                |
| [character.py](https://github.com/jasper-th-wang/jasper_single_user_dungeon/blob/main/gameplay/character.py) | The `character.py` module of a text-based adventure game provides character management functionalities. It allows for creating a new character with default attributes (`make_character`), displaying their stats (`display_stats`), moving them in a specified direction (`move_character`), checking if the end game goal has been attained (`check_if_goal_attained`), and determining if the character is still alive (`is_alive`). Characters have attributes such as coordinates, essence (health), wisdom, fury, and current quest.                                                                                    |

</details>

---

## 🚀 Getting Started

### 🔧 Installation

1. Clone the jasper_single_user_dungeon repository:

```sh
git clone https://github.com/jasper-th-wang/jasper_single_user_dungeon
```

2. Change to the project directory:

```sh
cd jasper_single_user_dungeon
```

### 🤖 Running jasper_single_user_dungeon

```sh
python game.py
```

### 🧪 Tests

```sh
python -m unittest
```

---
