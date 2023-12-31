"""
This module contains functions for managing and playing a game level.
"""

import json
import random

from gameplay import character, board, monster
from game_utils import render_text
from game_utils.handle_input import process_users_action


def get_game_level_info(level: int) -> dict or None:
    """
    Retrieves the game level information from a level JSON file.

    :param level: The level number of the game.
    :precondition: The level number must be an integer.
    :postcondition: The level information is retrieved from the JSON file, or None is returned if the file does not exist.
    :return: A dictionary containing the level information.
    >>> level_info_demo = get_game_level_info(9999)  # Non-existent level
    Level 9999 file not found.
    """
    try:
        with open(f"./assets/levels/level{level}.json", "r") as input_object:
            level_info = json.load(input_object)
    except FileNotFoundError:
        print(f"Level {level} file not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding level {level} file.")
        return None

    return level_info


def check_for_monsters():
    """
    Determine whether a foe is present

    :postcondition: determine if a foe is present by comparing equality between 0 with generated random integer
    :return: a Boolean value of True if foe is present, False otherwise
    """
    random_number = random.randint(0, 2)
    return random_number == 0


def generate_monster(monster_list: list) -> dict:
    """
    Generate a random monster from a list of monsters

    :param monster_list: a list of monsters
    :precondition: monster_list must be a list of dictionaries
    :postcondition: generate a random monster from monster_list
    :return: a dictionary representing a monster
    """
    random_number = random.randint(0, len(monster_list) - 1)
    return monster_list[random_number]


def play_level(level: int, game_character: dict) -> dict or None:
    """
    Initialize the game level, returns a game character if the character is alive and the goal is reached, None otherwise

    :param level: the level number of the game
    :param game_character: a game character represented by a dictionary
    :precondition: level must be an integer
    :precondition: game_character must be a game character generated by the make_character() function in this module
    :postcondition: play the game level
    :raises ValueError: if level_info is not a dictionary
    :return: a game character represented by a dictionary if the character is alive and the goal is reached, None otherwise
    """
    level_info = get_game_level_info(level)
    if level_info is None:
        raise ValueError("Invalid input: level_info must be a dictionary")

    rows = level_info["rows"]
    columns = level_info["columns"]
    game_board = board.make_board(level_info)
    monsters = level_info["monsters"]

    game_character["Quest"] = level_info["quest"]
    game_character["X-coordinate"] = 0
    game_character["Y-coordinate"] = 0

    achieved_goal = False

    render_text.print_text_line(level_info.get("entrance_description", ""))

    while character.is_alive(game_character) and not achieved_goal:
        board.render_current_location(game_board, game_character)
        achieved_goal = character.check_if_goal_attained(game_character)
        if achieved_goal:
            return game_character
        direction = process_users_action(game_character)
        if board.validate_move(rows, columns, game_character, direction):
            character.move_character(game_character, direction)
            if check_for_monsters():
                encountered_monster = generate_monster(monsters)
                monster.play_monster_encounter(encountered_monster, game_character)
        else:
            color_flag = "!"
            render_text.print_text_line(f"{color_flag}You cannot go here!")

    return game_character if character.is_alive(game_character) else None
