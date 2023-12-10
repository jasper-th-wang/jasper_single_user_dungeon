"""
This module contains functions for managing and playing a monster encounter in the game.
"""

import random

from game_utils import render_text, handle_input

FURY_INCREMENT = 5
WISDOM_INCREMENT = 5
ESSENCE_DECREMENT = 10
KILL_MONSTER_OPTION = "K"


def play_monster_encounter(monster: dict, character: dict) -> None:
    """
    Play the monster encounter, a mini-game where the player has to guess a number to deter the monster.

    :param character: a game character represented by a dictionary
    :param monster: a monster represented by a dictionary
    :precondition: character is a game character generated by the make_character() function in this module
    :precondition: monster is a monster generated by the generate_monster() function in the gameplay/level.py module
    :postcondition: play the monster encounter, no data is modified and no value is returned
    """
    render_text.print_text_line("!>>> !!! ALERT: MONSTER ENCOUNTER !!! <<<")
    render_text.print_text_line(f"!{monster['encounter_message']}")
    monster_name = monster["name"]

    lower = 1
    upper = determine_guess_range_upper_bound(character["Wisdom"])
    secret_number = random.randint(lower, upper)

    print(
        f"Enter a number between {lower} and {upper} inclusive to deter the {monster_name}, or type '{KILL_MONSTER_OPTION}' to kill the {monster_name}"
    )

    guess = handle_input.get_valid_user_input(upper, KILL_MONSTER_OPTION)

    if guess == KILL_MONSTER_OPTION:
        kill_monster(monster_name, character)
        return

    if int(guess) == secret_number:
        deter_monster(monster_name, character)
    else:
        fail_to_deter_monster(monster_name, character)


def determine_guess_range_upper_bound(wisdom_points):
    """
    Determine the upper bound of the range for the player to guess the secret number, based on the player's wisdom points.

    :param wisdom_points: the player's wisdom points
    :precondition: wisdom_points is an integer
    :postcondition: return the upper bound of the range for the player to guess the secret number, no data is modified
    :return: the upper bound of the range for the player to guess the secret number
    >>> determine_guess_range_upper_bound(101)
    1
    >>> determine_guess_range_upper_bound(51)
    2
    """
    if wisdom_points > 30:
        return 1
    elif wisdom_points > 20:
        return 2
    elif wisdom_points > 10:
        return 3
    else:
        return 5


def kill_monster(monster_name: str, character: dict) -> None:
    """
    Kill the monster and gain fury points.

    :param character: a game character
    :param monster_name: the name of the monster
    :precondition: character is a game character generated by the make_character() function in this module
    :precondition: monster_name is a string
    :postcondition: kill the monster and gain fury points, character's fury points is incremented by FURY_INCREMENT
    """
    render_text.print_text_line(
        f"You killed the {monster_name} ruthlessly. Though you are unharmed, you feel an anger inside brewing."
    )
    render_text.print_text_line(f"!You gained {FURY_INCREMENT} Fury")
    character["Fury"] += FURY_INCREMENT


def deter_monster(monster_name: str, character: dict) -> None:
    """
    Deter the monster and gain wisdom points.

    :param character: a game character
    :param monster_name: the name of the monster
    :precondition: character is a game character generated by the make_character() function in this module
    :precondition: monster_name is a string
    :postcondition: deter the monster and gain wisdom points, character's wisdom points is incremented by WISDOM_INCREMENT
    """
    render_text.print_text_line(f"You successfully deterred the {monster_name}!")
    render_text.print_text_line(f"$You gained {WISDOM_INCREMENT} Wisdom!")
    character["Wisdom"] += WISDOM_INCREMENT


def fail_to_deter_monster(monster_name: str, character: dict) -> None:
    """
    Fail to deter the monster and lose essence points.

    :param character: a game character
    :param monster_name: the name of the monster
    :precondition: character is a game character generated by the make_character() function in this module
    :precondition: monster_name is a string
    :postcondition: fail to deter the monster and lose essence points, character's essence points is decremented by ESSENCE_DECREMENT
    """
    character["Essence"] -= ESSENCE_DECREMENT
    render_text.print_text_line(
        f"You failed, the {monster_name} attacked you and ran away."
    )
    render_text.print_text_line(f"!You just lost {ESSENCE_DECREMENT} Essence Point")
