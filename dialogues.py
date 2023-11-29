# TODO: rename this module to like rendering utils??

from constants import TEXT_FLAGS
from render_text import print_text_line
from utils import get_users_choice


def parse_dialogue_file_properties(property_line_list):
    dialogues_properties = {}
    CONTENT_START_FLAG = TEXT_FLAGS()["CONTENT_START_FLAG"]

    for line in property_line_list:
        line = line.strip()

        if line == CONTENT_START_FLAG:
            break

        yarn_property = line.split(": ")
        dialogues_properties[yarn_property[0]] = yarn_property[1]

    return dialogues_properties


def create_dialogue_lines_and_options_list(dialogue_content):
    dialogue_lines_list = []
    OPTION_FLAG = TEXT_FLAGS()["OPTION_FLAG"]
    options_list = []  # list of options
    options_content = {}

    for line in dialogue_content:
        if line == "\n":
            continue

        line = line.rstrip()

        if OPTION_FLAG in line:
            # store and clear previous options_content dictionary
            if options_content:
                options_list.append(options_content)
                options_content = {}
            # initialize option dictionary
            options_content["option"] = line.replace(OPTION_FLAG, "")
            continue

        if line.startswith((" ", "\t")):
            line = line.strip()
            if "dialogues" in options_content:
                options_content["dialogues"].append(line)
            else:
                options_content["dialogues"] = [line]

            continue

        # on new normal line, check if options related values are stored, if
        # not, store it
        if options_content:
            options_list.append(options_content)
            options_content = {}
            dialogue_lines_list.append(options_list)
            options_list = []

        dialogue_lines_list.append(line)

    # after exhausting list, check if options related values are stored, if
    # not, store it
    if options_content:
        options_list.append(options_content)
        options_content = {}
        dialogue_lines_list.append(options_list)
        options_list = []

    return dialogue_lines_list


def parse_dialogue_file(file_path):
    """
    Read and convert dialogue text files to dialogue dictionary for rendering

    :param file_path: strings representing path to a dialogue file
    :return: a dictionary representing information about a dialogue
    """
    CONTENT_START_FLAG = TEXT_FLAGS()["CONTENT_START_FLAG"]
    try:
        with open(file_path, "r") as dialogues:
            lines = dialogues.readlines()

    except OSError:
        print("No dialogue text file is found")
    else:
        dialogues_properties = parse_dialogue_file_properties(lines)
        index_of_content_start = lines.index(CONTENT_START_FLAG + "\n")

        dialogues_content = lines[index_of_content_start + 1 : -1]
        parsed_dialogues = create_dialogue_lines_and_options_list(dialogues_content)

        return {
            "properties": dialogues_properties,
            "dialogues": parsed_dialogues,
        }


def render_dialogues(parsed_dialogues_dictionary):
    dialogues_properties = parsed_dialogues_dictionary["properties"]
    parsed_dialogues_list = parsed_dialogues_dictionary["dialogues"]
    # for element in lisst
    # if strings -> print
    # if list -> call helper prompt_user_options
    for item in parsed_dialogues_list:
        if isinstance(item, str):
            print_text_line(item)
            continue
        if isinstance(item, list):
            play_options_interactions(item, dialogues_properties["option_type"])
            continue


def play_dialogues_from_file(file_path):
    parsed_dialogues = parse_dialogue_file(file_path)
    render_dialogues(parsed_dialogues)


def render_options_menu(options_list):
    # NOTE: for display options as multiple choice by print
    option_number = 1

    for option in options_list:
        print(f"{ option_number }: {option['option']}")
        option_number += 1


# HACK: might need to break it down
def play_options_interactions(options_list, type):
    # options object
    if type == "multiple_choice":
        while True:
            render_options_menu(options_list)

            try:
                user_input = get_users_choice(len(options_list))
            except ValueError:
                print(f"You must enter a number between 1 and {len(options_list)}")
                continue

            render_dialogues(
                {
                    "dialogues": options_list[user_input - 1]["dialogues"],
                    "properties": {
                        "title": "option",
                    },
                }
            )
            break
        return None
        # TODO: Implement stats change after dialouge

    # WARNING: change index to number, index keeps changing as options are
    # popped
    if type == "elimination":
        # find terminating option's index
        # terminating_option_index = 0

        for option in options_list:
            # remove the $ mark
            option["terminating"] = False

            if option["option"].startswith("$"):
                option["option"] = option["option"][1:]
                option["terminating"] = True
                break

            # terminating_option_index += 1

        terminating_option_chosen = False

        # user prompt loop begin
        while not terminating_option_chosen:
            render_options_menu(options_list)
            try:
                user_input = get_users_choice(len(options_list))
            except ValueError:
                print(f"You must enter a number between 1 and {len(options_list)}")
                continue

            chosen_option = options_list[user_input - 1]

            if chosen_option["terminating"]:
                terminating_option_chosen = True

            print("\n")
            render_dialogues(
                {
                    "dialogues": options_list[user_input - 1]["dialogues"],
                    "properties": {
                        "title": "option",
                    },
                }
            )
            options_list.pop(user_input - 1)

        # TODO: may implement returning stats or wisdom points
        return None

    # TODO:
    # if regular / argument is last remaining_option type:
    # return user choice
