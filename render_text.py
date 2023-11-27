import sys
from time import sleep

from constants import TEXT_COLOR


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
    COMMAND_LINE_COLOR = TEXT_COLOR()
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
