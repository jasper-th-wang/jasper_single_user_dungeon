import io
from unittest import TestCase
from unittest.mock import patch

from gameplay.handle_input import process_users_action


class Test(TestCase):
    @patch("builtins.input", return_value="1")
    def test_valid_input(self, _):
        actual = process_users_action()
        expected = 1
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["5", "1"])
    def test_invalid_number_input(self, _):
        actual = process_users_action()
        expected = 1
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["a", "1"])
    def test_invalid_string_input(self, _):
        actual = process_users_action()
        expected = 1
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["a", "1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_error_message_invalid_input(self, mock_output, _):
        process_users_action()
        printed_message = mock_output.getvalue()
        expected = "Invalid entry, please enter either 1 for north, 2 for south, 3: east or 4: west.\n"

        self.assertIn(expected, printed_message)

    @patch("builtins.input", return_value="1")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_error_message_invalid_input(self, mock_output, _):
        process_users_action()
        printed_message = mock_output.getvalue()
        expected = "Invalid entry, please enter either 1 for north, 2 for south, 3: east or 4: west.\n"

        self.assertNotIn(expected, printed_message)
