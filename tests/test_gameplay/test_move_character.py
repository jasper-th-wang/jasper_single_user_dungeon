from unittest import TestCase
from gameplay.character import move_character


class Test(TestCase):
    def test_moving_character_to_north(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
        direction = 1
        move_character(character, direction)
        expected = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 3}
        self.assertEqual(expected, character)

    def test_moving_character_to_south(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
        direction = 2
        move_character(character, direction)
        expected = {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 3}
        self.assertEqual(expected, character)

    def test_moving_character_to_east(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
        direction = 3
        move_character(character, direction)
        expected = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 3}
        self.assertEqual(expected, character)

    def test_moving_character_to_west(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
        direction = 4
        move_character(character, direction)
        expected = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 3}
        self.assertEqual(expected, character)
