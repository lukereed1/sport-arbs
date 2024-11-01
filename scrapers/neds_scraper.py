import asyncio
from datetime import datetime
from util import get_soup_pyppeteer, get_soup_playwright
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class NedsScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.NFL_URL = "https://www.neds.com.au/sports/american-football/nfl"

    @staticmethod
    def date_format(date_string):
        date = datetime.strptime(date_string.split(' ')[1], "%d/%m/%Y")
        return date.strftime("%Y-%m-%d")

    def scrape_nfl_h2h(self):
        print("Scraping NFL H2H Odds for Neds")
        games = self.db.get_upcoming_games(1)
        strainer = SoupStrainer("div", attrs={"class": "events-wrapper__row-wrapper"})
        soup = get_soup_playwright(self.NFL_URL)

        try:
            game_containers = soup.find_all("div", class_="sport-events__date-group")
            if not game_containers:
                print("Problem finding games for Neds")
                return
        except AttributeError as ae:
            print(f"Problem finding games\nError: {ae}")
            return

        for container in game_containers:
            # date = container.find("span", class_="sports-date-title__text").get_text()
            for game in games:
                # if game['game_date'] != self.date_format(date):
                #     continue

                curr_date_games_list = container.find_all("div", class_="sport-event-card")

                for li_game in curr_date_games_list:
                    try:
                        teams = li_game.find_all("div", class_="price-button-name")
                        home = teams[0].get_text()
                        away = teams[1].get_text()

                        odds = li_game.find_all("div", class_="price-button-odds-price")
                        home_odds = float(odds[0].get_text())
                        away_odds = float(odds[1].get_text())

                        self.update_h2h_market(home, away, game, 2, home_odds, away_odds)
                    except (AttributeError, IndexError) as e:
                        print(f"Problem getting data for an NFL game on Neds - Game might be live\nError: {e}")
