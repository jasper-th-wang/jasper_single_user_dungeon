# TODO: rename this module to like rendering utils??
import copy

from dialogue import dialogue_options
from gameplay import constants, render_text

OPTION_FLAG = constants.TEXT_FLAGS["OPTION_FLAG"]
CONTENT_START_FLAG = constants.TEXT_FLAGS["CONTENT_START_FLAG"]


def play_dialogues_from_file(file_path):
    parsed_dialogues = parse_dialogue_file(file_path)
    render_dialogues(parsed_dialogues)



def parse_dialogue_file(file_path):
    """
    Read and convert dialogue text files to dialogue dictionary for rendering

    :param file_path: strings representing path to a dialogue file
    :return: a dictionary representing information about a dialogue
    """
    try:
        with open(file_path, "r") as dialogues:
            lines = [line.rstrip() for line in dialogues.readlines() if not line.isspace()]

    except OSError:
        print("No dialogue text file is found")
    else:
        dialogues_properties = get_dialogue_file_properties(lines)
        index_of_content_start = lines.index(CONTENT_START_FLAG)

        dialogues_content = lines[index_of_content_start + 1: -1]
        renderable_dialogues = build_renderable_dialogue_list(dialogues_content)

        return {
            "properties": dialogues_properties,
            "dialogues": renderable_dialogues,
        }


def render_dialogues(parsed_dialogues_dictionary: dict) -> None:
    """
    Render lines one by one

    :param parsed_dialogues_dictionary:
    :return:
    """
    dialogues_properties = parsed_dialogues_dictionary["properties"]
    parsed_dialogues_list = parsed_dialogues_dictionary["dialogues"]

    for item in parsed_dialogues_list:
        if isinstance(item, str):
            render_text.print_text_line(item)
            continue
        if isinstance(item, list):
            dialogue_options.play_options_interactions(item, dialogues_properties["option_type"])
            continue

def build_renderable_dialogue_list(dialogue_content):
    dialogue_lines_list = []
    list_of_options = []

    # dialogue_content = [line for line in dialogue_content if line != "\n"]
    for line in dialogue_content:
        if OPTION_FLAG in line:
            list_of_options.append(process_option(line))
        elif line.startswith((" ", "\t")):
            line = line.strip()
            list_of_options[-1].setdefault("dialogues", []).append(line)
        else:
            if list_of_options:
                dialogue_lines_list.append(list_of_options)
                list_of_options = []
            dialogue_lines_list.append(line)

    return dialogue_lines_list


def get_dialogue_file_properties(lines):
    properties_lines = lines[:lines.index(CONTENT_START_FLAG)]
    return {
        prop.strip().split(": ", 1)[0]: prop.strip().split(": ", 1)[1] for prop in properties_lines if
        prop != CONTENT_START_FLAG
    }


def process_option(line):
    option = line.replace(OPTION_FLAG, "")
    terminating = option.startswith("$")
    option = option[1:] if terminating else option
    return {"option": option, "terminating": terminating}


