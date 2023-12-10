import io
from unittest import TestCase
from unittest.mock import patch
from game import end_game_message


class TestEndGameMessage(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_message_no_character(self, mock_stdout, __):
        end_game_message(None)
        expected_print = (
            "[0mYou feel your essence gradually fade away, before you know it, you cease to exist in this realm."
            "\nPlease restart the game to try again.[0m\n\n"
        )
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_message_wisdom_greater(self, mock_stdout, __):
        character = {"Wisdom": 10, "Fury": 5}
        end_game_message(character)
        expected_print = (
            "[0mWith wisdom as your guide, you have woven a path of insight and harmony through a world of turmoil, "
            "leaving a legacy of enlightenment and peace that will echo through ages."
            "\nThe End.[0m\n\n"
        )
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_message_fury_greater_or_equal(self, mock_stdout, __):
        character = {"Wisdom": 5, "Fury": 10}
        end_game_message(character)
        expected_print = (
            "[0mIn a world craving balance, your path, fueled by unchecked fury, has left a trail marked by turmoil and "
            "conflict, a stark reminder of the cost of unbridled wrath."
            "\nThe End.[0m\n\n"
        )
        self.assertEqual(expected_print, mock_stdout.getvalue())
