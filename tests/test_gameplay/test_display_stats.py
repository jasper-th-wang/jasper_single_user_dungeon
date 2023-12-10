from unittest import TestCase
from unittest.mock import patch
import io
from gameplay.character import display_stats


class TestDisplayStats(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats(self, mock_output):
        character = {'Essence': 10, 'Max Essence': 100, 'Wisdom': 20, "Fury": 20, 'Quest': 'Find the treasure'}
        expected_output = (
            "Current Quest: Find the treasure\n"
            "+-------------------+\n"
            "|    Player Stats   |\n"
            "+-------------------+\n"
            "| Essence: 10/100   |\n"
            "| Wisdom: 20        |\n"
            "| Fury: 20          |\n"
            "+-------------------+\n"
            "| Actions:          |\n"
            "| W - Go North      |\n"
            "| A - Go West       |\n"
            "| S - Go South      |\n"
            "| D - Go East       |\n"
            "| ! - See Stats     |\n"
            "+-------------------+\n"
        )
        display_stats(character)
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_essence_zero(self, mock_output):
        character = {'Essence': 0, 'Max Essence': 100, 'Wisdom': 20, 'Fury': 20, 'Quest': 'Find the treasure'}
        expected_output = (
            "Current Quest: Find the treasure\n"
            "+-------------------+\n"
            "|    Player Stats   |\n"
            "+-------------------+\n"
            "| Essence: 0/100    |\n"
            "| Wisdom: 20        |\n"
            "| Fury: 20          |\n"
            "+-------------------+\n"
            "| Actions:          |\n"
            "| W - Go North      |\n"
            "| A - Go West       |\n"
            "| S - Go South      |\n"
            "| D - Go East       |\n"
            "| ! - See Stats     |\n"
            "+-------------------+\n"
        )
        display_stats(character)
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wisdom_and_fury_thousand(self, mock_output):
        character = {'Essence': 10, 'Max Essence': 100, 'Wisdom': 1000, 'Fury': 1000, 'Quest': 'Find the treasure'}
        expected_output = (
            "Current Quest: Find the treasure\n"
            "+-------------------+\n"
            "|    Player Stats   |\n"
            "+-------------------+\n"
            "| Essence: 10/100   |\n"
            "| Wisdom: 1000      |\n"
            "| Fury: 1000        |\n"
            "+-------------------+\n"
            "| Actions:          |\n"
            "| W - Go North      |\n"
            "| A - Go West       |\n"
            "| S - Go South      |\n"
            "| D - Go East       |\n"
            "| ! - See Stats     |\n"
            "+-------------------+\n"
        )
        display_stats(character)
        self.assertEqual(mock_output.getvalue(), expected_output)
