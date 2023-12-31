"""
ADD A DOCSTRING
"""
import io
from unittest import TestCase
from unittest.mock import patch
from narrative.options import render_options_menu


class TestRenderOptionsMenu(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_options_menu_with_one_option(self, mock_stdout):
        options_list = [{"option": "Option 1"}]
        render_options_menu(options_list)
        self.assertEqual("1: Option 1\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_options_menu_with_multiple_options(self, mock_stdout):
        options_list = [{"option": "Option 1"}, {"option": "Option 2"}, {"option": "Option 3"}]
        render_options_menu(options_list)
        self.assertEqual("1: Option 1\n2: Option 2\n3: Option 3\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_options_menu_with_long_option_text(self, mock_stdout):
        options_list = [{"option": "This is a very long option text that should be printed correctly"}]
        render_options_menu(options_list)
        self.assertEqual("1: This is a very long option text that should be printed correctly\n", mock_stdout.getvalue())

    def test_raises_type_error_if_options_list_not_list(self):
        options_list = "not a list"
        with self.assertRaises(TypeError):
            render_options_menu(options_list)

    def test_raises_value_error_if_options_list_empty(self):
        options_list = []
        with self.assertRaises(ValueError):
            render_options_menu(options_list)

    def test_raises_type_error_if_options_list_contains_non_dictionary_elements(self):
        options_list = ["not a dictionary"]
        with self.assertRaises(TypeError):
            render_options_menu(options_list)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_render_options_menu_with_whitespace_characters(self, mock_stdout):
        options_list = [
            {"option": "Option 1"},
            {"option": "Option 2"},
            {"option": "Option 3"},
        ]
        expected_output = "1: Option 1\n2: Option 2\n3: Option 3\n"
        render_options_menu(options_list)
        self.assertEqual(expected_output, mock_stdout.getvalue())
