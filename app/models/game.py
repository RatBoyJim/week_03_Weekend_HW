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
            return None




        