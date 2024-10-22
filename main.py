from bs4 import BeautifulSoup, SoupStrainer
import requests
import scrapers.bookie_scraper
from db.db import DB
from scrapers.games_scraper import GamesScraper
from datetime import datetime

from util import get_soup

# text = "Tuesday, October 22, 2024"
# arr = text.split(" ")
#
# date = f"{arr[3]}-{datetime.strptime(arr[1], '%B').month}-{arr[2].replace(',', '')}"
# print(date)
#



test = GamesScraper()

print(" ")
url = "https://www.sportsbet.com.au/betting/american-football/nfl"


def scrape_nfl_h2h():
    db = DB()
    games = db.get_upcoming_games(1)
    strainer = SoupStrainer("div", attrs={"data-automation-id": "competition-matches-container"})
    soup = get_soup(url, strainer)
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

                if home == game['home_team']:
                    if away == game['away_team']:
                        # print(f"{home} vs {away} is in the database")
                        game_market = {
                            "id": game['id'],
                            "bookmaker_id": 1,
                            "market_id": 1,
                            "opt_1": home,
                            "opt_1_odds": 1.5,
                            "opt_2": away,
                            "opt_2_odds": 1.9
                        }
                        db = DB()
                        db.insert_game_market(game_market)
                else:
                    continue





scrape_nfl_h2h()
