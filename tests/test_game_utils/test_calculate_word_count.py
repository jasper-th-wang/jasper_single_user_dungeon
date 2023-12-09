from unittest import TestCase
from game_utils.render_text import calculate_word_count


class TestCalculateWordCount(TestCase):
    def test_empty_string(self):
        self.assertEqual(0, calculate_word_count(''))

    def test_single_word(self):
        self.assertEqual(1, calculate_word_count('word'))

    def test_multiple_words(self):
        self.assertEqual(4, calculate_word_count('This is a test'))

    def test_strings_with_leading_and_trailing_spaces(self):
        self.assertEqual(4, calculate_word_count('  This is a test  '))

    def test_strings_with_multiple_spaces_between_words(self):
        self.assertEqual(4, calculate_word_count('This  is  a  test'))
