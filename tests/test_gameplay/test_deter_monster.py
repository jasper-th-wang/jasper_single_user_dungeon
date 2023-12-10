from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from gameplay.monster import deter_monster, WISDOM_INCREMENT


class TestDeterMonster(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_deter_monster(self, mock_stdout, __):
        character = {"Wisdom": 0}
        deter_monster(character)
        self.assertEqual(character["Wisdom"], WISDOM_INCREMENT)
        self.assertIn("You successfully deterred the monster!", mock_stdout.getvalue())
        self.assertIn(f"You gained {WISDOM_INCREMENT} Wisdom!", mock_stdout.getvalue())

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_deter_monster_with_existing_wisdom(self, mock_stdout, __):
        character = {"Wisdom": 5}
        deter_monster(character)
        self.assertEqual(character["Wisdom"], 5 + WISDOM_INCREMENT)
        self.assertIn("You successfully deterred the monster!", mock_stdout.getvalue())
        self.assertIn(f"You gained {WISDOM_INCREMENT} Wisdom!", mock_stdout.getvalue())
