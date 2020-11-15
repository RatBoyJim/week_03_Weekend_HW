from app.db.run_sql import run_sql

from app.models.player import Player

def save(player):
    sql = "INSERT INTO players (name, choice, won, drawn, lost) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [player.name, player.choice, player.won, player.drawn, player.lost]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for row in results:
        player = Player(row['name'], row['choice'], row['won'], row['drawn'], row['lost'], row['id'])
        players.append(player)
    return players

def select_player_by_name(name):
    player = None

    sql = 'SELECT * FROM players WHERE name = %s'
    values = [name]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = Player(result['name'], result['choice'], result['won'], result['drawn'], result['lost'], result['id'])
    return player


def update(player):
    sql = "UPDATE players SET (name, choice, won, drawn, lost) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [player.name, player.choice, player.won, player.drawn, player.lost, player.id]
    run_sql(sql, values)


def delete_all():
    sql = 'DELETE  FROM players'
    run_sql(sql)

