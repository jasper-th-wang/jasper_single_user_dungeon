from unittest import TestCase
from unittest.mock import patch

from game_utils.handle_input import process_users_action


class TestProcessUsersAction(TestCase):
    @patch('game_utils.handle_input.get_valid_user_input', return_value='W')
    def test_non_exclamation_input(self, mock_input):
        result = process_users_action({})
        self.assertEqual(result, 'W')

    @patch('game_utils.handle_input.get_valid_user_input', side_effect=['!', 'W'])
    @patch('game_utils.handle_input.character.display_stats')
    def test_exclamation_input(self, mock_display_stats, mock_input):
        result = process_users_action({})
        mock_display_stats.assert_called_once()
        self.assertEqual(result, 'W')
