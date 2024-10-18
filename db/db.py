import sqlite3


def get_db_connection():
    conn = sqlite3.connect("./db/odds.db")
    conn.row_factory = sqlite3.Row
    return conn


def insert_game(game):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO games (home_team, away_team, game_date, game_time) VALUES (?, ?, ?, ?)",
                   (game['home'], game['away'], game['date'], game['time']))
    conn.commit()
    conn.close()
