from unittest import TestCase
from game_utils.handle_input import validate_integer_input


class TestValidateIntegerInput(TestCase):
    def test_valid_input(self):
        self.assertTrue(validate_integer_input('3', 5))

    def test_out_of_range_input(self):
        self.assertFalse(validate_integer_input('6', 5))

    def test_non_digit_input(self):
        self.assertFalse(validate_integer_input('abc', 5))

    def test_negative_input(self):
        self.assertFalse(validate_integer_input('-3', 5))

    def test_zero_input(self):
        self.assertFalse(validate_integer_input('0', 5))

    def test_no_choices_input(self):
        self.assertFalse(validate_integer_input('3', 0))

    def test_empty_string_input(self):
        self.assertFalse(validate_integer_input('', 5))
