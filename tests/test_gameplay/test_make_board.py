from unittest import TestCase
from unittest.mock import patch
from gameplay.board import make_board


class TestMakeBoard(TestCase):
    @patch('random.randint', return_value=0)
    def test_no_npcs(self, mock_randint):
        level_info = {
            "rows": 2,
            "columns": 2,
            "area_descriptions": ["some scene"],
            "npcs": []
        }
        expected_board = {
            (0, 0): "some scene",
            (1, 0): "some scene",
            (0, 1): "some scene",
            (1, 1): "some scene"
        }

        actual_board = make_board(level_info)
        self.assertEqual(expected_board, actual_board)

    @patch('random.randint', return_value=0)
    def test_with_npcs(self, mock_randint):
        level_info = {
            "rows": 2,
            "columns": 2,
            "area_descriptions": ["some scene"],
            "npcs": [{"coordinates": [0, 0], "other_info": "npc info"}]
        }
        expected_board = {
            (0, 0): {"coordinates": [0, 0], "other_info": "npc info"},
            (1, 0): "some scene",
            (0, 1): "some scene",
            (1, 1): "some scene"
        }

        actual_board = make_board(level_info)
        self.assertEqual(expected_board, actual_board)

    @patch('random.randint', return_value=0)
    def test_asymmetrical_board(self, mock_randint):
        level_info = {
            "rows": 3,
            "columns": 2,
            "area_descriptions": ["some scene"],
            "npcs": []
        }
        expected_board = {
            (0, 0): "some scene",
            (1, 0): "some scene",
            (0, 1): "some scene",
            (1, 1): "some scene",
            (0, 2): "some scene",
            (1, 2): "some scene"
        }

        actual_board = make_board(level_info)
        self.assertEqual(expected_board, actual_board)

    def test_invalid_input_not_dict(self):
        level_info = "not a dictionary"
        with self.assertRaises(ValueError) as context:
            make_board(level_info)
        self.assertEqual("Invalid input: level_info must be a dictionary", str(context.exception))

    def test_invalid_input_missing_keys(self):
        level_info = {
            "rows": 2,
            "columns": 2,
            "area_descriptions": ["some scene"]
            # "npcs" key is missing
        }
        with self.assertRaises(ValueError) as context:
            make_board(level_info)
        self.assertEqual(
            "Invalid input: level_info must have the keys 'rows', 'columns', 'area_descriptions', and 'npcs'",
            str(context.exception))

