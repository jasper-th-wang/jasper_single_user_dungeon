import random

from gameplay import render_text
from gameplay.handle_input import get_valid_user_input

FURY_INCREMENT = 5
WISDOM_INCREMENT = 5
ESSENCE_DECREMENT = 5
KILL_MONSTER_OPTION = 'K'


def play_monster_encounter(character):
    render_text.print_text_line("!>>> !!! ALERT: MONSTER ENCOUNTER !!! <<<")

    lower = 1
    upper = determine_upper_bound(character['Wisdom'])
    secret_number = random.randint(lower, upper)

    print(
        f"Enter a number between {lower} and {upper} inclusive to deter the monster, or type '{KILL_MONSTER_OPTION}' to kill the monster")

    guess = get_valid_user_input(upper, KILL_MONSTER_OPTION)

    if guess == KILL_MONSTER_OPTION:
        kill_monster(character)
        return

    if int(guess) == secret_number:
        deter_monster(character)
    else:
        fail_to_deter_monster(character)


# TODO: Need improvement
def determine_upper_bound(wisdom_points):
    if wisdom_points > 30:
        return 3
    elif wisdom_points > 50:
        return 2
    elif wisdom_points > 100:
        return 1
    else:
        return 5


def kill_monster(character):
    render_text.print_text_line(
        "You killed the monster ruthlessly. Though you are unharmed, you feel an anger inside brewing.")
    render_text.print_text_line(f"!You gained {FURY_INCREMENT} Fury")
    character["Fury"] += FURY_INCREMENT


def deter_monster(character):
    render_text.print_text_line("You successfully deterred the monster!")
    render_text.print_text_line(f"$You gained {WISDOM_INCREMENT} Wisdom!")
    character["Wisdom"] += WISDOM_INCREMENT


def fail_to_deter_monster(character):
    character["Essence"] -= ESSENCE_DECREMENT
    render_text.print_text_line("You failed, the monster attacked you and ran away.")
    render_text.print_text_line(f"!You just lost {ESSENCE_DECREMENT} Essence Point")

# def play_monster_encounter(character):
#     """
#     Start a game number guessing game where user has to guess the randomly generated number between 1 and 5
#
#     :param character: a game character
#     :precondition: character is a game character generated by the make_character() function in this module
#     :postcondition: Essence is deducted from character if user guesses incorrectly, no data is modified otherwise
#     :return: None
#     """
#     render_text.print_text_line("!>>> !!! ALERT: MONSTER ENCOUNTER !!! <<<")
#
#     lower = 1
#     upper = determine_upper_bound(character['Wisdom'])
#
#     secret_number = random.randint(lower, upper)
#
#     print(
#         f"Enter a number between {lower} and {upper} inclusive to deter the monster, or type 'K' to kill the monster"
#     )
#
#     guess = get_valid_user_input(upper, "K")
#
#     if guess == "K":
#         render_text.print_text_line(
#             "You killed the monster ruthlessly. Though you are unharmed, you feel an anger inside brewing."
#         )
#         render_text.print_text_line(f"!You gained {FURY_INCREMENT} Fury")
#         character["Fury"] += FURY_INCREMENT
#         return
#
#     if int(guess) == secret_number:
#         render_text.print_text_line("You successfully deterred the monster!")
#         render_text.print_text_line(f"$You gained {WISDOM_INCREMENT} Wisdom!")
#         character["Wisdom"] += WISDOM_INCREMENT
#     else:
#         character["Essence"] -= ESSENCE_DECREMENT
#         render_text.print_text_line("You failed, the monster attacked you and ran away.")
#         render_text.print_text_line(f"!You just lost {ESSENCE_DECREMENT} Essence Point")

# TODO: Change docstrings
# def play_monster_encounter(character):
#     """
#     Start a test_game number guessing test_game where user has to guess the randomly generated number between 1 and 5
#
#     :param character: a test_game character
#     :precondition: character is a test_game character generated by the make_character() function in this module
#     :postcondition: 1 HP is deducted from character if user guesses incorrectly, no data is modified otherwise
#     :return: None
#     """
#     render_text.print_text_line("!>>> !!! ALERT: MONSTER ENCOUNTER !!! <<<")
#     # with K as kill
#     # if user use guess: they gain wisdom
#     # if user use kill, they gain anger
#
#     # if character wisdom is high, range becomes lower
#     lower = 1
#     upper = determine_upper_bound(character['Wisdom'])
#
#     secret_number = random.randint(lower, upper)
#
#     print(
#         f"Enter a number between {lower} and {upper} inclusive to deterred the monster, or type 'K' to kill the monster"
#     )
#
#     guess = get_valid_user_input(upper, "K")
#
#     if guess == "K":
#         render_text.print_text_line(
#             "You killed the monster ruthlessly. Though you are unharmed, you feel an anger inside brewing."
#         )
#         render_text.print_text_line("!You gained 5 Fury")
#         character["Fury"] += 5
#         return
#
#     if int(guess) == secret_number:
#         render_text.print_text_line("You succesfully deterred the monster!")
#         render_text.print_text_line("$You gained 5 Wisdom!")
#         character["Wisdom"] += 5
#     else:
#         character["Essence"] -= 5
#         render_text.print_text_line(f"You failed, the monster attacked you and ran away.")
#         render_text.print_text_line("!You just lost 5 Essence Point")
