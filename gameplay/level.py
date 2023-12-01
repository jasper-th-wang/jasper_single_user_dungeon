import json
import random

from gameplay import character, board, monster, render_text
# TODO: refactor process user action
from gameplay.handle_input import process_users_action


def get_game_level_info(level):
    with open(f"./assets/levels/level{level}.json", "r") as input_object:
        level_info = json.load(input_object)

    # pprint(level_info)
    return level_info


def play_level(level, game_character):
    """
    Initialize the test_game

    :return: None
    """
    # helper: read test_game json file:
    level_info = get_game_level_info(level)

    rows = level_info["rows"]
    columns = level_info["columns"]

    game_board = board.make_board(level_info)
    achieved_goal = False

    render_text.print_text_line(level_info.get("entrance_description", ""))

    while character.is_alive(game_character) and not achieved_goal:
        board.render_current_location(game_board, game_character)
        direction = process_users_action(game_character)
        valid_move = board.validate_move(rows, columns, game_character, direction)
        if valid_move:
            character.move_character(game_character, direction)
            # display_current_location(board, character)
            there_is_a_challenger = check_for_monsters()
            if there_is_a_challenger:
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
    if random_number == 0:
        return True

    return False