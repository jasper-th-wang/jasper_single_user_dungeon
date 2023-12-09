from unittest import TestCase
from game_utils.handle_input import validate_character_input


class TestValidateCharacterInput(TestCase):
    def test_valid_lowercase_input(self):
        self.assertTrue(validate_character_input('a', 'abc'))

    def test_valid_uppercase_input(self):
        self.assertTrue(validate_character_input('A', 'abc'))

    def test_invalid_input(self):
        self.assertFalse(validate_character_input('d', 'abc'))

    def test_empty_string_input(self):
        self.assertFalse(validate_character_input('', 'abc'))

    def test_no_valid_characters(self):
        self.assertFalse(validate_character_input('a', ''))

    def test_multiple_characters_input(self):
        self.assertFalse(validate_character_input('ab', 'abc'))

    def test_non_alphabetic_input(self):
        self.assertFalse(validate_character_input('1', 'abc'))
