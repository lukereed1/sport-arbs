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
from util import get_soup, get_soup_playwright
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
    print("Scraping NFL H2H Odds for Pointsbet")
    db = DB()
    stored_games = db.get_upcoming_games(1)
    strainer = SoupStrainer("div", attrs={"class": "fqk2zjd"})
    url = "https://pointsbet.com.au/sports/american-football/NFL"
    soup = get_soup_playwright(url, strainer)
    # soup = asyncio.run(get_soup_playwright(url, strainer))
    # soup = loop.run_until_complete(get_soup_playwright(url))
    # loop.close()

    try:
        games_list = soup.find_all("div", {"data-test": "event"})
    except AttributeError as ae:
        print(f"Problem finding games\nError: {ae}")
        return

    for li_game in games_list:
        date = ""
        try:
            date = li_game.find("div", class_="f1vavtkk").get_text()
            odds_boxes = li_game.find_all("span", class_="f11v6oas f1xlhiok")
            if len(odds_boxes) != 6:
                continue
            h2h_odds = [box.get_text() for box in odds_boxes if box.find_previous_sibling() is None]
            team_names = li_game.find_all("div", class_="fddsvlq")
            home_odds = h2h_odds[1]
            away_odds = h2h_odds[0]
            home = team_names[1].get_text()
            away = team_names[0].get_text()

            print("home: " + home + "odds: " + home_odds)
            print("away: " + away + "odds: " + away_odds)

        except (IndexError, AttributeError) as e:
            print(f"Problem getting data for an NFL game on Pointsbet - Game might be live\nError: {e}")

        for game in stored_games:
            if date_format(date) != game["game_date"]:
                continue
            db = DB()


def date_format(date_string):
    date = date_string.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")
    date = f"{datetime.now().year} {date}"
    date = datetime.strptime(date, '%Y %a %d %b, %I:%M%p')
    return date.strftime('%Y-%m-%d')


test()
