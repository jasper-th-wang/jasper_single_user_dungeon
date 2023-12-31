from unittest import TestCase
from gameplay.character import is_alive


class Test(TestCase):
    def test_character_is_alive(self):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Essence": 3}
        self.assertTrue(is_alive(character))

    def test_character_is_dead(self):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Essence": 0}
        self.assertFalse(is_alive(character))
