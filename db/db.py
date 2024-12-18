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
        except sqlite3.OperationalError as e:
            print(f"Problem getting all games\nError: {e}")
        finally:
            conn.close()

    def get_upcoming_games(self, sport_id):
        conn = self.get_db_connection()
        try:
            games = conn.execute("SELECT * FROM games WHERE sport_id = ? "
                                 "AND ((game_date > DATE('now')) OR (game_date = DATE('now') "
                                 "AND game_time > TIME('now')))", (sport_id,)).fetchall()
            return games
        except sqlite3.OperationalError as e:
            print(f"Problem getting upcoming games\nError: {e}")
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
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print(f"Problem inserting game\nError: {e}")
        finally:
            conn.close()

    def check_game_exists(self, game):
        conn = self.get_db_connection()
        try:
            game = conn.execute("SELECT 1 FROM games WHERE home_team = ? AND away_team = ? AND game_date = ? LIMIT 1",
                                (game['home'], game['away'], game['date'])).fetchone()
            return game is not None
        except sqlite3.OperationalError as e:
            print(f"Problem checking if game exists\nError: {e}")
        finally:
            conn.close()

    def get_all_markets(self, sport_id):
        conn = self.get_db_connection()
        try:
            available_markets = conn.execute("SELECT * FROM game_markets "
                                             "JOIN games ON game_markets.game_id = games.id "
                                             "JOIN sports ON games.sport_id = sports.id "
                                             "JOIN bookmakers ON game_markets.bookmaker_id = bookmakers.id "
                                             "JOIN markets ON game_markets.market_id = markets.id "
                                             "WHERE sport_id = ?", (sport_id,)).fetchall()
            return available_markets
        except sqlite3.OperationalError as e:
            print(f"Problem getting all markets\nError: {e}")

    def get_all_markets_by_game(self, game_id):
        conn = self.get_db_connection()
        try:
            markets = conn.execute("SELECT * FROM game_markets "
                                   "JOIN games ON game_markets.game_id = games.id "
                                   "JOIN sports ON games.sport_id = sports.id "
                                   "JOIN bookmakers ON game_markets.bookmaker_id = bookmakers.id "
                                   "JOIN markets ON game_markets.market_id = markets.id "
                                   "WHERE game_id = ?", (game_id,)).fetchall()
            return markets
        except sqlite3.OperationalError as e:
            print(f"Problem getting markets for game id: {game_id}\nError: {e}")

    def insert_game_market(self, game_market, sport_id=None):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        try:
            if sport_id == 4:
                cursor.execute("INSERT INTO game_markets (game_id, bookmaker_id, market_id, option_1, option_1_odds,"
                               "option_2, option_2_odds, option_3_odds) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                               (game_market['id'], game_market['bookmaker_id'],
                                game_market['market_id'], game_market['opt_1'],
                                game_market['opt_1_odds'], game_market['opt_2'],
                                game_market['opt_2_odds'], game_market['opt_3_odds'],))
            else:
                cursor.execute("INSERT INTO game_markets (game_id, bookmaker_id, market_id, option_1, option_1_odds,"
                               "option_2, option_2_odds) VALUES (?, ?, ?, ?, ?, ?, ?)",
                               (game_market['id'], game_market['bookmaker_id'],
                                game_market['market_id'], game_market['opt_1'],
                                game_market['opt_1_odds'], game_market['opt_2'],
                                game_market['opt_2_odds'],))
            conn.commit()
        except sqlite3.OperationalError as e:
            print(f"Problem inserting game market\nError: {e}")
        finally:
            conn.close()

    def check_game_market_exists(self, game_id, bookmaker_id, market_id):
        conn = self.get_db_connection()
        try:
            game_market = conn.execute(
                "SELECT * FROM game_markets WHERE game_id = ? AND bookmaker_id = ? AND market_id = ?"
                , (game_id, bookmaker_id, market_id,)).fetchone()
            return game_market
        except sqlite3.OperationalError as e:
            print(f"Problem checking if game market exists\nError: {e}")
        finally:
            conn.close()

    def update_game_market_odds(self, sport_id, game_market_id, new_odds_1, new_odds_2, new_odds_3):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        try:
            if sport_id == 4:
                cursor.execute("UPDATE game_markets "
                               "SET option_1_odds = ?, option_2_odds = ?, option_3_odds = ? "
                               "WHERE id = ?", (new_odds_1, new_odds_2, new_odds_3, game_market_id,))
                conn.commit()
            else:
                cursor.execute("UPDATE game_markets "
                               "SET option_1_odds = ?, option_2_odds = ? "
                               "WHERE id = ?", (new_odds_1, new_odds_2, game_market_id,))
                conn.commit()

        except sqlite3.OperationalError as e:
            print(f"Problem updating game market odds\nError: {e}")
        finally:
            conn.close()
