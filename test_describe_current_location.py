import io
from unittest import TestCase
from unittest.mock import patch

from simple_game import describe_current_location


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_spawn_coordinates(self, mock_output):
        board = {
            (0, 0): "The Server Room Labyrinth",
            (0, 1): "The Library of Obsolete Languages",
            (1, 0): "The Cafeteria of Constant Cravings",
            (1, 1): "The Printer Paper Jam Dungeon"
        }
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        describe_current_location(board, character)
        printed_message = mock_output.getvalue()
        expected = "The Server Room Labyrinth\n"
        self.assertEqual(expected, printed_message)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_goal_coordinates(self, mock_output):
        board = {
            (0, 0): "The Server Room Labyrinth",
            (0, 1): "The Library of Obsolete Languages",
            (1, 0): "The Cafeteria of Constant Cravings",
            (1, 1): "The Printer Paper Jam Dungeon"
        }
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        describe_current_location(board, character)
        printed_message = mock_output.getvalue()
        expected = "The Printer Paper Jam Dungeon\n"
        self.assertEqual(expected, printed_message)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_any_coordinate_besides_spawn_and_goal_coordinates(self, mock_output):
        board = {
            (0, 0): "The Server Room Labyrinth",
            (0, 1): "The Library of Obsolete Languages",
            (1, 0): "The Cafeteria of Constant Cravings",
            (1, 1): "The Printer Paper Jam Dungeon"
        }
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        describe_current_location(board, character)
        printed_message = mock_output.getvalue()
        expected = "The Library of Obsolete Languages\n"
        self.assertEqual(expected, printed_message)
