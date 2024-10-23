from abc import ABC

from db.db import DB
from util import get_soup
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class SportsbetScraper(BookieScraper, ABC):
    def __init__(self):
        self.db = DB()
        self.NFL_URL = "https://www.sportsbet.com.au/betting/american-football/nfl"

    def scrape_nfl_h2h(self):
        games = self.db.get_upcoming_games(1)
        strainer = SoupStrainer("div", attrs={"data-automation-id": "competition-matches-container"})
        soup = get_soup(self.NFL_URL, strainer)
        game_containers = soup.find_all("div", class_="groupTitleContainerDesktop_fukjuk5 groupTitleExtra_f1r0fg9l")
        if not game_containers:
            return
        for container in game_containers:
            date = container.find("time").get('datetime')
            if date is None:
                return

            for game in games:
                if game['game_date'] != date:
                    continue

                curr_date_games_list = container.next_sibling.find_all("li")

                for li_game in curr_date_games_list:
                    away = li_game.find("div", {"data-automation-id": "participant-one"}).get_text()
                    home = li_game.find("div", {"data-automation-id": "participant-two"}).get_text()
                    if away is None or home is None:
                        continue

                    odds = li_game.find_all("span", class_="size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9")
                    home_odds = float(odds[1].get_text())
                    away_odds = float(odds[0].get_text())

                    if home_odds is None or away_odds is None:
                        return

                    if home == game['home_team']:
                        if away == game['away_team']:
                            db = DB()
                            # Gets existing game market if exists for SB H2H
                            existing_game_market = db.check_game_market_exists(game['id'], 1, 1)

                            # if game market exists, checks odds to see if they require updating
                            if existing_game_market is not None:
                                existing_home_odds = existing_game_market['option_1_odds']
                                existing_away_odds = existing_game_market['option_2_odds']
                                if existing_home_odds != home_odds or existing_away_odds != away_odds:
                                    db.update_game_market_odds(existing_game_market['id'], home_odds, away_odds)

                            else:
                                game_market = {
                                    "id": game['id'],
                                    "bookmaker_id": 1,
                                    "market_id": 1,
                                    "opt_1": home,
                                    "opt_1_odds": home_odds,
                                    "opt_2": away,
                                    "opt_2_odds": away_odds
                                }
                                self.db.insert_game_market(game_market)
