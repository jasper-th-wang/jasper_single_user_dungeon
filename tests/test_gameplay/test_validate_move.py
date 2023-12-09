from unittest import TestCase
from gameplay.board import validate_move


class Test(TestCase):
    def test_moving_to_just_before_north_boundary(self):
        direction = 1
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
        rows = 2
        columns = 2
        expected = True

        self.assertEqual(expected, validate_move(rows, columns, character, direction))

    def test_moving_over_north_boundary(self):
        direction = 1
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 3}
        rows = 2
        columns = 2
        expected = False

        self.assertEqual(expected, validate_move(rows, columns, character, direction))

    def test_moving_to_just_before_south_boundary(self):
        direction = 2
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 3}
        rows = 2
        columns = 2
        expected = True

        self.assertEqual(expected, validate_move(rows, columns, character, direction))

    def test_moving_over_south_boundary(self):
        direction = 2
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
        rows = 2
        columns = 2
        expected = False

        self.assertEqual(expected, validate_move(rows, columns, character, direction))

    def test_moving_to_just_before_east_boundary(self):
        direction = 3
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 3}
        rows = 2
        columns = 2
        expected = True

        self.assertEqual(expected, validate_move(rows, columns, character, direction))

    def test_moving_over_east_boundary(self):
        direction = 3
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
        rows = 2
        columns = 2
        expected = False

        self.assertEqual(expected, validate_move(rows, columns, character, direction))

    def test_moving_to_just_before_west_boundary(self):
        direction = 4
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
        rows = 2
        columns = 2
        expected = True

        self.assertEqual(expected, validate_move(rows, columns, character, direction))

    def test_moving_over_west_boundary(self):
        direction = 4
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 3}
        rows = 2
        columns = 2
        expected = False

        self.assertEqual(expected, validate_move(rows, columns, character, direction))

    def test_moving_in_middle_of_board(self):
        direction = 2
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 3}
        rows = 4
        columns = 4
        expected = True

        self.assertEqual(expected, validate_move(rows, columns, character, direction))
