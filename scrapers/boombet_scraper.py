from datetime import datetime
from util import get_soup, get_soup_playwright
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class BoombetScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.NFL_URL = "https://www.boombet.com.au/sport-menu/Sport/American%20Football/NFL"

    def scrape_nfl_h2h(self):
        print("Scraping NFL H2H Odds for Boombet")
        stored_games = self.db.get_upcoming_games(1)
        strainer = SoupStrainer("div", attrs={"class": "listItemsWrapper"})
        soup = get_soup_playwright(self.NFL_URL, strainer)

        try:
            games_list = soup.find_all("div", class_="sc-eFRbCa kVgTIN")
        except AttributeError as ae:
            print(f"Problem finding games\nError: {ae}")
            return

        for li_game in games_list:
            try:
                date = li_game.find("span", class_="matchDate").get_text()
                teams = li_game.find_all("span", class_="market-title")
                h2h_odds_element = li_game.find(lambda tag: tag.name == "span" and "H2H" in tag.get_text())
                home = teams[0].get_text()
                away = teams[1].get_text()
                home_odds = h2h_odds_element.next_sibling.get_text()
                away_odds = h2h_odds_element.next_sibling.next_sibling.get_text()

            except (IndexError, AttributeError) as e:
                print(f"Problem getting data for an NFL game on Boombet - Game might be live\nError: {e}")
                continue

            for game in stored_games:
                if self.date_format(date) == game["game_date"]:
                    self.update_h2h_market(home, away, game, 5, home_odds, away_odds)

    @staticmethod
    def date_format(date_string):
        date_object = datetime.strptime(date_string, "%a, %b %d %I:%M %p")
        return date_object.strftime(f"{datetime.now().year}-%m-%d")