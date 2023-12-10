from unittest import TestCase

from gameplay.character import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_check_if_goal_attained_true(self):
        character = {'Quest': 'Complete'}
        self.assertTrue(check_if_goal_attained(character))

    def test_check_if_goal_attained_false(self):
        character = {'Quest': 'Find the treasure'}
        self.assertFalse(check_if_goal_attained(character))
