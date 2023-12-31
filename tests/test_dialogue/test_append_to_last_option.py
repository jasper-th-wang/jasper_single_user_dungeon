from unittest import TestCase

from narrative.dialogue import append_to_last_option


class TestAppendToLastOption(TestCase):
    def test_appends_string_to_dialogues_list_with_single_option(self):
        options_list = [{"option": "Option 1", "dialogues": []}]
        expected = [{"option": "Option 1", "dialogues": ["New Dialogue"]}]

        option_line = "New Dialogue"
        append_to_last_option(options_list, option_line)

        self.assertEqual(expected, options_list)

    def test_appends_string_to_dialogues_list(self):
        options_list = [
            {"option": "Option 1", "dialogues": ["Dialogue 1"]},
            {"option": "Option 2", "dialogues": ["Dialogue 2"]},
        ]
        expected = [
            {"option": "Option 1", "dialogues": ["Dialogue 1"]},
            {"option": "Option 2", "dialogues": ["Dialogue 2", "New Dialogue"]},
        ]

        option_line = "New Dialogue"
        append_to_last_option(options_list, option_line)

        self.assertEqual(expected, options_list)

    def test_raises_value_error_when_options_list_is_empty(self):
        options_list = []
        option_line = "New Dialogue"

        with self.assertRaises(ValueError):
            append_to_last_option(options_list, option_line)
