from flask import render_template, request, redirect
from app import app
from app.models.players import *
from app.models.player import *
from app.models.game import *

@app.route('/')
def index():
    return render_template('index.html', title='RPS', players=players)

@app.route('/rock/scissors')
def player_v_player():
    # Game.play_game(player_1, player_2)
    return render_template('playervplayer.html', title='PvP', players=players)



# methods=['POST']