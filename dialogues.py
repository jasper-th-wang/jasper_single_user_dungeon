import sys
from time import sleep

CONTENT_START_FLAG = "---"
OPTION_FLAG = "-> "


def prompt_user_options(options):
    # options object

    # if elimination type / there are nested options object:
    # prompt_user_options(remaining_options)

    # if regular / argument is last remaining_option type:
    # return user choice
    pass


def get_yarn_properties(property_line_list):
    dialogues_properties = {}

    # Get Properties
    index_of_content_start = 0

    for line in property_line_list:
        line = line.strip()
        if line == CONTENT_START_FLAG:
            break
        index_of_content_start += 1
        property = line.split(": ")
        dialogues_properties[property[0]] = property[1]

    return dialogues_properties


def parse_yarn_content(content_line_list):
    parsed_dialogues = []
    # for line in lines:
    # store each top level line directly in list
    # when see "->", start a while loop, and store lines that have root tab level + 1 extra tab level into an dictionary

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

        if line.startswith("\t"):
            if "content" in options_content:
                options_content["content"].append(line)
            else:
                options_content["content"] = [line]

            continue

        if options_list:
            parsed_dialogues.append(options_list)

        parsed_dialogues.append(line)

    # how to scope a line of texts
    # get current tab level
    # while tab level is same
    # same scope!


def parse_yarn_file(file_path):
    CONTENT_START_FLAG = "---"
    with open(file_path, "r") as dialogues:
        lines = dialogues.readlines()
        # print(lines)
        dialogues_properties = get_yarn_properties(lines)

        # print(dialogues_properties)

        # WARNING: index is undefined NEEDS to be fixed
        # dialogues_content = lines[index_of_content_start + 1 : -1]
        # parsed_dialogues = parse_yarn_content(dialogues_content)
        # print(dialogues_content)


# parse_yarn_file("./dialogues/opening.yarn")


def calculate_word_count(text):
    stripped_text = text.strip().lower()
    words_in_text = stripped_text.split(" ")
    # print(words_in_text)

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


def print_with_delay(text_list):
    for text in text_list:
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


# print_text_file("test.txt")
