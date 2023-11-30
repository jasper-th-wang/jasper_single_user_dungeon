from dialogue.parse_dialogue import parse_dialogue_file
from interaction.options_interaction import play_options_interactions
from utils.render_text import print_text_line


def render_dialogues(parsed_dialogues_dictionary):
    """
    Render lines one by one

    :param parsed_dialogues_dictionary:
    :return:
    """
    dialogues_properties = parsed_dialogues_dictionary["properties"]
    parsed_dialogues_list = parsed_dialogues_dictionary["dialogues"]

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
