import sys
from pprint import pprint
from time import sleep

CONTENT_START_FLAG = "---"
OPTION_FLAG = "-> "


def prompt_user_options(options, type):
    # options object

    # if elimination type / there are nested options object:
    # prompt_user_options(remaining_options)

    # if regular / argument is last remaining_option type:
    # return user choice
    pass


def get_yarn_properties(property_line_list):
    dialogues_properties = {}

    for line in property_line_list:
        line = line.strip()

        if line == CONTENT_START_FLAG:
            break

        property = line.split(": ")
        dialogues_properties[property[0]] = property[1]

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
                print("options_content is not empty!!")
                options_list.append(options_content)
                options_content = {}
            # initialize option dictionary
            options_content["option"] = line.replace(OPTION_FLAG, "")
            continue

        if line.startswith((" ", "\t")):
            line = line.strip()
            if "content" in options_content:
                options_content["content"].append(line)
            else:
                options_content["content"] = [line]

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
        dialogues_properties = get_yarn_properties(lines)
        index_of_content_start = lines.index(CONTENT_START_FLAG + "\n")

        dialogues_content = lines[index_of_content_start + 1 : -1]
        parsed_dialogues = parse_yarn_content(dialogues_content)

        return {
            property: dialogues_properties,
            dialogues: parsed_dialogues,
        }


def render_dialogues(parsed_yarn_dict):
    pass


def calculate_word_count(text):
    stripped_text = text.strip().lower()
    words_in_text = stripped_text.split(" ")

    return len(words_in_text)


def calculate_delay_duration_in_seconds(text):
    # TODO: calculate base on average reading speed (238 words per minute)
    WORD_PER_SECOND = 5
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
            sleep(1)
        sleep(0.01)


def print_with_delay(text):
    print_with_typewritter_effect(text)
    delay_duration = calculate_delay_duration_in_seconds(text)
    sleep(delay_duration)


def print_text_file(file_path):
    try:
        with open(file_path, "r") as input_file:
            texts = input_file.readlines()
            print_with_delay(texts)

    except OSError:
        print("No dialogue text file is found")
    print("test!")
