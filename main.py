from bs4 import BeautifulSoup, SoupStrainer
import requests
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import scrapers.bookie_scraper
from db.db import DB
from scrapers.games_scraper import GamesScraper
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from util import get_soup
from requests_html import HTMLSession
# text = "Tuesday, October 22, 2024"
# arr = text.split(" ")
#
# date = f"{arr[3]}-{datetime.strptime(arr[1], '%B').month}-{arr[2].replace(',', '')}"
# print(date)
#
from team_names.NFLteams import tab_mapping
import asyncio
from pyppeteer import launch
from util import get_soup_pyppeteer


# Testing


def get_soup_test(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    return BeautifulSoup(response.content, "lxml")


def test():
    print("Scraping NFL H2H Odds for TAB")
    url = "https://www.tab.com.au/sports/betting/American%20Football/competitions/NFL"
    strainer = SoupStrainer("div", class_="customised-template")
    soup = asyncio.run(get_soup_pyppeteer(url, strainer))
    db = DB()
    stored_games = db.get_upcoming_games(1)

    games_list = soup.find_all("div", class_="template-item")

    if not games_list:
        return

    for li_game in games_list:
        try:
            date = li_game.find("li", {"data-test": "close-time"}).get_text()
            match_title = li_game.find("span", {"class": "match-name-text"}).get_text()
            home, away = match_title.split(" v ")
            home = tab_mapping(home.lower().strip())
            away = tab_mapping(away.lower().strip())

            h2h_span = li_game.find_all("span", {"data-content": "Head To Head"})
            home_odds = h2h_span[0].parent.next_sibling.get_text()
            away_odds = h2h_span[1].parent.next_sibling.get_text()
        except (KeyError, AttributeError, IndexError) as e:
            print(f"Problem getting game data - Game might be live\nError: {e}")
            continue

        for game in stored_games:
            print(date_format(date))
            if date_format(date) != game['game_date']:
                continue

            if home == game['home_team']:
                if away == game['away_team']:
                    db = DB()
                    # Gets existing game market if exists for SB H2H
                    existing_game_market = db.check_game_market_exists(game['id'], 3, 1)

                    # if game market exists, checks odds to see if they require updating
                    if existing_game_market is not None:
                        existing_home_odds = existing_game_market['option_1_odds']
                        existing_away_odds = existing_game_market['option_2_odds']
                        if existing_home_odds != home_odds or existing_away_odds != away_odds:
                            db.update_game_market_odds(existing_game_market['id'], home_odds, away_odds)
                    else:
                        game_market = {
                            "id": game['id'],
                            "bookmaker_id": 3,
                            "market_id": 1,
                            "opt_1": home,
                            "opt_1_odds": home_odds,
                            "opt_2": away,
                            "opt_2_odds": away_odds
                        }
                        db.insert_game_market(game_market)


def date_format(date_string):
    date = datetime.strptime(f"{datetime.now().year} {date_string}", "%Y %a %d %b %H:%M")
    return date.strftime("%Y-%m-%d")


test()
