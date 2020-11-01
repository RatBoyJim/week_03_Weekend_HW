from flask import render_template, request, redirect
from app import app
from app.models.players import *
from app.models.player import *
from app.models.game import *

@app.route('/')
def index():
    return render_template('index.html', title='RPS', players=players)

# @app.route('/rock/scissors', methods=['GET', 'POST'])
# def player_v_player():
#     # name1 = request.form['name1']
#     # name2 = request.form['name2']
#     # choice1 = request.form['choice1']
#     # choice2 = request.form['choice2']
#     player1 = Player(name="Michael", choice="Rock")
#     player2 = Player(name="Marie", choice="Scissors")
#     play_game = Game.play_game(player1, player2)
#     return render_template('playervplayer.html', title='PvP', winner=play_game)


@app.route('/player1')
def player1_choice():
    return render_template('player1.html', title='Player 1')

@app.route('/player1/rock')
def player2_choice_p1r():
    return render_template('player1rock.html', title='Player 2')

@app.route('/player1/paper')
def player2_choice_p1p():
    return render_template('player1paper.html', title='Player 2')

@app.route('/player1/scissors')
def player2_choice_p1s():
    return render_template('player1scissors.html', title='Player 2')

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
    player1 = Player(name="Michael", choice=choice_1)
    player2 = Player(name="Marie", choice=choice_2)
    play_game = Game.play_game(player1, player2)
    return render_template('results.html', title='Results', winner=play_game)

