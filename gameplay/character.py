"""
ADD A DOCSTRING
"""


def make_character():
    """
    Create a character with 5 HP, located at (0, 0) on the board

    :postcondition: create a test_game character
    :return: a dictionary representing a character with their X and Y coordinates, and their health point
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Essence': 5, 'Wisdom': 5}
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


def display_stats(character):
    print(f"Current Quest: {character['Quest']}")
    print("+-------------------+")
    print("|    Player Stats   |")
    print("+-------------------+")
    print(f"| Essence: {character['Essence']}/{character['Max Essence']} |")
    print(f"| Wisdom: {character['Wisdom']}        |")
    print("+-------------------+")
    print("| Actions:          |")
    print("| W - Go North      |")
    print("| A - Go West       |")
    print("| S - Go South      |")
    print("| D - Go East       |")
    print("| ! - See Stats     |")
    print("+-------------------+")


def move_character(character, direction):
    """
    Move character's coordinates according to specified direction

    :param character: a test_game character
    :param direction: an integer between 1 and 4 representing a direction
    :precondition: character is a test_game character generated by the make_character() function in this module
    :precondition: direction is an integer between 1 and 4
    :postcondition: change the character's X or Y coordinate according to direction
    :return: None
    >>> character_demo = {"X-coordinate": 2, "Y-coordinate": 0, "Essence": 3}
    >>> move_character(character_demo, 2)
    >>> character_demo['Y-coordinate'] == 1
    True
    >>> character_demo = {"X-coordinate": 2, "Y-coordinate": 3, "Essence": 3}
    >>> move_character(character_demo, 4)
    >>> character_demo['X-coordinate'] == 1
    True
    """
    direction_map = {
        "W": (0, -1),
        "S": (0, 1),
        "D": (1, 0),
        "A": (-1, 0)
    }
    dx, dy = direction_map[direction]
    character["X-coordinate"] += dx
    character["Y-coordinate"] += dy


def check_if_goal_attained(character):
    # TODO: Implement so that it will check character's Quest property, if "complete" then goal attained
    return character["Quest"] == "Complete"


def is_alive(character):
    return character["Essence"] != 0
