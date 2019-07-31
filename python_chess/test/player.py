import unittest
from src.player import Player, new_players

class TestPlayer(unittest.TestCase):

    def test_player_inherits_props(self):
        mockProps = { 'one': 1, 'two': 2 }
        mockPlayer = Player(mockProps)
        self.assertEqual(mockPlayer.one, 1)
        self.assertEqual(mockPlayer.two, 2)

    def test_player_moves(self):
        mockProps = { 'history': [] }
        mockPlayer = Player(mockProps)
        mockPlayer.move(1)
        mockPlayer.move(2)
        self.assertEqual(len(mockPlayer.history), 2)
        self.assertEqual(mockPlayer.history[0], 1)
        self.assertEqual(mockPlayer.history[1], 2)

    def test_summon_new_players(self):
        mockPlayers = new_players(['blah', 'bleh'])
        self.assertEqual(mockPlayers[0].color, 'blah')
        self.assertEqual(mockPlayers[1].color, 'bleh')
