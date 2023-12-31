"""
This module contains the main game functions for this text-based adventure game.
"""

import gameplay.character
import narrative.dialogue
from game_utils.render_text import print_text_line
from gameplay.level import play_level


def opening_sequence(level: int, character: dict) -> None:
    """
    Play the opening sequence of the game.

    :param level: an integer
    :param character: a game character represented by a dictionary
    :precondition: level is an integer representing the level of the game
    :precondition: character is a game character generated by the make_character() function in this module
    :postcondition: play the opening sequence, no data is modified and no value is returned
    """
    narrative.dialogue.play_dialogues_from_file_path(
        f"assets/dialogues/level{level}.txt", character
    )


def end_game_message(character: dict or None) -> None:
    """
    Print the end game message based on the character's status

    :param character: a game character represented by a dictionary
    :precondition: character is a game character generated by the make_character() function in this module
    :postcondition: print the end game message, no data is modified and no value is returned
    >>> end_game_message({"Wisdom": 10, "Fury": 5})
    With wisdom as your guide, you have woven a path of insight and harmony through a world of turmoil, leaving a legacy of enlightenment and peace that will echo through ages.
    >>> end_game_message({"Wisdom": 5, "Fury": 10})
    In a world craving balance, your path, fueled by unchecked fury, has left a trail marked by turmoil and conflict, a stark reminder of the cost of unbridled wrath.
    """
    if not character:
        print_text_line(
            "You feel your essence gradually fade away, before you know it, you cease to exist in this realm."
            "\nPlease restart the game to try again."
        )
    elif character["Wisdom"] > character["Fury"]:
        print_text_line(
            "With wisdom as your guide, you have woven a path of insight and harmony through a world of turmoil, "
            "leaving a legacy of enlightenment and peace that will echo through ages."
            "\nThe End."
        )
    else:
        print_text_line(
            "In a world craving balance, your path, fueled by unchecked fury, has left a trail marked by turmoil and "
            "conflict, a stark reminder of the cost of unbridled wrath."
            "\nThe End."
        )


def game():
    character = gameplay.character.make_character()
    for level in range(1, 3):
        opening_sequence(level, character)
        character = play_level(level, character)

        if not character:
            break

    end_game_message(character)


def main():
    game()


if __name__ == "__main__":
    main()
