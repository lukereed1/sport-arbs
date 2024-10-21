import sqlite3

connection = sqlite3.connect("odds.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO sports (sport) VALUES (?)", ("NFL",))
cur.execute("INSERT INTO sports (sport) VALUES (?)", ("NBA",))
cur.execute("INSERT INTO sports (sport) VALUES (?)", ("NRL",))
cur.execute("INSERT INTO sports (sport) VALUES (?)", ("AFL",))

# cur.execute("INSERT INTO games (sport_id, home_team, away_team, game_date, game_time) VALUES (?, ?, ?, ?, ?)",
#             ("1", "Team_A", "Team_B", "2024-10-21", "14:13:00"))
#
# cur.execute("INSERT INTO games (sport_id, home_team, away_team, game_date, game_time) VALUES (?, ?, ?, ?, ?)",
#             ("2", "Team_C", "Team_D", "2024-10-21", "16:13:00"))


connection.commit()
connection.close()