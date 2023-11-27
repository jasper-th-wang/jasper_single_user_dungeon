# TODO: rename this module to like rendering utils??
import sys
from pprint import pprint
from time import sleep

CONTENT_START_FLAG = "---"
OPTION_FLAG = "-> "
COMMAND_LINE_COLOR = {
    "HEADER": "\033[95m",
    "NPC": "\033[94m",
    "OKCYAN": "\033[96m",
    "PLAYER": "\033[92m",
    "YELLOW": "\033[93m",
    "ENEMY": "\033[91m",
    "NORMAL": "\033[0m",
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
}


def calculate_word_count(text):
    stripped_text = text.strip().lower()
    words_in_text = stripped_text.split(" ")

    return len(words_in_text)


def calculate_delay_duration_in_seconds(text):
    # TODO: calculate base on average reading speed (238 words per minute)
    WORD_PER_SECOND = 15
    word_count = calculate_word_count(text)
    # print(word_count)
    pause_duration = word_count / WORD_PER_SECOND
    # print(pause_duration)
    return pause_duration


# only use when it's describing the scene
def print_with_typewritter_effect(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character == "," or character == ".":
            sleep(0.15)
        sleep(0.01)
    print("\n")


def process_text_color(text):
    # apply color, and remove color determining prefix
    color_type = "NORMAL"

    if text.startswith("$"):
        color_type = "PLAYER"
    elif text.startswith("@"):
        color_type = "NPC"
    elif text.startswith("!"):
        color_type = "YELLOW"

    if color_type != "NORMAL":
        text = text[1:]

    return f"{COMMAND_LINE_COLOR[color_type]}{text}{COMMAND_LINE_COLOR['NORMAL']}"


def print_text_line(text):
    text = process_text_color(text)
    print_with_typewritter_effect(text)
    delay_duration = calculate_delay_duration_in_seconds(text)
    sleep(delay_duration)


def parse_yarn_properties(property_line_list):
    dialogues_properties = {}

    for line in property_line_list:
        line = line.strip()

        if line == CONTENT_START_FLAG:
            break

        property = line.split(": ")
        dialogues_properties[property[0]] = property[1]
    # HACK: to remove
    pprint(dialogues_properties)
    return dialogues_properties


def parse_yarn_content(content_line_list):
    parsed_dialogues = []
    options_list = []  # list of options
    options_content = {}

    for line in content_line_list:
        if line == "\n":
            continue

        line = line.rstrip()
        if OPTION_FLAG in line:
            # clear previous options_content dictionary
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

        # on new normal line, check if options related values are stored, if not, store it
        if options_content:
            options_list.append(options_content)
            options_content = {}
            parsed_dialogues.append(options_list)
            options_list = []

        parsed_dialogues.append(line)

    # after exhausting list, check if options related values are stored, if not, store it
    if options_content:
        options_list.append(options_content)
        options_content = {}
        parsed_dialogues.append(options_list)
        options_list = []

    return parsed_dialogues


def parse_yarn_file(file_path):
    try:
        with open(file_path, "r") as dialogues:
            lines = dialogues.readlines()

    except OSError:
        print("No dialogue text file is found")
    else:
        dialogues_properties = parse_yarn_properties(lines)
        index_of_content_start = lines.index(CONTENT_START_FLAG + "\n")

        dialogues_content = lines[index_of_content_start + 1 : -1]
        parsed_dialogues = parse_yarn_content(dialogues_content)

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
            prompt_user_options(item, dialogues_properties["option_type"])
            continue


def play_dialogues_from_file(file_path):
    parsed_dialogues = parse_yarn_file(file_path)
    render_dialogues(parsed_dialogues)


def render_options(options_list):
    # NOTE: for display options as multiple choice by print
    option_number = 1

    for option in options_list:
        print(f"{ option_number }: {option['option']}")
        option_number += 1


def get_users_choice(number_of_choices):
    """
    Print a prompt to get the desired choice number from user

    :raises ValueError:
    :return: a positive integer representing the user's inputted value
    """
    user_input = int(input("Enter your choice: "))

    if user_input not in range(1, number_of_choices + 1):
        raise ValueError(f"User input has to be between 1 and {number_of_choices}")

    return user_input


def prompt_user_options(options_list, type):
    # options object
    # WARNING: change index to number, index keeps changing as options are popped
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
            # pprint(options_list)
            # print("terminating index: " + str(terminating_option_index))
            render_options(options_list)
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


def print_text_file(file_path):
    try:
        with open(file_path, "r") as input_file:
            texts = input_file.readlines()
            print_text_line(texts)

    except OSError:
        print("No dialogue text file is found")
    print("test!")


def test():
    mock_list2 = [
        "-> Run away",
        "    Without a second thought, you turn and dash away, your feet pounding against the cold, stone ground.",
        "    Then, just as you think you've lost him, you round a corner and come face-to-face with the same figure, standing calmly as if he'd been waiting for you all along.",
        "    'Running won't change your situation,' he says, his voice still calm and soothing, a stark contrast to your panting breaths. 'But it's understandable. This place can be... overwhelming for newcomers.'",
        "-> $Ask who he is",
        "    'Who are you?' you ask, your voice tinged with a mix of curiosity and caution.",
    ]
    mock_yarn_dict = {
        "properties": {"title": "start", "option_type": "elimination"},
        "dialogues": [
            "You slowly come to, a chilling sense of unease creeping over you. ",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once. ",
        ],
    }
    # render_dialogues(mock_yarn_dict)
    mock_choices = [
        {
            "option": "$Take a deep breath",
            "dialogues": [
                "The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries."
            ],
        },
        {
            "option": "Sit up and stretch",
            "dialogues": [
                "You sit up, your hands brushing against a cold, damp ground that seems to be made of stone, yet oddly smooth, like polished marble left neglected for ages."
            ],
        },
    ]
    mock_dialogues_dict = {
        "properties": {"title": "start", "option_type": "elimination"},
        "dialogues": [
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once.",
            [
                {
                    "option": "Take a deep breath",
                    "dialogues": [
                        "The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries."
                    ],
                },
                {
                    "option": "$Sit up and stretch",
                    "dialogues": [
                        "You sit up, your hands brushing against a cold, damp ground that seems to be made of stone, yet oddly smooth, like polished marble left neglected for ages."
                    ],
                },
            ],
            "Tall, imposing columns rise to a ceiling lost in darkness, carved with intricate designs that seem to shift and move in the corner of your eye.",
        ],
    }
    test_dialogues = parse_yarn_file("./dialogues/opening.yarn")
    render_dialogues(test_dialogues)


# test()
