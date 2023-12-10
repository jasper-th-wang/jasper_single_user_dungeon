from unittest import TestCase
from unittest.mock import patch
from gameplay.level import generate_monster


class TestGenerateMonster(TestCase):
    @patch('gameplay.level.random.randint', return_value=0)
    def test_generate_monster_first(self, mock_randint):
        monster_list = [{"name": "Monster 1"}, {"name": "Monster 2"}, {"name": "Monster 3"}]
        self.assertEqual(generate_monster(monster_list), {"name": "Monster 1"})
        mock_randint.assert_called_once_with(0, len(monster_list) - 1)

    @patch('gameplay.level.random.randint', return_value=1)
    def test_generate_monster_middle(self, mock_randint):
        monster_list = [{"name": "Monster 1"}, {"name": "Monster 2"}, {"name": "Monster 3"}]
        self.assertEqual(generate_monster(monster_list), {"name": "Monster 2"})
        mock_randint.assert_called_once_with(0, len(monster_list) - 1)

    @patch('gameplay.level.random.randint', return_value=2)
    def test_generate_monster_last(self, mock_randint):
        monster_list = [{"name": "Monster 1"}, {"name": "Monster 2"}, {"name": "Monster 3"}]
        self.assertEqual(generate_monster(monster_list), {"name": "Monster 3"})
        mock_randint.assert_called_once_with(0, len(monster_list) - 1)
