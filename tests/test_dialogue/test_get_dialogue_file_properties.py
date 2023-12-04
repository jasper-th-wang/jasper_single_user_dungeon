from unittest import TestCase
from narrative.dialogue import get_dialogue_file_properties


class TestGetDialogueFileProperties(TestCase):

    def test_handles_input_lines_with_multiple_properties_before_content_start_flag(self):
        lines = [
            "title: Test Dialogue",
            "author: John Doe",
            "option_type: multiple choice",
            "---",
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once."
        ]
        expected = {
            "title": "Test Dialogue",
            "author": "John Doe",
            "option_type": "multiple choice"
        }
        actual = get_dialogue_file_properties(lines)
        self.assertEqual(actual, expected)

    def test_handles_input_lines_with_only_one_property_before_content_start_flag(self):
        lines = [
            "title: Test Dialogue",
            "---",
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once."
        ]
        expected = {
            "title": "Test Dialogue"
        }
        actual = get_dialogue_file_properties(lines)
        self.assertEqual(actual, expected)

    def test_handles_input_lines_with_no_properties_before_content_start_flag(self):
        lines = [
            "---",
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once."
        ]
        expected = {}
        actual = get_dialogue_file_properties(lines)
        self.assertEqual(actual, expected)

    def test_raises_value_error_if_content_start_flag_not_found_in_input_lines(self):
        lines = [
            "title: Test Dialogue",
            "author: John Doe",
            "option_type: multiple choice",
            "You slowly come to, a chilling sense of unease creeping over you.",
            "Your eyes flutter open, met by an eerie, dim light that seems to emanate from nowhere and everywhere all at once."
        ]
        with self.assertRaises(ValueError):
            get_dialogue_file_properties(lines)
