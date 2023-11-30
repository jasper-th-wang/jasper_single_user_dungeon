"""
Jasper Wang
A01362031
"""

from dialogue.render_dialogue import play_dialogues_from_file
from game_state.character import make_character, display_stats
from game_state.level import play_game_level


# TODO: modify character docstrings in different functions according to new stats schemes


# WARNING: sourcing test file for now
def opening_sequence():
    play_dialogues_from_file("assets/dialogues/opening.txt")


# HACK: mock function
def mock_scenario_descriptions():
    """
    Produce a list of predefined scenario descriptions for the test_game board

    :return: a list containing strings representing scenario descriptions
    """
    return [
        "The Server Room Labyrinth",
        "The Library of Obsolete Languages",
        "The Cafeteria of Constant Cravings",
        "The Printer Paper Jam Dungeon",
        "The WiFi Woods",
        "The Echo Hall of Helpdesk Calls",
        "The Lost USB Mines",
        "The Classroom of Endless Lectures",
        "The Firewall Fortress",
        "The Recursive Room",
    ]


# TODO: add displaying character functionality, change docstring
def process_users_action(character):
    """
    Print a prompt to ask for the direction the user wish to move towards

    :postcondition: print a prompt to ask for user input, no data is modified
    :return: an integer representing the user's inputted direction
    """
    AVAILABLE_ACTIONS = "WASDwasd!"

    while True:
        user_choice = input(
            "What would you like to do? (Type ! to see stats and available actions.): "
        )

        if len(user_choice) != 1 or user_choice not in AVAILABLE_ACTIONS:
            print(
                f"Invalid entry, please enter one of the following letters or characters: {', '.join('WASD!')}"
            )
            continue

        if user_choice == "!":
            display_stats(character)
        else:
            return user_choice.upper()


# TODO: Modify control scheme to WASD instead, change docstrings


# TODO: Modify control scheme to WASD instead, change docstrings


# TODO: modify docstrings


def game():
    MAX_LEVEL = 3
    # HACK: commented out
    opening_sequence()
    character = make_character()
    for level in range(1, MAX_LEVEL + 1):
        character = play_game_level(level, character)
        # TODO: What?
        if character == None:
            return
    pass
