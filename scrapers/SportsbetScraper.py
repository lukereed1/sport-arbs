from abc import ABC
from util import get_soup
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer

class SportsbetScraper(BookieScraper, ABC):
    def __init__(self):
        self.NFL_URL = "https://www.sportsbet.com.au/betting/american-football/nfl"
    def scrape_nfl_h2h(self):
        strainer = SoupStrainer("div", attrs={"class": "size11_fwt0xu4 Nevada_fxjpoyk groupTitle_fhtxh7u"})
        soup = get_soup(self.NFL_URL, strainer)

        # Get all games available
        # Get dates and times that have not ben yet for NFL from database