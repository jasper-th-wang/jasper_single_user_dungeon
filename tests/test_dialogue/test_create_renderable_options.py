from unittest import TestCase
from narrative.dialogue import create_renderable_options


class TestCreateRenderableOptions(TestCase):
    def test_list_of_option_lines_with_single_dialogue_line_each(self):
        option_lines = [
            "-> Option 1",
            "    Dialogue line 1",
            "-> Option 2",
            "    Dialogue line 2",
        ]
        expected = [
            {"option": "Option 1", "dialogues": ["Dialogue line 1"], 'terminating': False},
            {"option": "Option 2", "dialogues": ["Dialogue line 2"], 'terminating': False},
        ]

        actual = create_renderable_options(option_lines)
        self.assertEqual(expected, actual)

    def test_list_of_option_lines_with_multiple_dialogue_lines_each(self):
        option_lines = [
            "-> Option 1",
            "    Dialogue line 1",
            "    Dialogue line 2",
            "-> Option 2",
            "    Dialogue line 3",
            "    Dialogue line 4",
        ]
        expected = [
            {"option": "Option 1", "dialogues": ["Dialogue line 1", "Dialogue line 2"], 'terminating': False},
            {"option": "Option 2", "dialogues": ["Dialogue line 3", "Dialogue line 4"], 'terminating': False},
        ]

        actual = create_renderable_options(option_lines)
        self.assertEqual(expected, actual)

    def test_list_of_option_lines_with_mixed_terminating_and_non_terminating_options(self):
        option_lines = [
            "-> Option 1",
            "    Dialogue line 1",
            "-> $Exit",
            "-> Option 2",
            "    Dialogue line 2",
        ]
        expected = [
            {"option": "Option 1", "dialogues": ["Dialogue line 1"], 'terminating': False},
            {"option": "Exit", "dialogues": [], 'terminating': True},
            {"option": "Option 2", "dialogues": ["Dialogue line 2"], 'terminating': False},
        ]

        actual = create_renderable_options(option_lines)
        self.assertEqual(expected, actual)

    def test_list_of_option_lines_with_terminating_options(self):
        option_lines = [
            "-> $Exit",
            "-> $Restart",
        ]
        expected = [
            {"option": "Exit", "dialogues": [], 'terminating': True},
            {"option": "Restart", "dialogues": [], 'terminating': True},
        ]

        actual = create_renderable_options(option_lines)
        self.assertEqual(expected, actual)

    def test_empty_list(self):
        option_lines = []
        expected = []
        actual = create_renderable_options(option_lines)
        self.assertEqual(expected, actual)
