from unittest import TestCase
from simple_game import scenario_descriptions


class Test(TestCase):
    def test_scenario_descriptions(self):
        expected = [
            "The Server Room Labyrinth",
            "The Library of Obsolete Languages",
            "The Cafeteria of Constant Cravings",
            "The Printer Paper Jam Dungeon",
            "The WiFi Woods",
            "The Echo Hall of Helpdesk Calls",
            "The Lost USB Mines",
            "The Classroom of Endless Lectures",
            "The Firewall Fortress",
            "The Recursive Room"
        ]
        self.assertEqual(expected, scenario_descriptions())
