from unittest import TestCase
from gameplay.character import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        character = make_character()
        self.assertIsInstance(character, dict)
        self.assertEqual(0, character["X-coordinate"])
        self.assertEqual(0, character["Y-coordinate"])
        self.assertEqual(100, character["Essence"])
        self.assertEqual(100, character["Max Essence"])
        self.assertEqual(5, character["Wisdom"])
        self.assertEqual(5, character["Fury"])
        self.assertIsNone(character["Quest"])
