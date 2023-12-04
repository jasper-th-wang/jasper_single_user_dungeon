import itertools

from typing import TextIO
from gameplay import constants
from game_utils import render_text
from narrative import options

OPTION_FLAG = constants.TEXT_FLAGS["OPTION_FLAG"]
CONTENT_START_FLAG = constants.TEXT_FLAGS["CONTENT_START_FLAG"]


# TODO: docstrings and unit tests
def play_dialogues_from_file_path(file_path):
    try:
        with open(file_path, "r") as dialogue_file:
            parsed_dialogues = parse_dialogue_file(dialogue_file)
    except OSError:
        print("No dialogue text file is found")
    else:
        render_dialogues(parsed_dialogues)


def parse_dialogue_file(dialogue_file: TextIO) -> dict:
    """
    Read and convert dialogue text files to dialogue dictionary for rendering

    :param dialogue_file:
    :return: a dictionary representing information about a dialogue
    """
    lines = [line.rstrip() for line in dialogue_file.readlines() if not line.isspace()]
    try:
        dialogues_properties = get_dialogue_file_properties(lines)
        dialogues_content = lines[lines.index(CONTENT_START_FLAG) + 1: -1]
        renderable_dialogues = build_renderable_dialogue_list(dialogues_content)
    except ValueError as e:
        print(f"Something went wrong when parsing dialogue file: {e}")
    else:
        return {
            "properties": dialogues_properties,
            "dialogues": renderable_dialogues,
        }


def get_dialogue_file_properties(lines: list) -> dict:
    """
    Get the properties of a dialogue file.
    
    :param lines: A list of strings representing the lines of the dialogue file.
    :return: A dictionary containing the properties of the dialogue file.
    >>> demo_lines = [
    ...     "Title: My Dialogue File",
    ...     "Author: John Doe",
    ...     "---",
    ...     "Line 1",
    ...     "Line 2",
    ... ]
    >>> get_dialogue_file_properties(demo_lines)
    {'Title': 'My Dialogue File', 'Author': 'John Doe'}
    """
    if "---" not in lines:
        raise ValueError("Content Start Flag '---' not found in this file.")
    properties_lines = lines[:lines.index(CONTENT_START_FLAG)]
    return {
        prop.strip().split(": ", 1)[0]: prop.strip().split(": ", 1)[1]
        for prop in properties_lines
    }


def render_dialogues(parsed_dialogues_dictionary: dict) -> None:
    """
    Takes a parsed dialogues dictionary and renders the dialogues line by line.

    :param parsed_dialogues_dictionary: A dictionary containing the parsed dialogues.
    """
    dialogues_properties = parsed_dialogues_dictionary["properties"]
    parsed_dialogues_list = parsed_dialogues_dictionary["dialogues"]

    for dialogue_item in parsed_dialogues_list:
        if isinstance(dialogue_item, str):
            render_text.print_text_line(dialogue_item)
            #TODO: if it's about stats, process it here
            continue
        if isinstance(dialogue_item, list):
            options.play_options_interactions(dialogue_item, dialogues_properties["option_type"])
            continue


def build_renderable_dialogue_list(dialogue_content: list) -> list:
    """
    Build a renderable dialogue list from a list of dialogue content.

    :param dialogue_content: A list of strings representing dialogue content.
    :return: A list of renderable dialogue elements.
    >>> demo_dialogue_content = [
    ...     "You slowly come to, a chilling sense of unease creeping over you.",
    ...     "-> Option 1",
    ...     "    Dialogue line 1",
    ...     "-> Option 2",
    ...     "    Dialogue line 2"
    ... ]
    >>> expected = [
    ...     "You slowly come to, a chilling sense of unease creeping over you.",
    ...     [
    ...         {
    ...             "option": "Option 1",
    ...             "terminating": False,
    ...             "dialogues": ["Dialogue line 1"]
    ...         },
    ...         {
    ...             "option": "Option 2",
    ...             "terminating": False,
    ...             "dialogues": ["Dialogue line 2"]
    ...         }
    ...     ]
    ... ]
    >>> build_renderable_dialogue_list(demo_dialogue_content) == expected
    True
    """
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


def create_renderable_options(option_lines: list) -> list:
    """
    Takes a list of option lines and processes them to create a list of renderable options.

    :param option_lines: A list of strings representing option lines.
    :return: A list of renderable options.
    >>> demo_option_lines = [ "-> Option 1", "    Dialogue line 1", "-> Option 2", "    Dialogue line 2" ]
    >>> expected = [{'option': 'Option 1', 'terminating': False, 'dialogues': ['Dialogue line 1']},
    ... {'option': 'Option 2','terminating': False, 'dialogues': ['Dialogue line 2']}]
    >>> create_renderable_options(demo_option_lines) == expected
    True
    """
    list_of_options = []
    for line in option_lines:
        if OPTION_FLAG in line:
            initialize_each_option(list_of_options, line)
        elif line.startswith((" ", "\t")):
            append_to_last_option(list_of_options, line)

    return list_of_options


def initialize_each_option(options_list: list, option_line: str) -> None:
    """
    Initializes each option in the options list based on the option line.

    :param options_list: A list of dictionaries representing options.
    :param option_line: A string representing the option line.
    :raises ValueError: If the options list is empty.
    >>> demo_options1 = []
    >>> initialize_each_option(demo_options1, "$Exit")
    >>> demo_options1
    [{'option': 'Exit', 'terminating': True, 'dialogues': []}]
    >>> demo_options_2 = []
    >>> initialize_each_option(demo_options_2, "Go to the next room")
    >>> demo_options_2
    [{'option': 'Go to the next room', 'terminating': False, 'dialogues': []}]
     """
    option_name = option_line.replace(OPTION_FLAG, "")
    if not option_name:
        raise ValueError("Option cannot be empty.")

    is_terminating = option_name.startswith("$")
    option_name = option_name[1:] if is_terminating else option_name
    option = {"option": option_name, "terminating": is_terminating, "dialogues": []}
    options_list.append(option)


def append_to_last_option(options_list: list, option_line: str) -> None:
    """
    Appends a dialogue line to the last option in the options list.

    :param options_list: A list of dictionaries representing options.
    :param option_line: A string representing the dialogue line to append.
    :raises ValueError: If the options list is empty.
    >>> demo_options1 = [{'option': 'Option 1', 'dialogues': ['Yo']}, {'option': 'Option 2', 'dialogues': []}]
    >>> append_to_last_option(demo_options1, "  Hello!")
    >>> demo_options1
    [{'option': 'Option 1', 'dialogues': ['Yo']}, {'option': 'Option 2', 'dialogues': ['Hello!']}]
    >>> demo_options2 = [{'option': 'Option 1', 'dialogues': ['Yo']}, {'option': 'Option 2', 'dialogues': ['Hello!']}]
    >>> append_to_last_option(demo_options2, "  How are you?")
    >>> demo_options2
    [{'option': 'Option 1', 'dialogues': ['Yo']}, {'option': 'Option 2', 'dialogues': ['Hello!', 'How are you?']}]
    """
    if not options_list:
        raise ValueError("Option list is empty, there is no option to append dialogue to.")
    options_list[-1].get("dialogues", []).append(option_line.lstrip())
