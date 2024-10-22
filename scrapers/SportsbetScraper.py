from abc import ABC

from db.db import DB
from util import get_soup
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class SportsbetScraper(BookieScraper, ABC):
    def __init__(self):
        self.NFL_URL = "https://www.sportsbet.com.au/betting/american-football/nfl"
        self.db = DB()

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
                    if odds[0] is None or odds[1] is None:
                        return

                    if home == game['home_team']:
                        if away == game['away_team']:
                            # print(f"{home} vs {away} is in the database")
                            game_market = {
                                "id": game['id'],
                                "bookmaker_id": 1,
                                "market_id": 1,
                                "opt_1": home,
                                "opt_1_odds": odds[1].get_text(),
                                "opt_2": away,
                                "opt_2_odds": odds[0].get_text()
                            }
                            self.db.insert_game_market(game_market)
