"""
Jasper Wang
A01362031
"""

import dialogue.render_dialogue
import gameplay.character
from gameplay.level import play_level


# TODO: modify character docstrings in different functions according to new stats schemes


# WARNING: sourcing test file for now
def opening_sequence():
    dialogue.render_dialogue.play_dialogues_from_file("assets/dialogues/opening.txt")


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


# TODO: Modify control scheme to WASD instead, change docstrings


# TODO: Modify control scheme to WASD instead, change docstrings


# TODO: modify docstrings


def game():
    MAX_LEVEL = 3
    # HACK: commented out
    opening_sequence()
    character = gameplay.character.make_character()
    for level in range(1, MAX_LEVEL + 1):
        character = play_level(level, character)
        # TODO: What?
        if character == None:
            return


def main():
    game()


if __name__ == '__main__':
    main()
