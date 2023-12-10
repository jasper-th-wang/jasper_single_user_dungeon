from unittest import TestCase

from narrative.dialogue import process_stats_change


class TestProcessStatsChange(TestCase):
    def test_change_essence(self):
        character = {'Essence': 100, 'Max Essence': 100, 'Wisdom': 30, 'Fury': 150, 'Quest': 'Demo Quest'}
        process_stats_change("++E", character)
        self.assertEqual(character['Essence'], 95)

    def test_change_wisdom(self):
        character = {'Essence': 100, 'Max Essence': 100, 'Wisdom': 30, 'Fury': 150, 'Quest': 'Demo Quest'}
        process_stats_change("++W", character)
        self.assertEqual(character['Wisdom'], 35)

    def test_change_fury(self):
        character = {'Essence': 100, 'Max Essence': 100, 'Wisdom': 30, 'Fury': 150, 'Quest': 'Demo Quest'}
        process_stats_change("++F", character)
        self.assertEqual(character['Fury'], 155)

    def test_no_change(self):
        character = {'Essence': 100, 'Max Essence': 100, 'Wisdom': 30, 'Fury': 150, 'Quest': 'Demo Quest'}
        process_stats_change("++X", character)
        self.assertEqual(character,
                         {'Essence': 100, 'Max Essence': 100, 'Wisdom': 30, 'Fury': 150, 'Quest': 'Demo Quest'})
