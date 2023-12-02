from unittest import TestCase

from narrative.dialogue import initialize_each_option


class TestInitializeEachOption(TestCase):
    def test_initializes_option_with_terminating_flag(self):
        options_list = []
        option_line = "-> $Option"
        initialize_each_option(options_list, option_line)
        expected = [{"option": "Option", "terminating": True, "dialogues": []}]
        self.assertEqual(expected, options_list)

    def test_adds_initialized_option_to_list(self):
        options_list = []
        option_line = "-> Option"
        initialize_each_option(options_list, option_line)
        expected = [{"option": "Option", "terminating": False, "dialogues": []}]
        self.assertEqual(expected, options_list)

    def test_append_terminating_option_to_existing_options(self):
        options_list = [
            {"option": "Option 1", "terminating": False, "dialogues": []},
            {"option": "Option 2", "terminating": False, "dialogues": []},
        ]
        option_line = "-> $Option 3"
        expected_options_list = [
            {"option": "Option 1", "terminating": False, "dialogues": []},
            {"option": "Option 2", "terminating": False, "dialogues": []},
            {"option": "Option 3", "terminating": True, "dialogues": []},
        ]

        initialize_each_option(options_list, option_line)

        self.assertEqual(options_list, expected_options_list)

    def test_append_option_to_list_with_terminating_option(self):
        options_list = [
            {"option": "Option 1", "terminating": True, "dialogues": []},
            {"option": "Option 2", "terminating": False, "dialogues": []},
        ]
        option_line = "-> Option 3"

        initialize_each_option(options_list, option_line)

        expected_options_list = [
            {"option": "Option 1", "terminating": True, "dialogues": []},
            {"option": "Option 2", "terminating": False, "dialogues": []},
            {"option": "Option 3", "terminating": False, "dialogues": []},
        ]
        self.assertEqual(options_list, expected_options_list)

    def test_raises_value_error_if_option_name_is_empty(self):
        options_list = []
        option_line = "-> "
        with self.assertRaises(ValueError):
            initialize_each_option(options_list, option_line)

