import json
from unittest import TestCase
from unittest.mock import patch, mock_open
from gameplay.level import get_game_level_info


class TestGetGameLevelInfo(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='{"level": 1}')
    @patch('json.load', return_value={"level": 1})
    def test_level_info_valid(self, _, __):
        result = get_game_level_info(1)
        self.assertEqual(result, {"level": 1})

    @patch('builtins.open', new_callable=mock_open, read_data='{"level": 1}')
    @patch('json.load')
    def test_level_info_file_not_found(self, mock_json_load, mock_file):
        mock_file.side_effect = FileNotFoundError
        result = get_game_level_info(9999)
        self.assertIsNone(result)

    @patch('builtins.open', new_callable=mock_open, read_data='{"level": 1}')
    @patch('json.load')
    def test_json_decode_error(self, mock_json_load, mock_file):
        mock_json_load.side_effect = json.JSONDecodeError('Error', doc='', pos=0)
        result = get_game_level_info(1)
        self.assertIsNone(result)
