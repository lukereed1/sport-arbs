from bs4 import BeautifulSoup, SoupStrainer
import requests
from playwright.sync_api import sync_playwright
from pyppeteer.errors import PageError
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
from util import get_soup, get_soup_playwright, get_soup_playwright_async
from requests_html import HTMLSession
# text = "Tuesday, October 22, 2024"
# arr = text.split(" ")
#
# date = f"{arr[3]}-{datetime.strptime(arr[1], '%B').month}-{arr[2].replace(',', '')}"
# print(date)
#
from team_names.espn_team_map import tab_mapping
import asyncio
from pyppeteer import launch
from util import get_soup_pyppeteer
import re


# Testing


def get_soup_test(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    return BeautifulSoup(response.content, "lxml")


def get_soup_playwright_test(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ua = (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        )
        page = browser.new_page(user_agent=ua)
        page.goto(url)
        html = page.content()
        soup = BeautifulSoup(html, "lxml")
        return soup


async def get_soup_pyppeteer_test(url):
    browser = await launch(headless=False,
                           handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False)
    page = await browser.newPage()

    await page.setViewport({"width": 1920, "height": 1080})
    try:
        ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        await page.setUserAgent(ua)
        await page.goto(url)
        content = await page.content()
        soup = BeautifulSoup(content, "lxml")
        return soup
    except PageError as pe:
        print(f"Page Error: {pe}")
    except TimeoutError as te:
        print(f"Timeout Error: {te}")
    finally:
        await browser.close()


def test():
    url = "https://www.espn.com.au/nba/schedule"
    strainer = SoupStrainer("div", attrs={"class": "Wrapper Card__Content overflow-visible"})
    soup = get_soup(url, strainer)
    game_containers = soup.find_all(class_="ScheduleTables")

    if not game_containers:
        return

    for container in game_containers:
        # Gets date of games and converts to db format
        try:
            date = container.find("div", class_="Table__Title").get_text()
        except AttributeError as ae:
            print("Problem getting the data for some upcoming games")
            continue

        games = container.find_all("tr", class_="Table__TR Table__TR--sm Table__even")
        for game in games:
            # Gets time of games and converts to 24hr format
            time = game.find("td", class_="date__col")
            if time is not None:
                if time.get_text().strip() == "LIVE":
                    continue
                time = convert_to_24hr(time.get_text())
            else:
                continue  # Don't get data if games completed

            home_team = game.find("td", class_="colspan__col Table__TD").find("a", class_="AnchorLink")["href"]
            if home_team is not None:
                home_team = home_team.split("/")[6]
            away_team = game.find("td", class_="events__col Table__TD").find("a", class_="AnchorLink")["href"]
            if away_team is not None:
                away_team = away_team.split("/")[6]

            game = {
                "sport": 2,
                "home": home_team,
                "away": away_team,
                "date": date,
                "time": time
            }

            db = DB()
            if not db.check_game_exists(game):
                db.insert_game(game)

def convert_date(date):
    arr = date.split(" ")
    month = str(datetime.strptime(arr[1], '%B').month).zfill(2)
    day = arr[2].replace(',', '').zfill(2)
    return f"{arr[3]}-{month}-{day}"

def convert_to_24hr(time):
    return datetime.strptime(time, "%I:%M %p").strftime("%H:%M")

def date_format(date_string):
    date_object = datetime.strptime(date_string, "%a, %b %d %I:%M %p")
    return date_object.strftime(f"{datetime.now().year}-%m-%d")


test()
