from bs4 import BeautifulSoup, SoupStrainer
import requests
from urllib.error import HTTPError
from pyppeteer import launch
from pyppeteer.errors import PageError


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


# use when site has loading screens
async def get_soup_pyppeteer(url, strainer):
    browser = await launch(headless=True,
                           handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False)
    page = await browser.newPage()
    await page.setViewport({"width": 1920, "height": 1080})
    try:
        await page.goto(url)
        # await page.waitForSelector('.sport-event-card')  # Wait for a specific element
        content = await page.content()
        soup = BeautifulSoup(content, "lxml", parse_only=strainer)
        return soup
    except PageError as pe:
        print(f"Page Error: {pe}")
    except TimeoutError as te:
        print(f"Timeout Error: {te}")
    finally:
        await browser.close()


