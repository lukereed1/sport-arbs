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
    print("Scraping NFL H2H Odds for Boombet")
    db = DB()
    stored_games = db.get_upcoming_games(1)
    strainer = SoupStrainer("div", attrs={"class": "listItemsWrapper"})
    url = "https://www.boombet.com.au/sport-menu/Sport/American%20Football/NFL"
    soup = get_soup_playwright(url, strainer)

    try:
        games_list = soup.find_all("div", class_="sc-eFRbCa kVgTIN")
    except AttributeError as ae:
        print(f"Problem finding games\nError: {ae}")
        return

    for li_game in games_list:
        try:
            date = date_format(li_game.find("span", class_="matchDate").get_text())
            teams = li_game.find_all("span", class_="market-title")
            h2h_odds_element = li_game.find(lambda tag: tag.name == "span" and "H2H" in tag.get_text())
            home = teams[0].get_text()
            away = teams[1].get_text()
            home_odds = h2h_odds_element.next_sibling.get_text()
            away_odds = h2h_odds_element.next_sibling.next_sibling.get_text()

            # print(f"home: {home} odds: {home_odds}")
            # print(f"away: {away} odds: {away_odds}")

        except (IndexError, AttributeError) as e:
            print(f"Problem getting data for an NFL game on Boombet - Game might be live\nError: {e}")
            continue


def date_format(date_string):
    date_object = datetime.strptime(date_string, "%a, %b %d %I:%M %p")
    return date_object.strftime(f"{datetime.now().year}-%m-%d")

test()
