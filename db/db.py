import sqlite3


class DB:
    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect("./db/odds.db")
        conn.row_factory = sqlite3.Row
        return conn

    def get_all_games(self):
        conn = self.get_db_connection()
        try:
            games = conn.execute("SELECT * FROM games JOIN sports ON games.sport_id = sports.id").fetchall()
            return games
        except sqlite3.OperationalError:
            print("Problem getting games")
        finally:
            conn.close()

    def get_upcoming_games(self, sport_id):
        conn = self.get_db_connection()
        try:
            games = conn.execute("SELECT * FROM games WHERE sport_id = ?"
                                 "AND (game_date > DATE('now')) OR (game_date = DATE('now')"
                                 "AND game_time > TIME('now'))", (sport_id,)).fetchall()
            return games
        except sqlite3.OperationalError:
            print("Problem getting upcoming games")
        finally:
            conn.close()

    def insert_game(self, game):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO games (sport_id, home_team, away_team, game_date, game_time) VALUES (?, ?, ?, ?, ?)",
                (game['sport'], game['home'], game['away'], game['date'], game['time']))
            conn.commit()
        except sqlite3.OperationalError:
            print("Problem inserting game")
        finally:
            conn.close()

    def check_game_exists(self, game):
        conn = self.get_db_connection()
        try:
            game = conn.execute("SELECT 1 FROM games WHERE home_team = ? AND away_team = ? AND game_date = ? LIMIT 1",
                                (game['home'], game['away'], game['date'])).fetchone()
            return game is not None
        except sqlite3.OperationalError:
            print("Problem checking if game exists")
        finally:
            conn.close()


