"""
TODO: Make elimination and multiple choice into same function
ADD A DOCSTRING
"""
import narrative.dialogue
from game_utils import handle_input


def render_options_menu(options_list):
    """
    Print an options menu during player options interaction

    :param options_list: a list containing one or more option dictionaries
    :precondition: options_list must not be empty
    :postcondition: an options menu is printed to the screen, no data is modified
    """
    for option_number, option in enumerate(options_list, start=1):
        print(f"{option_number}: {option['option']}")


def play_options_interactions(options_list, options_type):
    while True:
        render_options_menu(options_list)
        user_input = handle_input.get_valid_user_input(len(options_list))
        narrative.dialogue.render_dialogues(
            {
                "dialogues": options_list[user_input - 1]["dialogues"],
                "properties": {
                    "title": "option",
                },
            }
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
