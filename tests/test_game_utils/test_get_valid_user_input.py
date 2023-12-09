"""
ADD A DOCSTRING
"""
from unittest import TestCase
from unittest.mock import patch
from game_utils.handle_input import get_valid_user_input


class TestGetValidUserInput(TestCase):
    @patch('builtins.input', return_value='1')
    def test_integer_input(self, mock_input):
        self.assertEqual(get_valid_user_input(number_of_choices=5), 1)

    @patch('builtins.input', return_value='a')
    def test_character_input(self, mock_input):
        self.assertEqual(get_valid_user_input(valid_characters='abc'), 'A')

    @patch('builtins.input', side_effect=['6', '3'])
    def test_invalid_then_valid_integer(self, mock_input):
        self.assertEqual(get_valid_user_input(number_of_choices=5), 3)

    @patch('builtins.input', side_effect=['d', 'b'])
    def test_invalid_then_valid_character(self, mock_input):
        self.assertEqual(get_valid_user_input(valid_characters='abc'), 'B')

    @patch('builtins.input', side_effect=['', '3'])
    def test_empty_input_then_valid_input(self, mock_input):
        self.assertEqual(get_valid_user_input(number_of_choices=5), 3)

    @patch('builtins.input', return_value='1')
    def test_both_integer_and_valid_options_with_integer_input(self, mock_input):
        self.assertEqual(get_valid_user_input(number_of_choices=4, valid_characters='a'), 1)

    @patch('builtins.input', return_value='a')
    def test_both_integer_and_valid_options_with_string_input(self, mock_input):
        self.assertEqual(get_valid_user_input(number_of_choices=4, valid_characters='a'), 'A')

    def test_no_validation_params(self):
        with self.assertRaises(ValueError):
            get_valid_user_input()
