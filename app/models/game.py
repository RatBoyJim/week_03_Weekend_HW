import random

from app.models.player import Player

class Game():
    def play_game(player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Scissors":
            return f"{player_1.name} is the winner because {player_1.choice} smashes {player_2.choice}"
        elif player_1.choice == "Paper" and player_2.choice == "Rock":
            return f"{player_1.name} is the winner because {player_1.choice} covers {player_2.choice}"
        elif player_1.choice == "Scissors" and player_2.choice == "Paper":
            return f"{player_1.name} is the winner because {player_1.choice} cuts {player_2.choice}"
        elif player_1.choice == "Scissors" and player_2.choice == "Rock":
            return f"{player_2.name} is the winner because {player_2.choice} smashes {player_1.choice}"
        elif player_1.choice == "Rock" and player_2.choice == "Paper":
            return f"{player_2.name} is the winner because {player_2.choice} covers {player_1.choice}"
        elif player_1.choice == "Paper" and player_2.choice == "Scissors":
            return f"{player_2.name} is the winner because {player_2.choice} cuts {player_1.choice}"
        elif player_1.choice == player_2.choice:
            return "It's a draw!"

    def play_game_2(player1, player2):
        if player1.choice == player2.choice:
            return None
        elif player1.choice == "Rock" and player2.choice == "Scissors":
            player1.won += 1
            return player1
        elif player1.choice == "Scissors" and player2.choice == "Paper":
            player1.won += 1
            return player1
        elif player1.choice == "Paper" and player2.choice == "Rock":
            player1.won += 1
            return player1
        else:
            player2.won += 1
            return player2
        

    def play_compy():
        all_moves = ["Rock", "Paper", "Scissors"]
        compy_choice = random.choice(all_moves)
        compy = Player("Compy", compy_choice)
        return compy




        