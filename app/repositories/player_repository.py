from app.db.run_sql import run_sql

from app.models.player import Player

def save(player):
    sql = "INSERT INTO players (name) VALUES (%s) RETURNING *"
    values = [player.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for row in results:
        player = Player(row['name'], row['id'])
        players.append(player)
    return players

def delete_all():
    sql = 'DELETE  FROM players'
    run_sql(sql)

