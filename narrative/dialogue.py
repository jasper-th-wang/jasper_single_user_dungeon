# TODO: rename this module to like rendering utils??
import itertools
from pprint import pprint

from gameplay import constants, render_text
from narrative import options

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


def get_dialogue_file_properties(lines):
    properties_lines = lines[:lines.index(CONTENT_START_FLAG)]
    return {
        prop.strip().split(": ", 1)[0]: prop.strip().split(": ", 1)[1] for prop in properties_lines if
        prop != CONTENT_START_FLAG
    }


def render_dialogues(parsed_dialogues_dictionary: dict) -> None:
    """
    Render lines one by one

    :param parsed_dialogues_dictionary:
    :return:
    """
    dialogues_properties = parsed_dialogues_dictionary["properties"]
    parsed_dialogues_list = parsed_dialogues_dictionary["dialogues"]

    for dialogue_item in parsed_dialogues_list:
        if isinstance(dialogue_item, str):
            render_text.print_text_line(dialogue_item)
            continue
        if isinstance(dialogue_item, list):
            options.play_options_interactions(dialogue_item, dialogues_properties["option_type"])
            continue


def build_renderable_dialogue_list(dialogue_content):
    def check_dialogue_type(dialogue_item):
        if OPTION_FLAG in dialogue_item or dialogue_item.startswith((" ", "\t")):
            return "options"
        return "dialogue_line"

    grouped_dialogue_items = itertools.groupby(dialogue_content, key=check_dialogue_type)

    renderable_dialogue_list = []
    for dialogue_type, dialogue_group in grouped_dialogue_items:
        if dialogue_type == "dialogue_line":
            renderable_dialogue_list.extend(dialogue_group)
        elif dialogue_type == "options":
            renderable_dialogue_list.append(create_renderable_options(dialogue_group))

    return renderable_dialogue_list


def create_renderable_options(options_line):
    list_of_options = []
    for line in options_line:
        if OPTION_FLAG in line:
            initialize_each_option(list_of_options, line)
        elif line.startswith((" ", "\t")):
            append_to_last_option(list_of_options, line)

    return list_of_options


def initialize_each_option(options_list, option_line):
    """
    Initializes each option in the options list based on the option line.

    :param options_list: A list of dictionaries representing options.
    :param option_line: A string representing the option line.
    >>> demo_options1 = []
    >>> initialize_each_option(demo_options1, "$Exit")
    >>> demo_options1
    [{'option': 'Exit', 'terminating': True}]

    >>> demo_options_2 = []
    >>> initialize_each_option(demo_options_2, "Go to the next room")
    >>> demo_options_2
    [{'option': 'Go to the next room', 'terminating': False}]
     """
    option_name = option_line.replace(OPTION_FLAG, "")
    terminating = option_name.startswith("$")
    option_name = option_name[1:] if terminating else option_name
    option = {"option": option_name, "terminating": terminating}
    options_list.append(option)


def append_to_last_option(options_list, option_line):
    """
    Appends a dialogue line to the last option in the options list.

    :param options_list: A list of dictionaries representing options.
    :param option_line: A string representing the dialogue line to append.
    :raises ValueError: If the options list is empty.
    >>> demo_options1 = [{'option': 'Option 1', 'dialogues': ['Yo']}, {'option': 'Option 2'}]
    >>> append_to_last_option(demo_options1, "Hello!")
    >>> demo_options1
    [{'text': 'Option 1', 'dialogues': ['Yo']}, {'text': 'Option 2', 'dialogues': ['Hello!']}]

    >>> demo_options2 = [{'text': 'Option 1', 'dialogues': ['Yo']}, {'text': 'Option 2', 'dialogues': ['Hello!']}]
    >>> append_to_last_option(demo_options2, "How are you?")
    >>> demo_options2
    [{'text': 'Option 1', 'dialogues': ['Yo']}, {'text': 'Option 2', 'dialogues': ['Hello!', 'How are you?']}]

    """
    if not options_list:
        raise ValueError("Option list is empty, there is no option to append dialogue to.")
    options_list[-1].setdefault("dialogues", []).append(option_line.lstrip())
