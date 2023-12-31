"""
This module contains functions for creating and managing a character in this text-based adventure game.
"""


def make_character() -> dict:
    """
    Creates a new character with default attributes.

    :postcondition: create a new character with default attributes
    :return: a dictionary representing a character. The keys are attributes of the character, and the values are the attributes' values.
    >>> character = make_character()
    >>> character["X-coordinate"]
    0
    >>> character["Y-coordinate"]
    0
    >>> character["Essence"]
    100
    >>> character["Max Essence"]
    100
    >>> character["Wisdom"]
    5
    >>> character["Fury"]
    5
    >>> character["Quest"] is None
    True
    """
    return {
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Essence": 100,
        "Max Essence": 100,
        "Wisdom": 5,
        "Fury": 5,
        "Quest": None,
    }


def display_stats(character: dict) -> None:
    """
    Displays the stats of a character in a formatted manner.

    :param character: a game character
    :precondition: character is a game character generated by the make_character() function in this module
    :postcondition: display the stats of the character in a formatted manner, no data is modified and no value is returned
    >>> character = {'Essence': 10, 'Max Essence': 100, 'Wisdom': 20, 'Fury': 15, 'Quest': 'Find the treasure'}
    >>> display_stats(character)
    Current Quest: Find the treasure
    +-------------------+
    |    Player Stats   |
    +-------------------+
    | Essence: 10/100   |
    | Wisdom: 20        |
    | Fury: 15          |
    +-------------------+
    | Actions:          |
    | W - Go North      |
    | A - Go West       |
    | S - Go South      |
    | D - Go East       |
    | ! - See Stats     |
    +-------------------+
    >>> character = {'Essence': 100, 'Max Essence': 100, 'Wisdom': 30, 'Fury': 150, 'Quest': 'Defeat the dragon'}
    >>> display_stats(character)
    Current Quest: Defeat the dragon
    +-------------------+
    |    Player Stats   |
    +-------------------+
    | Essence: 100/100  |
    | Wisdom: 30        |
    | Fury: 150         |
    +-------------------+
    | Actions:          |
    | W - Go North      |
    | A - Go West       |
    | S - Go South      |
    | D - Go East       |
    | ! - See Stats     |
    +-------------------+
    """
    essence_stats = f"{character['Essence']}/{character['Max Essence']}"
    essence_stats_padding = " " * (9 - len(essence_stats))
    wisdom_stats = f"{character['Wisdom']}"
    wisdom_stats_padding = " " * (10 - len(wisdom_stats))
    fury_stats = f"{character['Fury']}"
    fury_stats_padding = " " * (12 - len(fury_stats))
    print(f"Current Quest: {character['Quest']}")
    print("+-------------------+")
    print("|    Player Stats   |")
    print("+-------------------+")
    print(f"| Essence: {essence_stats}{essence_stats_padding}|")
    print(f"| Wisdom: {wisdom_stats}{wisdom_stats_padding}|")
    print(f"| Fury: {fury_stats}{fury_stats_padding}|")
    print("+-------------------+")
    print("| Actions:          |")
    print("| W - Go North      |")
    print("| A - Go West       |")
    print("| S - Go South      |")
    print("| D - Go East       |")
    print("| ! - See Stats     |")
    print("+-------------------+")


def move_character(character: dict, direction: str) -> None:
    """
    Move character's coordinates according to specified direction

    :param character: a game character
    :param direction: an integer between 1 and 4 representing a direction
    :precondition: character is a game character generated by the make_character() function in this module
    :precondition: direction is a string representing a direction ("W", "S", "D", "A")
    :postcondition: change the character's X or Y coordinate according to direction
    >>> character_demo = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> move_character(character_demo, 'W')
    >>> character_demo
    {'X-coordinate': 0, 'Y-coordinate': -1}
    >>> character_demo = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> move_character(character_demo, 'S')
    >>> character_demo
    {'X-coordinate': 0, 'Y-coordinate': 1}
    >>> character_demo = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> move_character(character_demo, 'D')
    >>> character_demo
    {'X-coordinate': 1, 'Y-coordinate': 0}
    """
    direction_map = {"W": (0, -1), "S": (0, 1), "D": (1, 0), "A": (-1, 0)}
    dx, dy = direction_map[direction]
    character["X-coordinate"] += dx
    character["Y-coordinate"] += dy


def check_if_goal_attained(character):
    """
    Check if the character has reached the end game.

    :param character: a game character
    :precondition: character is a game character generated by the make_character() function in this module
    :postcondition: return True if the character has reached the end game, otherwise return False
    :return: a boolean representing whether the character has reached the end game
    >>> character_demo = {'Quest': 'Completed'}
    >>> check_if_goal_attained(character_demo)
    True
    >>> character_demo = {'Quest': 'Find the treasure'}
    >>> check_if_goal_attained(character_demo)
    False
    """
    return character["Quest"] == "Completed"


def is_alive(character):
    """
    Check if the character is alive.

    :param character: a game character
    :precondition: character is a game character generated by the make_character() function in this module
    :postcondition: return True if the character is alive, otherwise return False
    :return: a boolean representing whether the character is alive
    >>> character_demo = {'Essence': 0}
    >>> is_alive(character_demo)
    False
    >>> character_demo = {'Essence': 100}
    >>> is_alive(character_demo)
    True
    """
    return character["Essence"] != 0
