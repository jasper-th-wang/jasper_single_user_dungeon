import unittest
from unittest.mock import patch
from narrative.dialogue import render_dialogues, process_stats_change


class TestRenderDialogues(unittest.TestCase):
    @patch("narrative.dialogue.render_text.print_text_line")
    @patch("narrative.dialogue.make_stats_change_message", return_value="Stats changed")
    def test_render_dialogues_with_stats_change(
            self,
            mock_make_stats_change_message,
            mock_print_text_line,
    ):
        dialogues_dictionary = {
            "properties": {"title": "Hello, world!"},
            "dialogues": ["++E"],
        }
        character = {"Essence": 50}
        render_dialogues(dialogues_dictionary, character)
        process_stats_change("++E", character)
        mock_make_stats_change_message.assert_called_once_with("++E")
        mock_print_text_line.assert_called_once_with("Stats changed")
        self.assertLess(character["Essence"], 50)

    @patch("narrative.dialogue.render_text.print_text_line")
    def test_render_dialogues_with_string(self, mock_print_text_line):
        dialogues_dictionary = {
            "properties": {"title": "Hello, world!"},
            "dialogues": ["Hello, world!"],
        }
        render_dialogues(dialogues_dictionary, character={})
        mock_print_text_line.assert_called_once_with("Hello, world!")

    @patch("narrative.dialogue.options.play_options_interactions")
    def test_render_dialogues_with_options(self, mock_play_options_interactions):
        dialogues_dictionary = {
            "properties": {"character": {}, "option_type": "type"},
            "dialogues": [["Option 1", "Option 2"]],
        }
        render_dialogues(dialogues_dictionary, character={})
        mock_play_options_interactions.assert_called_once_with(
            ["Option 1", "Option 2"], "type"
        )
