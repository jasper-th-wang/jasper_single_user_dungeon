from unittest import TestCase
from gameplay.character import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 1}
        move_character(character, 'W')
        self.assertEqual({'X-coordinate': 0, 'Y-coordinate': 0}, character)

    def test_move_character_south(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        move_character(character, 'S')
        self.assertEqual({'X-coordinate': 0, 'Y-coordinate': 1}, character)

    def test_move_character_east(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        move_character(character, 'D')
        self.assertEqual({'X-coordinate': 1, 'Y-coordinate': 0}, character)

    def test_move_character_west(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 0}
        move_character(character, 'A')
        self.assertEqual({'X-coordinate': 0, 'Y-coordinate': 0}, character)
