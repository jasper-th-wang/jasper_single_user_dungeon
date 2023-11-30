# TODO: 3 functions are doing the same thing, consolidate
from gameplay import character

def get_users_choice(number_of_choices):
    """
    Print a prompt to get the desired choice number from user

    :raises ValueError:
    :return: a positive integer representing the user's inputted value
    """
    user_input = int(input("Enter your choice: "))

    if user_input not in range(1, number_of_choices + 1):
        raise ValueError(f"User input has to be between 1 and {number_of_choices}")

    return user_input


def process_users_action(game_character):
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
            character.display_stats(game_character)
        else:
            return user_choice.upper()
