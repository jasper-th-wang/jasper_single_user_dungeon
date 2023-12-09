"""
ADD A DOCSTRING
"""
from unittest import TestCase
from unittest.mock import patch
from game_utils.handle_input import get_valid_user_input


class TestGetValidUserInput(TestCase):
    @patch('builtins.input', return_value='1')
    def test_integer_input(self, mock_input):
        self.assertEqual(1, get_valid_user_input(number_of_choices=5))

    @patch('builtins.input', return_value='a')
    def test_character_input(self, mock_input):
        self.assertEqual('A', get_valid_user_input(valid_characters='abc'))

    @patch('builtins.input', side_effect=['6', '3'])
    def test_invalid_then_valid_integer(self, mock_input):
        self.assertEqual(3, get_valid_user_input(number_of_choices=5))

    @patch('builtins.input', side_effect=['d', 'b'])
    def test_invalid_then_valid_character(self, mock_input):
        self.assertEqual('B', get_valid_user_input(valid_characters='abc'))

    @patch('builtins.input', side_effect=['', '3'])
    def test_empty_input_then_valid_input(self, mock_input):
        self.assertEqual(3, get_valid_user_input(number_of_choices=5))

    @patch('builtins.input', return_value='1')
    def test_both_integer_and_valid_options_with_integer_input(self, mock_input):
        self.assertEqual(1, get_valid_user_input(number_of_choices=4, valid_characters='a'))

    @patch('builtins.input', return_value='a')
    def test_both_integer_and_valid_options_with_string_input(self, mock_input):
        self.assertEqual('A', get_valid_user_input(number_of_choices=4, valid_characters='a'))

    def test_no_validation_params(self):
        with self.assertRaises(ValueError):
            get_valid_user_input()
