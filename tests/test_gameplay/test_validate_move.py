from unittest import TestCase
from gameplay.board import validate_move


class TestValidateMove(TestCase):
    def test_move_within_bounds(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Essence": 3}
        self.assertTrue(validate_move(3, 3, character, "W"))
        self.assertTrue(validate_move(3, 3, character, "S"))
        self.assertTrue(validate_move(3, 3, character, "D"))
        self.assertTrue(validate_move(3, 3, character, "A"))

    def test_move_out_of_bounds(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Essence": 3}
        self.assertFalse(validate_move(3, 3, character, "W"))
        self.assertFalse(validate_move(3, 3, character, "A"))

        character = {"X-coordinate": 2, "Y-coordinate": 2, "Essence": 3}
        self.assertFalse(validate_move(3, 3, character, "S"))
        self.assertFalse(validate_move(3, 3, character, "D"))

    def test_move_on_edge(self):
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Essence": 3}
        self.assertTrue(validate_move(3, 3, character, "S"))
        self.assertTrue(validate_move(3, 3, character, "W"))

        character = {"X-coordinate": 1, "Y-coordinate": 2, "Essence": 3}
        self.assertTrue(validate_move(3, 3, character, "A"))
        self.assertTrue(validate_move(3, 3, character, "D"))
