from abc import ABC, abstractmethod

from db.db import DB


class BookieScraper(ABC):
    def __init__(self):
        self.db = DB()

    @abstractmethod
    def scrape_nfl_h2h(self):
        pass

    def update_db_h2h_market(self, home, away, game, bookmaker_id, home_odds, away_odds):
        if home == game['home_team']:
            if away == game['away_team']:
                # Gets existing game market if exists for SB H2H
                existing_game_market = self.db.check_game_market_exists(game['id'], bookmaker_id, 1)

                # if game market exists, checks odds to see if they require updating
                if existing_game_market is not None:
                    existing_home_odds = existing_game_market['option_1_odds']
                    existing_away_odds = existing_game_market['option_2_odds']
                    if existing_home_odds != home_odds or existing_away_odds != away_odds:
                        self.db.update_game_market_odds(existing_game_market['id'], home_odds, away_odds)
                else:
                    game_market = {
                        "id": game['id'],
                        "bookmaker_id": bookmaker_id,
                        "market_id": 1,
                        "opt_1": home,
                        "opt_1_odds": home_odds,
                        "opt_2": away,
                        "opt_2_odds": away_odds
                    }
                    self.db.insert_game_market(game_market)