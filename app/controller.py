from flask import render_template, request, redirect
from app import app
from app.models.players import *
from app.models.player import *
from app.models.game import *

@app.route('/')
def index():
    return render_template('index.html', title='RPS', players=players)

@app.route('/rock/scissors', methods=['GET', 'POST'])
def player_v_player():
    # name1 = request.form['name1']
    # name2 = request.form['name2']
    # choice1 = request.form['choice1']
    # choice2 = request.form['choice2']
    player1 = Player(name="Michael", choice="Rock")
    player2 = Player(name="Marie", choice="Scissors")
    play_game = Game.play_game(player1, player2)
    return render_template('playervplayer.html', title='PvP', winner=play_game)

@app.route('/results')
def display_result():
    return render_template('results.html', title='Results')

