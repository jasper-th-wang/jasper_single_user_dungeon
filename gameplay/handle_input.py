# TODO: 3 functions are doing the same thing, consolidate
from gameplay import character
from gameplay.render_text import print_text_line


def get_valid_user_input(number_of_choices=None, valid_characters=None):
    """
    Print a prompt to get the desired choice number from user

    :raises ValueError:
    :return: a positive integer representing the user's inputted value
    """
    while True:
        user_input = input()

        # Check for single digit integer
        if (
                number_of_choices
                and user_input.isdigit()
                and len(user_input) == 1
                and int(user_input) in range(1, number_of_choices + 1)
        ):
            return int(user_input)

        # Check for valid string input
        if valid_characters and user_input in valid_characters:
            return user_input

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


def process_users_action(game_character):
    """
    Print a prompt to ask for the direction the user wish to move towards

    :postcondition: print a prompt to ask for user input, no data is modified
    :return: an integer representing the user's inputted direction
    """
    AVAILABLE_ACTIONS = ["W", "A", "S", "D", "w", "a", "s", "d", "!"]

    while True:
        print(
            "What would you like to do? (Type ! to see stats and available actions.): "
        )
        user_choice = get_valid_user_input(valid_characters=AVAILABLE_ACTIONS)

        # if len(user_choice) != 1 or user_choice not in AVAILABLE_ACTIONS:
        #     print(
        #         f"Invalid entry, please enter one of the following letters or characters: {', '.join('WASD!')}"
        #     )
        #     continue

        if user_choice == "!":
            character.display_stats(game_character)
        else:
            return user_choice.upper()
