from unittest import TestCase

from game_utils.render_text import process_text_color, TEXT_COLORS


class TestProcessTextColor(TestCase):
    def test_normal(self):
        self.assertEqual(f"{TEXT_COLORS['NORMAL']}Hello{TEXT_COLORS['NORMAL']}", process_text_color('Hello'))

    def test_player(self):
        self.assertEqual(f"{TEXT_COLORS['PLAYER']}Hello{TEXT_COLORS['NORMAL']}", process_text_color('$Hello'))

    def test_npc(self):
        self.assertEqual(f"{TEXT_COLORS['NPC']}Hello{TEXT_COLORS['NORMAL']}", process_text_color('@Hello'))

    def test_yellow(self):
        self.assertEqual(f"{TEXT_COLORS['YELLOW']}Hello{TEXT_COLORS['NORMAL']}", process_text_color('!Hello'))

    def test_empty_string(self):
        self.assertEqual(f"{TEXT_COLORS['NORMAL']}{TEXT_COLORS['NORMAL']}", process_text_color(''))
