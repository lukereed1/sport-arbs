import sqlite3

connection = sqlite3.connect("odds.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO games (home_team, away_team, game_date, game_time) VALUES (?, ?, ?, ?)",
            ("Team_A", "Team_B", "2024-10-21", "14:13:00"))


connection.commit()
connection.close()