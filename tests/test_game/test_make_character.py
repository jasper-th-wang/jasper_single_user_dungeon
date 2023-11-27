from unittest import TestCase
from game import make_character


class Test(TestCase):
    def test_make_character(self):
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(expected, make_character())
