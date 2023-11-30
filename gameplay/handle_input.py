# TODO: 3 functions are doing the same thing, consolidate
from gameplay import character
from gameplay.render_text import print_text_line


def process_users_action(game_character):
    """
    Print a prompt to ask for the direction the user wish to move towards

    :postcondition: print a prompt to ask for user input, no data is modified
    :return: an integer representing the user's inputted direction
    """
    AVAILABLE_ACTIONS = "WASD!"

    while True:
        print(
            "What would you like to do? (Type ! to see stats and available actions.)"
        )
        user_choice = get_valid_user_input(valid_characters=AVAILABLE_ACTIONS)

        if user_choice == "!":
            character.display_stats(game_character)
        else:
            return user_choice


def get_valid_user_input(number_of_choices=None, valid_characters=None):
    """
    Print a prompt to get the desired choice number from user
    return uppercase

    :raises ValueError:
    :return: a positive integer representing the user's inputted value
    """
    while True:
        user_input = input("Enter here: ")

        # Check for single digit integer
        if validate_integer_input(user_input, number_of_choices):
            return int(user_input)
        elif validate_character_input(user_input, valid_characters):
            # Check for valid string input
            return user_input.upper()

        if number_of_choices:
            print_text_line(
                f"!Invalid entry, please enter a number between 1 and {number_of_choices} inclusive"
            )

        if valid_characters:
            print_text_line(
                f"!Invalid entry, please enter one of the following letters or characters: {', '.join(valid_characters)}"
            )

        if not (number_of_choices or valid_characters):
            raise ValueError("No choices or valid characters given for validation")


def validate_integer_input(user_input, number_of_choices):
    return number_of_choices and user_input.isdigit() and 1 <= int(user_input) <= number_of_choices


def validate_character_input(user_input, valid_characters):
    """
    return uppercase

    :param user_input:
    :param valid_characters:
    :return:
    """
    return valid_characters and user_input.upper() in valid_characters.upper()
