from unittest import TestCase
from gameplay.board import get_board_dimensions


class TestGetBoardDimensions(TestCase):
    def test_get_board_dimensions_normal(self):
        self.assertEqual((2, 2), get_board_dimensions({(0, 0): 'some scene', (1, 1): 'O', (2, 2): 'some scene'}))

    def test_get_board_dimensions_different_x_y(self):
        self.assertEqual((2, 3), get_board_dimensions({(0, 0): 'some scene', (1, 2): 'O', (2, 3): 'some scene'}))

    def test_get_board_dimensions_empty_board(self):
        with self.assertRaises(ValueError):
            get_board_dimensions({})

    def test_get_board_dimensions_non_dict(self):
        with self.assertRaises(ValueError):
            get_board_dimensions("not a dict")

    def test_get_board_dimensions_non_tuple_keys(self):
        with self.assertRaises(ValueError):
            get_board_dimensions({"not a tuple": "some scene"})

    def test_get_board_dimensions_incorrect_tuple_length(self):
        with self.assertRaises(ValueError):
            get_board_dimensions({(0, 0, 0): "some scene"})
