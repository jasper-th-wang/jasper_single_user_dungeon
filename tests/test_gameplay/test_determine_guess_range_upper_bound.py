from unittest import TestCase
from gameplay.monster import determine_guess_range_upper_bound


class TestDetermineGuessRangeUpperBound(TestCase):
    def test_upper_bound_above_100(self):
        self.assertEqual(1, determine_guess_range_upper_bound(101))

    def test_upper_bound_above_50(self):
        self.assertEqual(2, determine_guess_range_upper_bound(51))

    def test_upper_bound_above_30(self):
        self.assertEqual(3, determine_guess_range_upper_bound(31))

    def test_upper_bound_below_30(self):
        self.assertEqual(5, determine_guess_range_upper_bound(29))

    def test_upper_bound_at_100(self):
        self.assertEqual(2, determine_guess_range_upper_bound(100))

    def test_upper_bound_at_50(self):
        self.assertEqual(3, determine_guess_range_upper_bound(50))

    def test_upper_bound_at_30(self):
        self.assertEqual(5, determine_guess_range_upper_bound(30))
