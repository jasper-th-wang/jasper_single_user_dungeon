from unittest import TestCase

from narrative.dialogue import make_stats_change_message


class TestMakeStatsChangeMessage(TestCase):
    def test_make_stats_change_message_essence(self):
        self.assertEqual(make_stats_change_message("++E"), "<< You lost 5 Essence >>")

    def test_make_stats_change_message_wisdom(self):
        self.assertEqual(make_stats_change_message("++W"), "<< You gained 5 Wisdom >>")

    def test_make_stats_change_message_fury(self):
        self.assertEqual(make_stats_change_message("++F"), "<< You gained 5 Fury >>")

    def test_make_stats_change_message_no_change(self):
        self.assertEqual(make_stats_change_message("++X"), None)
