"""
TODO: Circular Calling need fixing
ADD A DOCSTRING
"""
import dialogue.render_dialogue
import interaction.handle_input


def render_options_menu(options_list):
    # NOTE: for display options as multiple choice by print
    option_number = 1

    for option in options_list:
        print(f"{option_number}: {option['option']}")
        option_number += 1


def play_elimination(options_list):
    # find terminating option's index
    # terminating_option_index = 0

    for option in options_list:
        option["terminating"] = False

        if option["option"].startswith("$"):
            # remove the $ mark
            option["option"] = option["option"][1:]
            option["terminating"] = True
            break

        # terminating_option_index += 1

    terminating_option_chosen = False

    # user prompt loop begin
    while not terminating_option_chosen:
        render_options_menu(options_list)
        try:
            user_input = interaction.handle_input.get_users_choice(len(options_list))
        except ValueError:
            print(f"You must enter a number between 1 and {len(options_list)}")
            continue

        chosen_option = options_list[user_input - 1]

        if chosen_option["terminating"]:
            terminating_option_chosen = True

        print("\n")
        dialogue.render_dialogue.render_dialogues(
            {
                "dialogues": options_list[user_input - 1]["dialogues"],
                "properties": {
                    "title": "option",
                },
            }
        )
        options_list.pop(user_input - 1)


def play_multiple_choice(options_list):
    while True:
        render_options_menu(options_list)

        try:
            user_input = interaction.handle_input.get_users_choice(len(options_list))
        except ValueError:
            print(f"You must enter a number between 1 and {len(options_list)}")
            continue

        dialogue.render_dialogue.render_dialogues(
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
