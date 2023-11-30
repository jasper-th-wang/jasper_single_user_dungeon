# TODO: 3 functions are doing the same thing, consolidate
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
