"""
TODO: Circular Calling need fixing
ADD A DOCSTRING
"""
from dialogue import render_dialogue
from gameplay import handle_input


def render_options_menu(options_list):
    """
    Print an options menu during player options interaction

    :param options_list: a list containing one or more option dictionaries
    :precondition: options_list must not be empty
    :postcondition: an options menu is printed to the screen, no data is modified
    """
    for option_number, option in enumerate(options_list, start=1):
        print(f"{option_number}: {option['option']}")


def play_elimination(options_list):
    """
    Play elimination options interactions where player must choose terminating option to end the interaction

    :param options_list: a list containing one or more option dictionaries
    :precondition: options_list must not be empty
    :postcondition:
    """
    # Initialize terminating condition to False
    terminating_option_chosen = False
    # user prompt loop begin
    while True:
        render_options_menu(options_list)
        user_input = handle_input.get_valid_user_input(len(options_list))
        chosen_option = options_list[user_input - 1]
        if chosen_option["terminating"]:
            break

        render_dialogue.render_dialogues(
            {
                "dialogues": chosen_option["dialogues"],
                "properties": {
                    "title": "option",
                },
            }
        )
        options_list.pop(user_input - 1)


def play_multiple_choice(options_list):
    while True:
        render_options_menu(options_list)
        user_input = handle_input.get_valid_user_input(len(options_list))
        render_dialogue.render_dialogues(
            {
                "dialogues": options_list[user_input - 1]["dialogues"],
                "properties": {
                    "title": "option",
                },
            }
        )
        break


def play_options_interactions(options_list, options_type):
    # options object
    if options_type == "multiple_choice":
        play_multiple_choice(options_list)
        # TODO: Implement stats change after dialogue
    elif options_type == "elimination":
        play_elimination(options_list)
        # TODO: may implement returning stats or wisdom points

    # TODO:
    # if regular / argument is last remaining_option type:
    # return user choice
