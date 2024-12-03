from abc import ABC, abstractmethod

from db.db import DB


class BookieScraper(ABC):
    def __init__(self):
        self.db = DB()

    @abstractmethod
    def scrape_h2h(self, sport_id):
        pass

    def update_h2h_market(self, home, away, game, bookmaker_id, home_odds, away_odds, draw_odds=None):
        # print(f"SCRAPED GAME HOME_TEAM: {home}\nEXISTING GAME HOME_TEAM: {game['home_team']}\n")
        if home == game["home_team"]:
            if away == game["away_team"]:
                # Gets existing game market if exists for H2H
                existing_game_market = self.db.check_game_market_exists(game["id"], bookmaker_id, 1)
                sport_id = game["sport_id"]
                # if game market exists, checks odds to see if they require updating
                if existing_game_market is not None:
                    existing_home_odds = existing_game_market["option_1_odds"]
                    existing_away_odds = existing_game_market["option_2_odds"]
                    existing_draw_odds = existing_game_market["option_3_odds"]

                    if existing_home_odds != home_odds or existing_away_odds != away_odds or (sport_id == 4 and existing_draw_odds != draw_odds):
                        if sport_id == 4:
                            self.db.update_game_market_odds(sport_id, existing_game_market['id'], home_odds, away_odds, draw_odds)
                        else:
                            self.db.update_game_market_odds(sport_id, existing_game_market['id'], home_odds, away_odds, 0)
                else:
                    game_market = {
                        "id": game['id'],
                        "bookmaker_id": bookmaker_id,
                        "market_id": 1,
                        "opt_1": home,
                        "opt_1_odds": home_odds,
                        "opt_2": away,
                        "opt_2_odds": away_odds,
                    }

                    if sport_id == 4:
                        game_market["opt_3"] = "Draw"
                        game_market["opt_3_odds"] = draw_odds
                        self.db.insert_game_market(game_market, 4)
                    else:
                        self.db.insert_game_market(game_market)




