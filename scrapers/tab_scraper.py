import asyncio
from datetime import datetime

from team_names.NFLteams import tab_mapping
from util import get_soup_pyppeteer, get_soup_playwright_async
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class TabScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.NFL_URL = "https://www.tab.com.au/sports/betting/American%20Football/competitions/NFL"

    def scrape_nfl_h2h(self):
        print("Scraping NFL H2H Odds for TAB")
        strainer = SoupStrainer("div", class_="customised-template")
        soup = asyncio.run(get_soup_playwright_async(self.NFL_URL))
        stored_games = self.db.get_upcoming_games(1)

        try:
            games_list = soup.find_all("div", class_="template-item")
            if not games_list:
                print("Problem finding games for TAB")
                return
        except AttributeError as ae:
            print(f"Problem finding games for TAB\nError: {ae}")
            return

        for li_game in games_list:
            try:
                # date = li_game.find("li", {"data-test": "close-time"}).get_text()
                match_title = li_game.find("span", {"class": "match-name-text"}).get_text()
                home, away = match_title.split(" v ")
                home = tab_mapping(home.lower().strip())
                away = tab_mapping(away.lower().strip())

                h2h_span = li_game.find_all("span", {"data-content": "Head To Head"})
                home_odds = h2h_span[0].parent.next_sibling.get_text()
                away_odds = h2h_span[1].parent.next_sibling.get_text()
            except (KeyError, AttributeError, IndexError) as e:
                print(f"Problem getting data for an NFL game on TAB - Game might be live\nError: {e}")
                continue

            for game in stored_games:
                # if self.date_format(date) == game["game_date"]:
                    self.update_h2h_market(home, away, game, 3, home_odds, away_odds)

    @staticmethod
    def date_format(date_string):
        date = datetime.strptime(f"{datetime.now().year} {date_string}", "%Y %a %d %b %H:%M")
        return date.strftime("%Y-%m-%d")
