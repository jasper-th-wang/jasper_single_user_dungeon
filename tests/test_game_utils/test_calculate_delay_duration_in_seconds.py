from unittest import TestCase

from game_utils.render_text import calculate_delay_duration_in_seconds


class TestCalculateDelayDurationInSeconds(TestCase):
    def test_empty_string(self):
        self.assertEqual(0, calculate_delay_duration_in_seconds(''))

    def test_single_word(self):
        self.assertEqual(1 / 15, calculate_delay_duration_in_seconds('word'))

    def test_multiple_words(self):
        self.assertEqual(4 / 15, calculate_delay_duration_in_seconds('This is a test'))

    def test_strings_with_leading_and_trailing_spaces(self):
        self.assertEqual(4 / 15, calculate_delay_duration_in_seconds('  This is a test  '))

    def test_strings_with_multiple_spaces_between_words(self):
        self.assertEqual(4 / 15, calculate_delay_duration_in_seconds('This  is  a  test'))

    def test_max_duration(self):
        self.assertEqual(2, calculate_delay_duration_in_seconds('word ' * 45))
