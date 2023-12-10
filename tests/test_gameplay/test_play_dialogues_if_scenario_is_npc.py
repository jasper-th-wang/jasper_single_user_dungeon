from unittest import TestCase
from unittest.mock import patch
from gameplay.board import play_dialogues_if_scenario_is_npc


class TestPlayDialoguesIfScenarioIsNpc(TestCase):
    @patch('narrative.dialogue.play_dialogues_from_file_path')
    def test_if_scenario_is_npc_with_npc(self, mock_play_dialogues):
        scenario = {"dialogue_file_path": "some/path/to/dialogue.txt"}
        play_dialogues_if_scenario_is_npc(scenario)
        mock_play_dialogues.assert_called_once_with("some/path/to/dialogue.txt")

    @patch('narrative.dialogue.play_dialogues_from_file_path')
    def test_if_scenario_is_npc_with_empty_space(self, mock_play_dialogues):
        scenario = "An empty space"
        play_dialogues_if_scenario_is_npc(scenario)
        mock_play_dialogues.assert_not_called()

    @patch('narrative.dialogue.play_dialogues_from_file_path')
    def test_if_scenario_is_npc_with_npc_no_dialogue_file_path(self, mock_play_dialogues):
        scenario = {"other_key": "some value"}
        with self.assertRaises(KeyError):
            play_dialogues_if_scenario_is_npc(scenario)
