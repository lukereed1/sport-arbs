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
    db = DB()
    upcoming_games = db.get_upcoming_games(1)
    all_games_with_arb_percent = []
    for game in upcoming_games:
        markets = db.get_all_markets_by_game(game["id"])
        for outer in markets:
            outer_opt1_win_percentage = 1 / outer["option_1_odds"]
            for inner in markets:
                if outer["game_id"] == inner["game_id"] and outer["bookmaker"] == inner["bookmaker"]:
                    continue
                inner_opt2_win_percentage = 1 / outer["option_2_odds"]
                sum = round(outer_opt1_win_percentage + inner_opt2_win_percentage, 3)

                all_games_with_arb_percent.append({
                    "date": game["game_date"],
                    "time": game["game_time"],
                    "sport": outer["sport"],
                    "book_1": outer["bookmaker"],
                    "team_1": outer["option_1"],
                    "odds_team_1": outer["option_1_odds"],
                    "book_2": inner["bookmaker"],
                    "team_2": inner["option_2"],
                    "odds_team_2": inner["option_2_odds"],
                    "arbitrage_sum": sum,

                })
    all_games_with_arb_percent.sort(key=lambda item: item["arbitrage_sum"])
    return all_games_with_arb_percent

                # print("OUTER: ")
                # print(f"Game Id: {outer['game_id']}")
                # print(outer["bookmaker"])
                # print(outer['option_1'])
                # print(outer['option_1_odds'])
                # print(outer['option_2'])
                # print(outer['option_2_odds'])
                # print(" ")
                # print("INNER: ")
                # print(f"Game Id: {inner['game_id']}")
                # print(inner["bookmaker"])
                # print(inner['option_1'])
                # print(inner['option_1_odds'])
                # print(inner['option_2'])
                # print(inner['option_2_odds'])
                # print("")
                # print("")


def date_format(date_string):
    date_object = datetime.strptime(date_string, "%a, %b %d %I:%M %p")
    return date_object.strftime(f"{datetime.now().year}-%m-%d")


test()
