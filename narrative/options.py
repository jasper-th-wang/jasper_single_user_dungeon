"""
This module provides functions for handling player options during dialogues.

It includes functions for rendering an options menu and playing interactions based on the selected options.
"""
import narrative.dialogue
from game_utils import handle_input


def render_options_menu(options_list: list) -> None:
    """
    Print an options menu during player options interaction

    :param options_list: a list containing one or more option dictionaries
    :precondition: options_list must not be empty
    :postcondition: an options menu is printed to the screen, no data is modified
    :raises ValueError: if options_list is empty
    >>> demo_options_list = [
    ...     {"option": "Option 1", "terminating": False, "dialogues": ["Dialogue line 1"]},
    ...     {"option": "Option 2", "terminating": False, "dialogues": ["Dialogue line 2"]}
    ... ]
    >>> render_options_menu(demo_options_list)
    1: Option 1
    2: Option 2
    """
    if not options_list:
        raise ValueError("Options list must not be empty")

    for option_number, option in enumerate(options_list, start=1):
        print(f"{option_number}: {option['option']}")


def play_options_interactions(
    options_list: list, options_type: str, character: dict
) -> None:
    """
    Play interactions based on the provided options list.

    :param options_list: A list containing one or more option dictionaries.
    :param options_type: A string representing the type of options interaction.
    :param character: A dictionary representing the game character.
    :precondition: options_list should be a non-empty list of option dictionaries.
    :precondition: options_type should be a string that is represents the type of options interaction.
    :precondition: character should be a dictionary that represents the game character.
    :postcondition: The interactions based on the options list are printed and played, and character stats may be modified.
    """
    while True:
        render_options_menu(options_list)
        user_input = handle_input.get_valid_user_input(len(options_list))
        narrative.dialogue.render_dialogues(
            {
                "dialogues": options_list[user_input - 1]["dialogues"],
                "properties": {
                    "title": "option",
                },
            },
            character,
        )
        if options_type == "multiple_choice":
            break
        if options_list[user_input - 1]["terminating"]:
            break
        options_list.pop(user_input - 1)

    # TODO: Implement stats change after dialogue
    # TODO: may implement returning stats or wisdom points
    # TODO:
    # if regular / argument is last remaining_option type:
    # return user choice
