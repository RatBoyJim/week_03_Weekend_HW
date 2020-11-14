from flask import render_template, request, redirect
from app import app
from app.models.players import *
from app.models.player import *
from app.models.game import *
import app.repositories.player_repository as player_repository

@app.route('/')
def index():
    return render_template('index.html', title='RPS', players=players)

@app.route("/pvp/new", methods=["GET"])
def new_game():
    players = player_repository.select_all()
    return render_template('playervplayer.html', players = players)

@app.route('/pvp', methods = ["POST"])
def player_v_player():
    name1 = request.form['name1']
    name2 = request.form['name2']
    choice1 = request.form['choice1']
    choice2 = request.form['choice2']
    player1 = Player(name1, choice1)
    player2 = Player(name2, choice2)
    play_game = Game.play_game_2(player1, player2)
    return render_template('pvpresult.html', player1 = player1, player2 = player2, title='PvP', winner=play_game)

@app.route('/playvcompy')
def playvcompy():
    return render_template('playvcompy.html', title='RPS')

@app.route('/player1')
def player1_choice():
    players = player_repository.select_all()
    return render_template('player1.html', title='RPS', players = players)

@app.route('/player1/rock')
def player2_choice_p1r():
    return render_template('player1rock.html', title='RPS')

@app.route('/player1/paper')
def player2_choice_p1p():
    return render_template('player1paper.html', title='RPS')

@app.route('/player1/scissors')
def player2_choice_p1s():
    return render_template('player1scissors.html', title='RPS')

@app.route('/player1/<choice1>/<choice2>')
def result(choice1, choice2):
    if choice1 == 'rock':
        choice_1 = 'Rock'
    elif choice1 == 'paper':
        choice_1 = 'Paper'
    elif choice1 == 'scissors':
        choice_1 = 'Scissors'
    if choice2 == 'scissors':
        choice_2 = 'Scissors'
    elif choice2 == 'rock':
        choice_2 = 'Rock'
    elif choice2 == 'paper':
        choice_2 = 'Paper'
    player1 = Player(name="Player 1", choice=choice_1)
    player2 = Player(name="Player 2", choice=choice_2)
    play_game = Game.play_game(player1, player2)
    return render_template('results.html', title='RPS', winner=play_game)


@app.route('/player1/<choice1>/compy')
def play_compy(choice1):
    if choice1 == 'rock':
        choice_1 = 'Rock'
    elif choice1 == 'paper':
        choice_1 = 'Paper'
    elif choice1 == 'scissors':
        choice_1 = 'Scissors'
    compy = Game.play_compy()
    player1 = Player("Player 1", choice=choice_1)
    player2 = compy
    play_game = Game.play_game_2(player1, player2)
    return render_template('compy_results.html', title='RPS', winner=play_game, player1=player1, player2=player2)
