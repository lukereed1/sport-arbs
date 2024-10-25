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

# text = "Tuesday, October 22, 2024"
# arr = text.split(" ")
#
# date = f"{arr[3]}-{datetime.strptime(arr[1], '%B').month}-{arr[2].replace(',', '')}"
# print(date)
#
import asyncio
from pyppeteer import launch
from util import get_soup_pyppeteer

# Testing

async def scrape_with_pyppeteer(url):
    # Launch a headless browser
    browser = await launch(headless=True)
    page = await browser.newPage()

    # Navigate to the URL
    await page.goto(url)

    # Wait for the content to load (modify as necessary)
    await page.waitForSelector('.sports-event-subtitle__other-row')  # Wait for a specific element

    # Get the page content
    content = await page.content()

    # Close the browser
    await browser.close()

    # Use BeautifulSoup to parse the page content
    soup = BeautifulSoup(content, 'html.parser', parse_only=strainer)
    return soup


# def get_soup_test(url):
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#     response = requests.get(url, headers=headers)
#     time.sleep(5)
#     return BeautifulSoup(response.content, "lxml")


def scrape_nfl_h2h():
    db = DB()
    games = db.get_upcoming_games(1)
    url = "https://www.neds.com.au/sports/american-football/nfl"
    strainer = SoupStrainer("div", attrs={"class": "events-wrapper__row-wrapper"})
    soup = asyncio.run(get_soup_pyppeteer(url, strainer))
    game_containers = soup.find_all("div", class_="sport-events__date-group")
    if not game_containers:
        return

    for container in game_containers:
        date = container.find("span", class_="sports-date-title__text").get_text()
        if date is None:
            continue

        for game in games:
            # print(f"stored db date: {game['game_date']} | found date: {date}")
            if game['game_date'] != date_format(date):
                continue
            #
            curr_date_games_list = container.find_all("div", class_="sport-event-card")
            if not curr_date_games_list:
                continue

            for li_game in curr_date_games_list:
                teams = li_game.find_all("div", class_="price-button-name")
                if not teams:
                    continue
                home = teams[0].get_text()
                away = teams[1].get_text()
                if home is None or away is None:
                    continue

                odds = li_game.find_all("div", class_="price-button-odds-price")
                home_odds = float(odds[0].get_text())
                away_odds = float(odds[1].get_text())
                if home_odds is None or away_odds is None:
                    continue

                # book = scrapers.SportsbetScraper()
                # book.upd

                if home == game['home_team']:
                    if away == game['away_team']:
                        db = DB()
                        existing_game_market = db.check_game_market_exists(game['id'], 2, 1)

                        if existing_game_market is not None:
                            existing_home_odds = existing_game_market['option_1_odds']
                            existing_away_odds = existing_game_market['option_2_odds']
                            if existing_home_odds != home_odds or existing_away_odds != away_odds:
                                db.update_game_market_odds(existing_game_market['id'], home_odds, away_odds)
                        else:
                            game_market = {
                                "id": game['id'],
                                "bookmaker_id": 2,
                                "market_id": 1,
                                "opt_1": home,
                                "opt_1_odds": home_odds,
                                "opt_2": away,
                                "opt_2_odds": away_odds
                            }
                            db.insert_game_market(game_market)



def date_format(date_string):
    date = datetime.strptime(date_string.split(' ')[1], "%d/%m/%Y")
    return date.strftime("%Y-%m-%d")


scrape_nfl_h2h()
