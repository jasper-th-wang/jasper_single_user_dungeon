# TODO: rename this module to like rendering utils??
import copy

from gameplay import constants


def get_dialogue_file_properties(property_line_list):
    dialogues_properties = {}
    CONTENT_START_FLAG = constants.TEXT_FLAGS["CONTENT_START_FLAG"]

    for line in property_line_list:
        line = line.strip()

        if line == CONTENT_START_FLAG:
            break

        yarn_property = line.split(": ")
        dialogues_properties[yarn_property[0]] = yarn_property[1]

    return dialogues_properties


# TODO: function way too big
def build_renderable_dialogue_list(dialogue_content):
    dialogue_lines_list = []
    OPTION_FLAG = constants.TEXT_FLAGS["OPTION_FLAG"]
    list_of_options = []  # list of option
    for line in dialogue_content:
        if line == "\n":
            continue
        line = line.rstrip()
        if OPTION_FLAG in line:
            option = {"option": line.replace(OPTION_FLAG, "")}
            option["terminating"] = option["option"].startswith("$")
            option["option"] = option["option"][1:] if option["terminating"] else option["option"]
            list_of_options.append(option)
        elif line.startswith((" ", "\t")):
            line = line.strip()
            list_of_options[-1].setdefault("dialogues", []).append(line)
        elif list_of_options:
            dialogue_lines_list.append(list_of_options)
            list_of_options = []
        else:
            dialogue_lines_list.append(line)

    return dialogue_lines_list


def parse_dialogue_file(file_path):
    """
    Read and convert dialogue text files to dialogue dictionary for rendering

    :param file_path: strings representing path to a dialogue file
    :return: a dictionary representing information about a dialogue
    """
    CONTENT_START_FLAG = constants.TEXT_FLAGS["CONTENT_START_FLAG"]
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
