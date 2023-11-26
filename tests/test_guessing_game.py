import io
from unittest import TestCase
from unittest.mock import patch

from simple_game import guessing_game


class Test(TestCase):

    @patch('builtins.input', side_effect=["i am a string", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_error_message_for_invalid_input(self, mock_output, _):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}
        guessing_game(character)
        printed_value = mock_output.getvalue()
        expected = "Invalid entry, please enter a number between 1 and 5 inclusive: "
        self.assertIn(expected, printed_value)

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_error_message_for_valid_input(self, mock_output, _):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}
        guessing_game(character)
        printed_value = mock_output.getvalue()
        expected = "Invalid entry, please enter a number between 1 and 5 inclusive: "
        self.assertNotIn(expected, printed_value)

    @patch('random.randint', return_value=3)
    @patch('builtins.input', return_value="3")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_message_when_guess_correctly(self, mock_output, _, __):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}
        guessing_game(character)
        printed_value = mock_output.getvalue()
        expected = "You're right! You can go on with your adventure unscathed!"
        self.assertIn(expected, printed_value)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', return_value="3")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_message_when_guess_incorrectly(self, mock_output, _, __):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}
        guessing_game(character)
        printed_value = mock_output.getvalue()
        expected = "Wrong number! The number was 1 but you entered 3, you just lost 1 HP"
        self.assertIn(expected, printed_value)

    @patch('random.randint', return_value=3)
    @patch('builtins.input', return_value="3")
    def test_HP_when_guess_correctly(self, _, __):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}
        guessing_game(character)
        expected_HP = 3
        actual_HP = character["Current HP"]
        self.assertEqual(expected_HP, actual_HP)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', return_value="3")
    def test_HP_when_guess_incorrectly(self, _, __):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 3}
        guessing_game(character)
        expected_HP = 2
        actual_HP = character["Current HP"]
        self.assertEqual(expected_HP, actual_HP)
