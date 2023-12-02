"""
ADD A DOCSTRING
"""
from unittest import TestCase
from narrative.dialogue import build_renderable_dialogue_list


class TestBuildRenderableDialogueList(TestCase):
    def test_only_dialogue_lines(self):
        dialogue_content = [
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once."
        ]
        expected = [
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once."
        ]

        actual = build_renderable_dialogue_list(dialogue_content)

        self.assertEqual(expected, actual)

    #  Should handle dialogue content with only options
    def test_only_options(self):
        dialogue_content = [
            "-> Option 1",
            "    Dialogue line 1",
            "-> Option 2",
            "    Dialogue line 2"
        ]
        expected = [
            [
                {
                    "option": "Option 1",
                    "terminating": False,
                    "dialogues": ["Dialogue line 1"]
                },
                {
                    "option": "Option 2",
                    "terminating": False,
                    "dialogues": ["Dialogue line 2"]
                }
            ]
        ]

        actual = build_renderable_dialogue_list(dialogue_content)

        self.assertEqual(expected, actual)

    def test_dialogue_lines_preceding_options(self):
        dialogue_content = [
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once.",
            "-> Option 1",
            "    Dialogue line 1",
            "-> Option 2",
            "    Dialogue line 2"
        ]
        expected = [
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once.",
            [
                {
                    "option": "Option 1",
                    "terminating": False,
                    "dialogues": [
                        "Dialogue line 1"
                    ]
                },
                {
                    "option": "Option 2",
                    "terminating": False,
                    "dialogues": [
                        "Dialogue line 2"
                    ]
                }
            ]
        ]

        actual = build_renderable_dialogue_list(dialogue_content)
        self.assertEqual(expected, actual)

    def test_dialogue_line_following_options(self):
        dialogue_content = [
            "Dialogue line 1",
            "-> Option 1",
            "    Dialogue line 2",
            "-> Option 2",
            "    Dialogue line 3",
            "Dialogue line 4"
        ]
        expected = [
            "Dialogue line 1",
            [
                {
                    "option": "Option 1",
                    "terminating": False,
                    "dialogues": ["Dialogue line 2"]
                },
                {
                    "option": "Option 2",
                    "terminating": False,
                    "dialogues": ["Dialogue line 3"]
                }
            ],
            "Dialogue line 4"
        ]

        actual = build_renderable_dialogue_list(dialogue_content)

        self.assertEqual(expected, actual)

    def test_dialogue_lines_preceding_and_following_options(self):
        dialogue_content = [
            "Dialogue line 1",
            "-> Option 1",
            "    Dialogue line 2",
            "-> Option 2",
            "    Dialogue line 3",
            "Dialogue line 4"
        ]
        expected = [
            "Dialogue line 1",
            [
                {
                    "option": "Option 1",
                    "terminating": False,
                    "dialogues": ["Dialogue line 2"]
                },
                {
                    "option": "Option 2",
                    "terminating": False,
                    "dialogues": ["Dialogue line 3"]
                }
            ],
            "Dialogue line 4"
        ]

        actual = build_renderable_dialogue_list(dialogue_content)

        self.assertEqual(expected, actual)

    def test_return_empty_list_for_empty_dialogue_content(self):
        dialogue_content = []
        expected = []

        actual = build_renderable_dialogue_list(dialogue_content)

        self.assertEqual(expected, actual)

    #  Should handle dialogue content with only whitespace characters
    def test_handle_whitespace_dialogue_content(self):
        dialogue_content = ["    ", "  ", "\t\t"]
        expected = []

        actual = build_renderable_dialogue_list(dialogue_content)

        self.assertEqual(expected, actual)

    def test_handle_option_flag_dialogue_content(self):
        dialogue_content = ["-> ", "-> ", "-> "]
        expected = []

        actual = build_renderable_dialogue_list(dialogue_content)

        self.assertEqual(expected, actual)

    def test_handle_whitespace_and_option_flag_dialogue_content(self):
        dialogue_content = ["    ->", "  ->", "\t\t->"]
        expected = []

        actual = build_renderable_dialogue_list(dialogue_content)

        self.assertEqual(expected, actual)
