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


def play_level(level: int, game_character: dict) -> dict or None:
    """
    Initialize the game level
    """
    level_info = get_game_level_info(level)

    rows = level_info["rows"]
    columns = level_info["columns"]

    game_board = board.make_board(level_info)
    achieved_goal = False

    render_text.print_text_line(level_info.get("entrance_description", ""))

    while character.is_alive(game_character) and not achieved_goal:
        board.render_current_location(game_board, game_character)
        direction = process_users_action(game_character)
        if board.validate_move(rows, columns, game_character, direction):
            character.move_character(game_character, direction)
            if check_for_monsters():
                monster.play_monster_encounter(game_character)
            achieved_goal = character.check_if_goal_attained(game_character)
        else:
            color_flag = "!"
            render_text.print_text_line(f"{color_flag}You cannot go here!")

    if not character.is_alive(game_character):
        print("Sorry, you died.")
        return
    else:
        print("Congrats! You reached the end!")
        # TODO: character = STAT BOOST HELPER(character)
        return game_character


def check_for_monsters():
    """
    Determine whether a foe is present

    :postcondition: determine if a foe is present by comparing equality between 0 with generated random integer
    :return: a Boolean value of True if foe is present, False otherwise
    """
    random_number = random.randint(0, 3)
    return random_number == 0
