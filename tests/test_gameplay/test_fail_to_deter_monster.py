from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from gameplay.monster import fail_to_deter_monster, ESSENCE_DECREMENT


class TestFailToDeterMonster(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_fail_to_deter_monster(self, mock_stdout, __):
        character = {"Essence": 10}
        monster = "Ghost"
        fail_to_deter_monster(monster, character)
        self.assertEqual(character["Essence"], 10 - ESSENCE_DECREMENT)
        self.assertIn("You failed, the Ghost attacked you and ran away.", mock_stdout.getvalue())
        self.assertIn(f"You just lost {ESSENCE_DECREMENT} Essence Point", mock_stdout.getvalue())

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_fail_to_deter_monster_with_no_essence(self, mock_stdout, __):
        character = {"Essence": 0}
        monster = "Ghost"
        fail_to_deter_monster(monster, character)
        self.assertEqual(character["Essence"], -ESSENCE_DECREMENT)
        self.assertIn("You failed, the Ghost attacked you and ran away.", mock_stdout.getvalue())
        self.assertIn(f"You just lost {ESSENCE_DECREMENT} Essence Point", mock_stdout.getvalue())
