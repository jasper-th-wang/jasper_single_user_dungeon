from unittest import TestCase

from narrative.dialogue import make_stats_change_message


class TestMakeStatsChangeMessage(TestCase):
    def test_make_stats_change_message_essence(self):
        self.assertEqual("!<< You lost 5 Essence >>", make_stats_change_message("++E"))

    def test_make_stats_change_message_wisdom(self):
        self.assertEqual("$<< You gained 5 Wisdom >>", make_stats_change_message("++W"))

    def test_make_stats_change_message_fury(self):
        self.assertEqual("!<< You gained 5 Fury >>", make_stats_change_message("++F"))

    def test_make_stats_change_message_no_change(self):
        self.assertEqual(make_stats_change_message("++X"), None)
