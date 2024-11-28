from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError
from pyppeteer import launch
from pyppeteer.errors import PageError
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright


def get_soup(url, strainer):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/126.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        return BeautifulSoup(response.content, "lxml", parse_only=strainer)
    except HTTPError as hp:
        print(f"Http Error: {hp}")


async def get_soup_playwright_async(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ua = (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        )
        page = await browser.new_page(user_agent=ua)

        try:
            await page.goto(url)
            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")
            return soup
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()


def get_soup_playwright(url):
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


# async def get_soup_pyppeteer(url):
#     browser = await launch(headless=False,
#                            handleSIGINT=False,
#                            handleSIGTERM=False,
#                            handleSIGHUP=False)
#     page = await browser.newPage()
#
#     await page.setViewport({"width": 1920, "height": 1080})
#     try:
#         ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
#         await page.setUserAgent(ua)
#         await page.goto(url)
#         content = await page.content()
#         soup = BeautifulSoup(content, "lxml")
#         return soup
#     except PageError as pe:
#         print(f"Page Error: {pe}")
#     except TimeoutError as te:
#         print(f"Timeout Error: {te}")
#     finally:
#         await browser.close()
