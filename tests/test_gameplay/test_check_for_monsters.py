from unittest import TestCase
from unittest.mock import patch
from gameplay.level import check_for_monsters


class TestCheckForMonsters(TestCase):
    @patch('random.randint', return_value=0)
    def test_monster_found(self, mock_randint):
        mock_randint.return_value = 0
        self.assertTrue(check_for_monsters())

    @patch('random.randint', return_value=1)
    def test_monster_not_found(self, mock_randint):
        mock_randint.return_value = 1
        self.assertFalse(check_for_monsters())

    @patch('random.randint', return_value=2)
    def test_monster_not_found2(self, mock_randint):
        mock_randint.return_value = 2
        self.assertFalse(check_for_monsters())
