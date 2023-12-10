from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from gameplay.monster import kill_monster, FURY_INCREMENT


class TestKillMonster(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_kill_monster(self, mock_stdout, __):
        character = {"Fury": 0}
        monster = "Ghost"
        kill_monster(monster, character)
        self.assertEqual(character["Fury"], FURY_INCREMENT)
        self.assertIn("You killed the Ghost ruthlessly. Though you are unharmed, you feel an anger inside brewing.",
                      mock_stdout.getvalue())
        self.assertIn(f"You gained {FURY_INCREMENT} Fury", mock_stdout.getvalue())

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_kill_monster_with_existing_fury(self, mock_stdout, __):
        character = {"Fury": 5}
        monster = "Ghost"
        kill_monster(monster, character)
        self.assertEqual(character["Fury"], 5 + FURY_INCREMENT)
        self.assertIn("You killed the Ghost ruthlessly. Though you are unharmed, you feel an anger inside brewing.",
                      mock_stdout.getvalue())
        self.assertIn(f"You gained {FURY_INCREMENT} Fury", mock_stdout.getvalue())
