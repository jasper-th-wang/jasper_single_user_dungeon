from unittest import TestCase
from gameplay.monster import determine_guess_range_upper_bound


class TestDetermineGuessRangeUpperBound(TestCase):
    def test_upper_bound_above_30(self):
        self.assertEqual(1, determine_guess_range_upper_bound(101))

    def test_upper_bound_above_20(self):
        self.assertEqual(2, determine_guess_range_upper_bound(23))

    def test_upper_bound_above_10(self):
        self.assertEqual(3, determine_guess_range_upper_bound(14))

    def test_upper_bound_below_10(self):
        self.assertEqual(5, determine_guess_range_upper_bound(5))

    def test_upper_bound_at_30(self):
        self.assertEqual(2, determine_guess_range_upper_bound(30))

    def test_upper_bound_at_20(self):
        self.assertEqual(3, determine_guess_range_upper_bound(20))

    def test_upper_bound_at_10(self):
        self.assertEqual(5, determine_guess_range_upper_bound(10))
