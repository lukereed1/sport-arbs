from bs4 import BeautifulSoup, SoupStrainer
import requests
import scrapers.bookie_scraper
from scrapers.games_scraper import GamesScraper
from datetime import datetime


# text = "Tuesday, October 22, 2024"
# arr = text.split(" ")
#
# date = f"{arr[3]}-{datetime.strptime(arr[1], '%B').month}-{arr[2].replace(',', '')}"
# print(date)
#

test = GamesScraper()
games = test.get_nfl_games()

for game in games:
    print(game)



## sb nfl

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