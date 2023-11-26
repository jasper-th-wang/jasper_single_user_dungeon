from unittest import TestCase
from simple_game import is_alive


class Test(TestCase):
    def test_character_is_alive(self):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}
        self.assertTrue(is_alive(character))

    def test_character_is_dead(self):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 0}
        self.assertFalse(is_alive(character))
