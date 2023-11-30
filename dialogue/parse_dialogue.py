# TODO: rename this module to like rendering utils??
import copy

from utils.constants import TEXT_FLAGS


def get_dialogue_file_properties(property_line_list):
    dialogues_properties = {}
    CONTENT_START_FLAG = TEXT_FLAGS()["CONTENT_START_FLAG"]

    for line in property_line_list:
        line = line.strip()

        if line == CONTENT_START_FLAG:
            break

        yarn_property = line.split(": ")
        dialogues_properties[yarn_property[0]] = yarn_property[1]

    return dialogues_properties


def add_options_to_dialogue_line_list(option, list_of_options, dialogue_lines_list):
    list_of_options.append(copy.copy(option))
    option.clear()
    dialogue_lines_list.append(copy.copy(list_of_options))
    list_of_options.clear()


def add_dialogue_line_to_option(line, option):
    line = line.strip()
    if "dialogues" in option:
        option["dialogues"].append(line)
    else:
        option["dialogues"] = [line]


def initialize_option(line, option, list_of_options):
    OPTION_FLAG = TEXT_FLAGS()["OPTION_FLAG"]
    # if an option already exists, store and clear that dictionary
    if option:
        # TODO: maybe need to use deepcopy?
        list_of_options.append(copy.copy(option))
        option.clear()

    # initialize option dictionary
    option["option"] = line.replace(OPTION_FLAG, "")


# TODO: function way too big
def build_renderable_dialogue_list(dialogue_content):
    dialogue_lines_list = []
    OPTION_FLAG = TEXT_FLAGS()["OPTION_FLAG"]
    list_of_options = []  # list of option
    option = {}

    for line in dialogue_content:
        if line == "\n":
            continue

        line = line.rstrip()

        if OPTION_FLAG in line:
            initialize_option(line, option, list_of_options)
            continue

        if line.startswith((" ", "\t")):
            add_dialogue_line_to_option(line, option)
            continue

        # on new normal line, check if option related values are stored, if
        # not, store it
        if option:
            add_options_to_dialogue_line_list(option, list_of_options, dialogue_lines_list)

        dialogue_lines_list.append(line)

    # after exhausting list, check if option related values are stored, if
    # not, store it
    if option:
        add_options_to_dialogue_line_list(option, list_of_options, dialogue_lines_list)

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
        dialogues_properties = get_dialogue_file_properties(lines)
        index_of_content_start = lines.index(CONTENT_START_FLAG + "\n")

        dialogues_content = lines[index_of_content_start + 1: -1]
        renderable_dialogues = build_renderable_dialogue_list(dialogues_content)

        return {
            "properties": dialogues_properties,
            "dialogues": renderable_dialogues,
        }

# HACK: might need to break it down
