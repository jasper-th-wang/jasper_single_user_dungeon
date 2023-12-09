import sys
from time import sleep

from gameplay.constants import TEXT_COLORS


def calculate_word_count(text):
    """
    Calculate the number of words in the text.

    :param text: A string.
    :precondition: text should be a string.
    :postcondition: no data is modified, and the number of words in the text is returned.
    :return: The number of words in the text.
    """
    stripped_text = text.strip().lower()
    words_in_text = stripped_text.split(" ")

    return len(words_in_text)


def calculate_delay_duration_in_seconds(text):
    """
    Calculate the delay duration in seconds based on the number of words in the text.

    :param text: A string.
    :precondition: text should be a string.
    :postcondition: no data is modified, and the delay duration in seconds is returned.
    :return: The delay duration in seconds.
    """
    # TODO: calculate base on average reading speed (238 words per minute)
    WORD_PER_SECOND = 15
    word_count = calculate_word_count(text)

    pause_duration = word_count / WORD_PER_SECOND

    # Cap max duration to 2 seconds
    pause_duration = min(pause_duration, 2)
    return pause_duration


def print_with_typewritter_effect(text):
    """
    Print the text with a typewritter effect.

    :param text: A string.
    :precondition: text should be a string.
    :postcondition: no data is modified, and the text is printed
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character in [",", "."]:
            sleep(0.15)
        sleep(0.01)
    print("\n")


def process_text_color(text):
    """
    Process the text color.

    :param text: A string.
    :precondition: text should be a string.
    :postcondition: no data is modified, and the text is returned with the color prefix removed.
    :return: The text with the color prefix removed.
    """
    # apply color, and remove color determining prefix
    COMMAND_LINE_COLOR = TEXT_COLORS
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
    """
    Print the text line by line.

    :param text: A string.
    :precondition: text should be a string.
    :postcondition: no data is modified, and the text is printed line by line.
    """
    text = process_text_color(text)
    print_with_typewritter_effect(text)
    delay_duration = calculate_delay_duration_in_seconds(text)
    sleep(delay_duration)
