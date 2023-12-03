"""
Jasper Wang
A01362031
"""
import narrative.dialogue
import gameplay.character
from gameplay.level import play_level


# WARNING: sourcing test file for now
def opening_sequence():
    narrative.dialogue.play_dialogues_from_file_path("assets/dialogues/opening.txt")


def game():
    MAX_LEVEL = 3
    # HACK: commented out
    # opening_sequence()
    character = gameplay.character.make_character()
    for level in range(1, MAX_LEVEL + 1):
        character = play_level(level, character)
        # TODO: What?
        if character is None:
            return


def main():
    game()
    # narrative.dialogue.test_main()


if __name__ == '__main__':
    main()
