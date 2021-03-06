import unittest

from app.models.game import *
from app.models.player import *

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Michael", "Rock", 0, 0, 0)
        self.player2 = Player("Mizzle", "Scissors", 0, 0, 0)

    def test_game_is_played__player1_wins_rock_beats_scissors(self):
        self.player1 = Player("Michael", "Rock",0 ,0, 0)
        self.player2 = Player("Mizzle", "Scissors", 0, 0, 0)
        self.assertEqual("Michael is the winner because Rock smashes Scissors", Game.play_game(self.player1, self.player2))

    def test_game_is_working__player2_wins_rock_beats_scissors(self):
        self.player1 = Player("Michael", "Scissors", 0, 0, 0)
        self.player2 = Player("Mizzle", "Rock", 0, 0, 0)
        self.assertEqual("Mizzle is the winner because Rock smashes Scissors", Game.play_game(self.player1, self.player2))

    def test_game_is_working__player2_wins_scissors_beats_paper(self):
        self.player1 = Player("Michael", "Paper", 0, 0, 0)
        self.player2 = Player("Mizzle", "Scissors", 0, 0, 0)
        self.assertEqual("Mizzle is the winner because Scissors cuts Paper", Game.play_game(self.player1, self.player2))

    def test_game_can_be_drawn(self):
        self.player1 = Player("Michael", "Paper", 0, 0, 0)
        self.player2 = Player("Mizzle", "Paper", 0, 0, 0)
        self.assertEqual(None, Game.play_game(self.player1, self.player2))

    

    