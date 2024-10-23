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


# Testing
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

                odds = li_game.find_all("span", class_="size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9")

                home_odds = float(odds[1].get_text())
                away_odds = float(odds[0].get_text())

                if home_odds is None or away_odds is None:
                    return

                # print(f"away odds: {away_odds}")
                # print(f"home odds: {home_odds}")
                # print(" ")

                if home == game['home_team']:
                    if away == game['away_team']:
                        # print(f"{home} vs {away} is in the database")

                        # Check if game market exists in DB for this bookie (sportsbet)
                        # If odds have changed -> update db with new odds else continue
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
                                "opt_1": home_odds,
                                "opt_1_odds": 1.3,
                                "opt_2": away_odds,
                                "opt_2_odds": 1.9
                            }
                            db.insert_game_market(game_market)



scrape_nfl_h2h()
