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




def date_format(date_string):
    date = datetime.strptime(date_string.split(' ')[1], "%d/%m/%Y")
    return date.strftime("%Y-%m-%d")


scrape_nfl_h2h()
