from unittest import TestCase

from dialogues import parse_yarn_content

# from unittest.mock import patch


class TestParseYarnContent(TestCase):
    def test_no_options(self):
        line_list = [
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once.",
        ]
        expected = [
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once.",
        ]

        actual = parse_yarn_content(line_list)

        self.assertEqual(expected, actual)

    def test_options_with_one_line_content(self):
        line_list = [
            "-> Take a deep breath",
            "    The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries.",
        ]
        expected = [
            [
                {
                    "option": "Take a deep breath",
                    "content": [
                        "The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries."
                    ],
                },
            ]
        ]

        actual = parse_yarn_content(line_list)
        self.assertEqual(expected, actual)

    def test_two_options_with_one_line_content(self):
        line_list = [
            "-> Take a deep breath",
            "    The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries.",
            "-> Sit up and stretch",
            "    You sit up, your hands brushing against a cold, damp ground that seems to be made of stone, yet oddly smooth, like polished marble left neglected for ages.",
        ]
        expected = [
            [
                {
                    "option": "Take a deep breath",
                    "content": [
                        "The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries."
                    ],
                },
                {
                    "option": "Sit up and stretch",
                    "content": [
                        "You sit up, your hands brushing against a cold, damp ground that seems to be made of stone, yet oddly smooth, like polished marble left neglected for ages."
                    ],
                },
            ]
        ]

        actual = parse_yarn_content(line_list)
        self.assertEqual(expected, actual)

    def test_two_options_followed_by_normal_line(self):
        line_list = [
            "-> Take a deep breath",
            "    The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries.",
            "-> Sit up and stretch",
            "    You sit up, your hands brushing against a cold, damp ground that seems to be made of stone, yet oddly smooth, like polished marble left neglected for ages.",
            "Tall, imposing columns rise to a ceiling lost in darkness, carved with intricate designs that seem to shift and move in the corner of your eye. ",
        ]
        expected = [
            [
                {
                    "option": "Take a deep breath",
                    "content": [
                        "The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries."
                    ],
                },
                {
                    "option": "Sit up and stretch",
                    "content": [
                        "You sit up, your hands brushing against a cold, damp ground that seems to be made of stone, yet oddly smooth, like polished marble left neglected for ages."
                    ],
                },
            ],
            "Tall, imposing columns rise to a ceiling lost in darkness, carved with intricate designs that seem to shift and move in the corner of your eye.",
        ]

        actual = parse_yarn_content(line_list)
        self.assertEqual(expected, actual)

    def test_options_between_normal_lines(self):
        line_list = [
            "You slowly come to, a chilling sense of unease creeping over you. ",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once. ",
            "-> Take a deep breath",
            "    The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries.",
            "-> Sit up and stretch",
            "    You sit up, your hands brushing against a cold, damp ground that seems to be made of stone, yet oddly smooth, like polished marble left neglected for ages.",
            "Tall, imposing columns rise to a ceiling lost in darkness, carved with intricate designs that seem to shift and move in the corner of your eye. ",
        ]
        expected = [
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once.",
            [
                {
                    "option": "Take a deep breath",
                    "content": [
                        "The air is thick, tinged with a mustiness that feels ancient, as if it has been stagnant for centuries."
                    ],
                },
                {
                    "option": "Sit up and stretch",
                    "content": [
                        "You sit up, your hands brushing against a cold, damp ground that seems to be made of stone, yet oddly smooth, like polished marble left neglected for ages."
                    ],
                },
            ],
            "Tall, imposing columns rise to a ceiling lost in darkness, carved with intricate designs that seem to shift and move in the corner of your eye.",
        ]