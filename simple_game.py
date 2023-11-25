"""
Jasper Wang
A01362031
"""
import random


def opening_sequence():
    pass


def scenario_descriptions():
    """
    Produce a list of predefined scenario descriptions for the game board

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


def make_board(rows, columns):
    """
    Make a game board with specified numbers of rows and columns with scenarios associated with each coordinates

    :param rows: number of rows on the board
    :param columns: number of columns on the board
    :precondition: rows is a positive integer
    :precondition: columns is a positive integer
    :postcondition: Create a game board based on the inputted rows and columns, and predefined scenarios
    :return: a dictionary with tuples as keys representing coordinates, and strings as values representing scenarios
    """
    if rows < 2 or columns < 2:
        return None

    coordinates = []
    for column in range(columns):
        for row in range(rows):
            coordinates.append((column, row))

    scenarios = scenario_descriptions()
    board = {}
    for coordinate in coordinates:
        board[coordinate] = scenarios[random.randint(0, len(scenarios) - 1)]

    return board


def make_character():
    """
    Create a character with 5 HP, located at (0, 0) on the board

    :postcondition: create a game character
    :return: a dictionary representing a character with their X and Y coordinates, and their health point
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}


def describe_current_location(board, character):
    """
    Describe the current location by printing it on the screen

    :param board: a game board
    :param character: a game character
    :precondition: board is a game board generated by the make_board() function in this module
    :precondition: character is a game character generated by the make_character() function in this module
    :postcondition: a message is printed, no data is modified and no value is returned
    :return: None
    """
    scenario = board[(character["X-coordinate"], character["Y-coordinate"])]
    print(scenario)


def get_user_choice():
    """
    Print a prompt to ask for the direction the user wish to move towards

    :postcondition: print a prompt to ask for user input, no data is modified
    :return: an integer representing the user's inputted direction
    """
    user_direction = input(
        "Where would you like to go? "
        "Enter either 1 for north, 2 for south, 3: east or 4: west: "
    )

    while not (user_direction.isdigit() and int(user_direction) in range(1, 5)):
        print(
            "Invalid entry, please enter either 1 for north, 2 for south, 3: east or 4: west: "
        )
        user_direction = input()

    return int(user_direction)


def validate_move(rows, columns, character, direction):
    """
    Determine whether a move is valid based on whether the move will put the character out of bounds

    :param rows: number of rows on the board
    :param columns: number of columns on the board
    :param character: a game character
    :param direction: a integer between 1 and 4 representing a direction
    :precondition: rows is a positive integer larger or equal to 2
    :precondition: columns is a positive integer larger or equal to 2
    :precondition: character is a character generated by the make_character(), character is alive, goal is not reached
    :precondition: direction is an integer between 1 and 4
    :return: a Boolean value of True if character's move is valid, True if it put character out of bounds
    >>> validate_move(3, 3, {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}, 1)
    False
    >>> validate_move(3, 3, {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}, 2)
    True
    """
    if direction == 1:
        boundary = rows
        coordinate = character["Y-coordinate"] - 1
    elif direction == 2:
        boundary = rows
        coordinate = character["Y-coordinate"] + 1
    elif direction == 3:
        boundary = columns
        coordinate = character["X-coordinate"] + 1
    else:
        boundary = columns
        coordinate = character["X-coordinate"] - 1

    if 0 <= coordinate < boundary:
        return True

    return False


def move_character(character, direction):
    """
    Move character's coordinates according to specified direction

    :param character: a game character
    :param direction: an integer between 1 and 4 representing a direction
    :precondition: character is a game character generated by the make_character() function in this module
    :precondition: direction is an integer between 1 and 4
    :postcondition: change the character's X or Y coordinate according to direction
    :return: None
    >>> character_demo = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}
    >>> move_character(character_demo, 2)
    >>> character_demo['Y-coordinate'] == 1
    True
    >>> character_demo = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 3}
    >>> move_character(character_demo, 4)
    >>> character_demo['X-coordinate'] == 1
    True
    """
    if direction == 1:
        character["Y-coordinate"] -= 1
    elif direction == 2:
        character["Y-coordinate"] += 1
    elif direction == 3:
        character["X-coordinate"] += 1
    else:
        character["X-coordinate"] -= 1


def check_for_foes():
    """
    Determine whether a foe is present

    :postcondition: determine if a foe is present by comparing equality between 0 with generated random integer
    :return: a Boolean value of True if foe is present, False otherwise
    """
    random_number = random.randint(0, 3)
    if random_number == 0:
        return True

    return False


def guessing_game(character):
    """
    Start a game number guessing game where user has to guess the randomly generated number between 1 and 5

    :param character: a game character
    :precondition: character is a game character generated by the make_character() function in this module
    :postcondition: 1 HP is deducted from character if user guesses incorrectly, no data is modified otherwise
    :return: None
    """
    lower = 1
    upper = 5
    secret_number = random.randint(lower, upper)
    guess = input(f"Enter a number between {lower} and {upper} inclusive: ")

    while not (guess.isdigit() and int(guess) in range(1, 6)):
        print(
            f"Invalid entry, please enter a number between {lower} and {upper} inclusive: "
        )
        guess = input()

    if int(guess) == secret_number:
        print("You're right! You can go on with your adventure unscathed!")
    else:
        character["Current HP"] -= 1
        print(
            f"Wrong number! The number was {secret_number} but you entered {guess}, you just lost 1 HP"
        )


def check_if_goal_attained(rows, columns, character):
    """
    Determine whether character has reached the goal coordinate

    :param rows: number of rows on the board
    :param columns: number of columns on the board
    :param character: a game character
    :precondition: rows is a positive integer larger than 2
    :precondition: columns is a positive integer larger than 2
    :precondition: character is a game character generated by the make_character() function, and character is alive
    :postcondition: determine if character has reached the bottom right most coordinate of the board
    :return: a Boolean value of True if character has reached the goal, False otherwise
    >>> check_if_goal_attained(4, 4, {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 3})
    True
    >>> check_if_goal_attained(4, 4, {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 1})
    False
    """
    if (
        character["X-coordinate"] == rows - 1
        and character["Y-coordinate"] == columns - 1
    ):
        return True

    return False


def is_alive(character):
    """
    Check if character is alive

    :param character: a game character
    :precondition: character is a game character generated by the make_character() function in this module
    :return: a Boolean value of True if character's current HP is higher than 0, False otherwise
    >>> character_demo = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}
    >>> is_alive(character_demo)
    True
    >>> character_demo = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 0}
    >>> is_alive(character_demo)
    False
    """
    if character["Current HP"] == 0:
        return False
    return True


def game():
    """
    Initialize the game

    :return: None
    """
    opening_sequence()
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(rows, columns, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                guessing_game(character)
            achieved_goal = check_if_goal_attained(rows, columns, character)
        else:
            print("You cannot go here!")

    if not is_alive(character):
        print("Sorry, you died.")
    else:
        print("Congrats! You reached the end!")


def main():
    game()


if __name__ == "__main__":
    main()
