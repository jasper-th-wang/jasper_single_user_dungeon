import random

from game_utils import render_text, handle_input

FURY_INCREMENT = 5
WISDOM_INCREMENT = 5
ESSENCE_DECREMENT = 5
KILL_MONSTER_OPTION = "K"


def play_monster_encounter(character):
    render_text.print_text_line("!>>> !!! ALERT: MONSTER ENCOUNTER !!! <<<")

    lower = 1
    upper = determine_upper_bound(character["Wisdom"])
    secret_number = random.randint(lower, upper)

    print(
        f"Enter a number between {lower} and {upper} inclusive to deter the monster, or type '{KILL_MONSTER_OPTION}' to kill the monster"
    )

    guess = handle_input.get_valid_user_input(upper, KILL_MONSTER_OPTION)

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
        "You killed the monster ruthlessly. Though you are unharmed, you feel an anger inside brewing."
    )
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
