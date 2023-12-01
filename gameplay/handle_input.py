from gameplay import character


def process_users_action(game_character):
    """
    Process the user's action in the game.

    :param game_character: The game character.
    :postcondition: print a prompt to ask for user input, no data is modified
    :return: an integer representing the user's inputted action.
    """
    AVAILABLE_ACTIONS = "WASD!"

    while True:
        print("What would you like to do? (Type ! to see stats and available actions.)")
        user_choice = get_valid_user_input(valid_characters=AVAILABLE_ACTIONS)

        if user_choice == "!":
            character.display_stats(game_character)
        else:
            return user_choice


def get_valid_user_input(number_of_choices=None, valid_characters=None):
    """
    Get valid user input based on the specified constraints.

    :param number_of_choices: The upper bound of the range for validating integer input.
    :param valid_characters: A string representing the set of valid characters to compare against.
    :return: The valid user input as an integer or uppercase string.
    :raises ValueError: If no choices or valid characters are given for validation.
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
            print(
                f"Invalid entry, please enter a number between 1 and {number_of_choices} inclusive"
            )

        if valid_characters:
            print(
                f"Invalid entry, please enter one of the following letters or characters: {', '.join(valid_characters)}"
            )

        if not (number_of_choices or valid_characters):
            raise ValueError("No choices or valid characters given for validation")


def validate_integer_input(user_input, number_of_choices):
    """
    Validate the user input as a positive integer within the specified range.

    :param user_input: The user input to be validated.
    :param number_of_choices: The upper bound of the range for validation.
    :return: True if the user input is a valid positive integer within the range, False otherwise.
    """
    return (
        number_of_choices
        and user_input.isdigit()
        and 1 <= int(user_input) <= number_of_choices
    )


def validate_character_input(user_input, valid_characters):
    """
    Validate the user input against a set of valid characters.

    :param user_input: The user input to be validated.
    :param valid_characters: A string representing the set of valid characters to compare against.
    :return: True if the user input is in the set of valid characters, False otherwise.
    """
    return valid_characters and user_input.upper() in valid_characters.upper()
