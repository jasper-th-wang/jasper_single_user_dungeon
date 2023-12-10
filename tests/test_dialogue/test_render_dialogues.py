import unittest
from unittest.mock import patch
from narrative.dialogue import render_dialogues


class TestRenderDialogues(unittest.TestCase):
    @patch('narrative.dialogue.render_text.print_text_line')
    @patch('narrative.dialogue.process_stats_change')
    @patch('narrative.dialogue.make_stats_change_message', return_value="Stats changed")
    def test_render_dialogues_with_stats_change(self, mock_make_stats_change_message, mock_process_stats_change,
                                                mock_print_text_line):
        dialogues_dictionary = {
            "properties": {"character": {}},
            "dialogues": ["++E"]
        }
        render_dialogues(dialogues_dictionary)
        mock_process_stats_change.assert_called_once_with("++E", {})
        mock_make_stats_change_message.assert_called_once_with("++E")
        mock_print_text_line.assert_called_once_with("Stats changed")

    @patch('narrative.dialogue.render_text.print_text_line')
    def test_render_dialogues_with_string(self, mock_print_text_line):
        dialogues_dictionary = {
            "properties": {"character": {}},
            "dialogues": ["Hello, world!"]
        }
        render_dialogues(dialogues_dictionary)
        mock_print_text_line.assert_called_once_with("Hello, world!")

    @patch('narrative.dialogue.options.play_options_interactions')
    def test_render_dialogues_with_options(self, mock_play_options_interactions):
        dialogues_dictionary = {
            "properties": {"character": {}, "option_type": "type"},
            "dialogues": [["Option 1", "Option 2"]]
        }
        render_dialogues(dialogues_dictionary)
        mock_play_options_interactions.assert_called_once_with(["Option 1", "Option 2"], "type")
