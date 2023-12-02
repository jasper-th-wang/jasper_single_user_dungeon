"""
ADD A DOCSTRING
"""
from unittest import TestCase

from narrative.dialogue import initialize_each_option


class TestInitializeEachOption(TestCase):

    def test_initializes_option_with_terminating_flag(self):
        options_list = []
        option_line = "-> $Option"
        initialize_each_option(options_list, option_line)
        expected = [{"option": "Option", "terminating": True}]
        self.assertEqual(expected, options_list)

    def test_adds_initialized_option_to_list(self):
        options_list = []
        option_line = "-> Option"
        initialize_each_option(options_list, option_line)
        expected = [{"option": "Option", "terminating": False}]
        self.assertEqual(expected, options_list)

    def test_handles_empty_option_name(self):
        options_list = []
        option_line = "-> "
        initialize_each_option(options_list, option_line)
        expected = [{"option": "", "terminating": False}]
        self.assertEqual(expected, options_list)

    def test_append_terminating_option_to_existing_options(self):
        options_list = [
            {"option": "Option 1", "terminating": False},
            {"option": "Option 2", "terminating": False}
        ]
        option_line = "-> $Option 3"
        expected_options_list = [
            {"option": "Option 1", "terminating": False},
            {"option": "Option 2", "terminating": False},
            {"option": "Option 3", "terminating": True}
        ]

        initialize_each_option(options_list, option_line)

        self.assertEqual(options_list, expected_options_list)

    def test_append_option_to_list_with_terminating_option(self):
        options_list = [
            {"option": "Option 1", "terminating": True},
            {"option": "Option 2", "terminating": False}
        ]
        option_line = "-> Option 3"

        initialize_each_option(options_list, option_line)

        expected_options_list = [
            {"option": "Option 1", "terminating": True},
            {"option": "Option 2", "terminating": False},
            {"option": "Option 3", "terminating": False}
        ]
        self.assertEqual(options_list, expected_options_list)
