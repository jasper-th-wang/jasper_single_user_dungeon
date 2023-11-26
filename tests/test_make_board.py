from unittest import TestCase
from unittest.mock import patch

from simple_game import make_board


class Test(TestCase):
    def test_invalid_rows_and_columns(self):
        expected = None
        self.assertEqual(expected, make_board(1, 1))

    def test_valid_rows_invalid_columns(self):
        expected = None
        self.assertEqual(expected, make_board(3, 1))

    def test_invalid_rows_valid_columns(self):
        expected = None
        self.assertEqual(expected, make_board(1, 3))

    @patch('random.randint', side_effect=[0, 5, 3, 9])
    def test_valid_rows_and_columns(self, _):
        expected = {
            (0, 0): "The Server Room Labyrinth",
            (0, 1): "The Echo Hall of Helpdesk Calls",
            (1, 0): "The Printer Paper Jam Dungeon",
            (1, 1): "The Recursive Room"
        }
        self.assertEqual(expected, make_board(2, 2))

    @patch('random.randint', side_effect=[0, 5, 3, 9, 1, 2])
    def test_asymmetrical_board_row_larger_than_columns(self, _):
        expected = {
            (0, 0): "The Server Room Labyrinth",
            (0, 1): "The Echo Hall of Helpdesk Calls",
            (0, 2): "The Printer Paper Jam Dungeon",
            (1, 0): "The Recursive Room",
            (1, 1): "The Library of Obsolete Languages",
            (1, 2): "The Cafeteria of Constant Cravings"
        }
        self.assertEqual(expected, make_board(3, 2))

    @patch('random.randint', side_effect=[0, 5, 3, 9, 1, 2])
    def test_asymmetrical_board_columns_larger_than_rows(self, _):
        expected = {
            (0, 0): "The Server Room Labyrinth",
            (0, 1): "The Echo Hall of Helpdesk Calls",
            (1, 0): "The Printer Paper Jam Dungeon",
            (1, 1): "The Recursive Room",
            (2, 0): "The Library of Obsolete Languages",
            (2, 1): "The Cafeteria of Constant Cravings"
        }
        self.assertEqual(expected, make_board(2, 3))

    @patch('random.randint', side_effect=[0, 5, 3, 9, 1, 2, 4, 8, 1, 7, 3, 2])
    def test_more_coordinates_than_predefined_scenario_descriptions(self, _):
        expected = {
            (0, 0): "The Server Room Labyrinth",
            (0, 1): "The Echo Hall of Helpdesk Calls",
            (0, 2): "The Printer Paper Jam Dungeon",
            (0, 3): "The Recursive Room",
            (1, 0): "The Library of Obsolete Languages",
            (1, 1): "The Cafeteria of Constant Cravings",
            (1, 2): "The WiFi Woods",
            (1, 3): "The Firewall Fortress",
            (2, 0): "The Library of Obsolete Languages",
            (2, 1): "The Classroom of Endless Lectures",
            (2, 2): "The Printer Paper Jam Dungeon",
            (2, 3): "The Cafeteria of Constant Cravings"
        }
        self.assertEqual(expected, make_board(4, 3))
