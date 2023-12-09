from unittest import TestCase
from gameplay.character import check_if_goal_attained


class Test(TestCase):
    def test_character_did_not_reach_goal_coordinates(self):
        rows = 3
        columns = 3
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        self.assertFalse(check_if_goal_attained(rows, columns, character))

    def test_character_reach_goal_coordinates(self):
        rows = 3
        columns = 3
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
        self.assertTrue(check_if_goal_attained(rows, columns, character))

    def test_character_at_goal_column(self):
        rows = 3
        columns = 3
        character = {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 5}
        self.assertFalse(check_if_goal_attained(rows, columns, character))

    def test_character_at_goal_row(self):
        rows = 3
        columns = 3
        character = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 5}
        self.assertFalse(check_if_goal_attained(rows, columns, character))
