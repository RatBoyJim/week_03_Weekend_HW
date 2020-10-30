from flask import render_template, request, redirect
from app import app
from app.models.players import *
from app.models.player import *
from app.models.game import *

@app.route('/')
def index():
    return render_template('index.html', title='RPS', players=players)