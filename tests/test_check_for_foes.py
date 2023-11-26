from unittest import TestCase
from unittest.mock import patch

from simple_game import check_for_foes


class Test(TestCase):
    @patch('random.randint', return_value=0)
    def test_there_is_foe(self, _):
        self.assertTrue(check_for_foes())

    @patch('random.randint', return_value=2)
    def test_there_is_no_foe(self, _):
        self.assertFalse(check_for_foes())
