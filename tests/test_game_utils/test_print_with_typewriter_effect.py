from unittest import TestCase
from unittest.mock import patch, call
from game_utils.render_text import print_with_typewritter_effect


class TestPrintWithTypewritterEffect(TestCase):
    @patch('sys.stdout.write')
    @patch('time.sleep')
    def test_no_punctuation(self, mock_sleep, mock_write):
        print_with_typewritter_effect('test')
        mock_write.assert_has_calls([call('t'), call('e'), call('s'), call('t'), call('\n')])
        mock_sleep.assert_has_calls([call(0.01), call(0.01), call(0.01), call(0.01)])

    @patch('sys.stdout.write')
    @patch('time.sleep')
    def test_with_punctuation(self, mock_sleep, mock_write):
        print_with_typewritter_effect('test, test.')
        mock_write.assert_has_calls(
            [call('t'), call('e'), call('s'), call('t'), call(','), call(' '), call('t'), call('e'), call('s'),
             call('t'), call('.'), call('\n')])
        mock_sleep.assert_has_calls(
            [call(0.01), call(0.01), call(0.01), call(0.01), call(0.15), call(0.01) ,call(0.01), call(0.01), call(0.01), call(0.01),
             call(0.01), call(0.15), call(0.01)])

    @patch('sys.stdout.write')
    @patch('time.sleep')
    def test_empty_string(self, mock_sleep, mock_write):
        print_with_typewritter_effect('')
        mock_write.assert_has_calls([call('\n'), call('\n')])
        mock_sleep.assert_not_called()
