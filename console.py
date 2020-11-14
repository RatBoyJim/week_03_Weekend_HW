from app.models.player import Player


import app.repositories.player_repository as player_repository

player_repository.delete_all()


player1 = Player("Michael", "Rock", 0, 0, 0)
player_repository.save(player1)
player2 = Player("Marie", "Paper", 0, 0, 0)
player_repository.save(player2)
player3 = Player("Joseph", "Scissors", 0, 0, 0)
player_repository.save(player3)

player_repository.select_all()