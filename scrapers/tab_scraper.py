import asyncio
from datetime import datetime

from team_names.tab_team_map import tab_mapping
from util import get_soup_pyppeteer, get_soup_playwright_async
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class TabScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.SPORT_URLS = {
            1: "https://www.tab.com.au/sports/betting/American%20Football/competitions/NFL",
            2: "https://www.tab.com.au/sports/betting/Basketball/competitions/NBA",
            # 3: "https://www.tab.com.au/sports/betting/Ice%20Hockey"
        }

    def scrape_h2h(self, sport_id):
        print(f"Scraping Sport: {sport_id} Odds for TAB")
        strainer = SoupStrainer("div", class_="customised-template")
        try:  # Skip function if bookie not compatible with current sport iteration
            soup = asyncio.run(get_soup_playwright_async(self.SPORT_URLS[sport_id]))
        except KeyError:
            return
        stored_games = self.db.get_upcoming_games(sport_id)

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
                live_element = li_game.find("li", class_="in-play")
                if live_element is not None:
                    continue
                match_title = li_game.find("span", {"class": "match-name-text"}).get_text()
                if "v" not in match_title:
                    continue
                home, away = match_title.split(" v ")
                home = tab_mapping(home.lower().strip(), sport_id)
                away = tab_mapping(away.lower().strip(), sport_id)

                h2h_span = li_game.find_all("span", {"data-content": "Head To Head"})
                home_odds = h2h_span[0].parent.next_sibling.get_text()
                away_odds = h2h_span[1].parent.next_sibling.get_text()
            except (KeyError, AttributeError, IndexError) as e:
                print(f"Problem getting data for a game with sport id: {sport_id} on TAB\nError: {e}")
                continue

            for game in stored_games:
                # if self.date_format(date) == game["game_date"]:
                    self.update_h2h_market(home, away, game, 3, home_odds, away_odds)

    @staticmethod
    def date_format(date_string):
        date = datetime.strptime(f"{datetime.now().year} {date_string}", "%Y %a %d %b %H:%M")
        return date.strftime("%Y-%m-%d")
