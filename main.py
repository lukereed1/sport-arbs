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
    stored_game_dates = [game['game_date'] for game in games]
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




            # compare db.games.date with bookiegame list date
            # continue next iteration if not found
            # if date != game['game_date'] continue;
            # get list of games for current container (date was found in db row)
            # if bookie home team != game['home_team'] continue;
            # if bookie away team != game['away_team'] continue;
            # bookie game matches game in db
            # find bookie odds for either side
            # add to db (make new table) use game['id'] as foreign key in new table

            # bookie_game_list = container.next_sibling.find_all("li")
            # if not bookie_game_list:
            #     continue
            print(game)


scrape_nfl_h2h()
