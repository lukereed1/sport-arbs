from datetime import datetime, timedelta
from util import get_soup_playwright
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class PointsbetScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.NFL_URL = "https://pointsbet.com.au/sports/american-football/NFL"

    def scrape_nfl_h2h(self):
        print("Scraping NFL H2H Odds for Pointsbet")
        stored_games = self.db.get_upcoming_games(1)
        strainer = SoupStrainer("div", attrs={"class": "fqk2zjd"})
        soup = get_soup_playwright(self.NFL_URL, strainer)

        try:
            games_list = soup.find_all("div", {"data-test": "event"})
            if not games_list:
                print("Problem finding games for Pointsbet")
                return
        except AttributeError as ae:
            print(f"Problem finding games\nError: {ae}")
            return

        for li_game in games_list:
            try:
                # date = li_game.find("div", class_="f1vavtkk").get_text()
                odds_boxes = li_game.find_all("span", class_="f11v6oas f1xlhiok")
                if len(odds_boxes) != 6:
                    continue
                h2h_odds = [box.get_text() for box in odds_boxes if box.find_previous_sibling() is None]
                team_names = li_game.find_all("div", class_="fddsvlq")
                home_odds = h2h_odds[1]
                away_odds = h2h_odds[0]
                home = team_names[1].get_text()
                away = team_names[0].get_text()
            except (IndexError, AttributeError) as e:
                print(f"Problem getting data for an NFL game on Pointsbet - Game might be live\nError: {e}")
                continue

            for game in stored_games:
                # if self.date_format(date) == game["game_date"]:
                    self.update_h2h_market(home, away, game, 4, home_odds, away_odds)

    @staticmethod
    def date_format(date_string):
        if "Tomorrow" in date_string:
            return (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        elif "m" in date_string and "s" in date_string:
            return datetime.now().strftime('%Y-%m-%d')
        else:
            date = date_string.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")
            date = f"{datetime.now().year} {date}"
            date = datetime.strptime(date, '%Y %a %d %b, %I:%M%p')
            return date.strftime('%Y-%m-%d')

