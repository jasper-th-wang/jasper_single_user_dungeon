import io
import textwrap
from unittest import TestCase
from unittest.mock import call, patch

from gameplay.board import render_ascii_map


class TestRenderAsciiMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_render_ascii_map_player_at_0_0(self, mock_output):
        board = {
            (0, 0): "some scene",
            (1, 0): {},
            (0, 1): "some scene",
            (1, 1): "some scene",
        }
        character_coordinates = (0, 0)
        expected = textwrap.dedent("""
                +---+---+
                | @   ! |
                |       |
                +---+---+
                """).lstrip()

        render_ascii_map(board, character_coordinates)
        printed_map = mock_output.getvalue()
        self.assertEqual(expected, printed_map)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_render_ascii_map_player_at_1_0(self, mock_output):
        board = {
            (0, 0): "some scene",
            (1, 0): "some scene",
            (0, 1): {},
            (1, 1): "some scene",
        }
        character_coordinates = (1, 0)
        expected = textwrap.dedent("""
                +---+---+
                |     @ |
                | !     |
                +---+---+
                """).lstrip()

        render_ascii_map(board, character_coordinates)
        printed_map = mock_output.getvalue()
        self.assertEqual(expected, printed_map)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_render_ascii_map_no_npc(self, mock_output):
        board = {
            (0, 0): 'some scene',
            (1, 0): 'some scene',
            (0, 1): 'some scene',
            (1, 1): 'some scene'
        }
        character_coordinates = (0, 0)
        expected = textwrap.dedent("""
              +---+---+
              | @     |
              |       |
              +---+---+
          """).lstrip()

        render_ascii_map(board, character_coordinates)
        printed_map = mock_output.getvalue()
        self.assertEqual(expected, printed_map)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_render_ascii_map_multiple_npc(self, mock_output):
        board = {
            (0, 0): {},
            (1, 0): {},
            (0, 1): 'some scene',
            (1, 1): 'some scene'
        }
        character_coordinates = (1, 1)
        expected = textwrap.dedent("""
              +---+---+
              | !   ! |
              |     @ |
              +---+---+
          """).lstrip()

        render_ascii_map(board, character_coordinates)
        printed_map = mock_output.getvalue()
        self.assertEqual(expected, printed_map)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_render_ascii_map_asymmetrical_map(self, mock_output):
        board = {
            (0, 0): 'some scene',
            (1, 0): {},
            (0, 1): 'some scene',
            (1, 1): 'some scene',
            (2, 0): 'some scene',
            (2, 1): {}
        }
        character_coordinates = (0, 0)
        expected = textwrap.dedent("""
              +---+---+---+
              | @   !     |
              |         ! |
              +---+---+---+
          """).lstrip()

        render_ascii_map(board, character_coordinates)
        printed_map = mock_output.getvalue()
        self.assertEqual(expected, printed_map)
