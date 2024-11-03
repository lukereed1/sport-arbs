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
    print("Scraping NFL H2H Odds for Sportsbet")
    db = DB()
    games = db.get_upcoming_games(2)
    strainer = SoupStrainer("div", attrs={"data-automation-id": "competition-matches-container"})
    soup = get_soup("https://www.sportsbet.com.au/betting/basketball-us/nba", strainer)

    try:
        game_containers = soup.find_all("div", class_="groupTitleContainerDesktop_fukjuk5 groupTitleExtra_f1r0fg9l")
        if not game_containers:
            print("Problem finding games for Sportsbet")
            return
    except AttributeError as ae:
        print(f"Problem finding games\nError: {ae}")
        return

    for container in game_containers:
        # date = container.find("time").get('datetime')
        for game in games:
            # if game['game_date'] != date:
            #     continue

            curr_date_games_list = container.next_sibling.find_all("li")

            for li_game in curr_date_games_list:
                try:
                    live_element = li_game.find("div", class_="live_fst4f0d")
                    if live_element is not None:  # Skip live games
                        continue

                    away = li_game.find("div", {"data-automation-id": "participant-one"}).get_text()
                    home = li_game.find("div", {"data-automation-id": "participant-two"}).get_text()

                    odds = li_game.find_all("span", class_="size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9")
                    home_odds = float(odds[1].get_text())
                    away_odds = float(odds[0].get_text())

                    print(f"home: {home} home odds: {home_odds}")
                    print(f"away: {away} away odds: {away_odds}")

                    # self.update_h2h_market(home, away, game, 1, home_odds, away_odds)
                except (AttributeError, IndexError) as e:
                    print(f"Problem getting data for an NFL game on Sportsbet - Game might be live\nError: {e}")





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
