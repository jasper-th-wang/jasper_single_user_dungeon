import json

import enviroment.board
from game import process_users_action
from game_state.character import move_character, check_if_goal_attained, is_alive
from interaction.monster_interaction import check_for_monsters, play_monster_encounter
from utils.render_text import print_text_line


def get_game_level_info(level):
    with open(f"./assets/levels/level{level}.json", "r") as input_object:
        level_info = json.load(input_object)

    # pprint(level_info)
    return level_info


def play_game_level(level, character):
    """
    Initialize the test_game

    :return: None
    """
    # helper: read test_game json file:
    level_info = get_game_level_info(level)

    rows = level_info["rows"]
    columns = level_info["columns"]

    board = enviroment.board.make_board(level_info)
    achieved_goal = False

    print_text_line(level_info.get("entrance_description", ""))

    while is_alive(character) and not achieved_goal:
        enviroment.board.render_current_location(board, character)
        direction = process_users_action(character)
        valid_move = enviroment.board.validate_move(rows, columns, character, direction)
        if valid_move:
            move_character(character, direction)
            # display_current_location(board, character)
            there_is_a_challenger = check_for_monsters()
            if there_is_a_challenger:
                play_monster_encounter(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            color_flag = "!"
            print_text_line(f"{color_flag}You cannot go here!")

    if not is_alive(character):
        print("Sorry, you died.")
        return
    else:
        print("Congrats! You reached the end!")
        # TODO: character = STAT BOOST HELPER(character)
        return character
