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
from team_names.NFLteams import tab_mapping
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
    print("Scraping NFL H2H Odds for Betr")
    url = "https://www.betr.com.au/sports/American-Football/108/United-States-of-America/NFL-Matches/37249"
    soup = asyncio.run(get_soup_playwright_async(url))

    try:
        containers = soup.find_all("div", class_="MuiPaper-elevation1")

    except AttributeError as ae:
        print(f"Problem finding games for Betr\nError: {ae}")
        return

    for li_game in containers:
        team_and_odds_element = li_game.find_all("button", class_="MuiButton-disableElevation")
        if not team_and_odds_element:
            continue
        teams = []
        odds = []
        for team_odds in team_and_odds_element:
            team_and_odds = team_odds.get_text().strip()
            match = re.match(r"(.+?)(\d+\.\d+)", team_and_odds)
            if match:
                team_name = match.group(1).strip()
                odds_value = float(match.group(2).strip())
                teams.append(team_name)
                odds.append(odds_value)
                # print(f"Team: {team_name}, Odds: {odds_value}")

        home = teams[0]
        away = teams[1]
        home_odds = odds[0]
        away_odds = odds[1]
        print(f"Home Team: {home}, Odds: {home_odds}")
        print(f"Away Team: {away}, Odds: {away_odds}")
        print(" ")





def date_format(date_string):
    date_object = datetime.strptime(date_string, "%a, %b %d %I:%M %p")
    return date_object.strftime(f"{datetime.now().year}-%m-%d")

test()
