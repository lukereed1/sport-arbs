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
db = DB()
games = db.get_upcoming_games(1)
print(games[0]['id'])
stored_game_dates = [game['game_date'] for game in games]
for x in stored_game_dates:
    print(x)

print(" ")
url = "https://www.sportsbet.com.au/betting/american-football/nfl"


def scrape_nfl_h2h():
    strainer = SoupStrainer("div", attrs={"data-automation-id": "competition-matches-container"})
    soup = get_soup(url, strainer)
    game_containers = soup.find_all("div", class_="groupTitleContainerDesktop_fukjuk5 groupTitleExtra_f1r0fg9l")
    if not game_containers:
        return

    for container in game_containers:
        date = container.find("time").get('datetime')
        if date is None:
            return

        # With date found on web page, compare to games rows dates, if it matches
        # then compare home and away team, if matches again we can add this to our db with the odds

        if date not in stored_game_dates:
            continue

        # available games for date
        game_list = container.next_sibling.find_all("li")
        for game in game_list:
            print(game)







# scrape_nfl_h2h()

# url = "https://www.sportsbet.com.au/betting/american-football/nfl"
# strainer = SoupStrainer("div", attrs={"class": "multiMarketCouponContainer_f234ak7"})
# soup = get_soup(url, strainer)
#
# game_containers = soup.find_all(class_="multiMarketCouponContainer_f234ak7")
#
#
# for container in game_containers:
#     away = container.find("div", {"data-automation-id": "participant-one"}).get_text()
#     home = container.find("div", {"data-automation-id": "participant-two"}).get_text()
#     print(f"home: {home}")
#     print(f"away: {away}")
#     print(" ")