import dialogue.parse_dialogue
import interaction.options_interaction
import utils.render_text


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
            utils.render_text.print_text_line(item)
            continue
        if isinstance(item, list):
            interaction.options_interaction.play_options_interactions(item, dialogues_properties["option_type"])
            continue


def play_dialogues_from_file(file_path):
    parsed_dialogues = dialogue.parse_dialogue.parse_dialogue_file(file_path)
    render_dialogues(parsed_dialogues)
