from datetime import datetime

from scrapers.bookie_scraper import BookieScraper
from util import get_soup_playwright


class BoombetScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.SPORT_URLS = {
            1: "https://www.boombet.com.au/sport-menu/Sport/American%20Football/NFL",
            2: "https://www.boombet.com.au/sport-menu/Sport/Basketball/NBA",
            3: "https://www.boombet.com.au/sport-menu/Sport/Ice%20Hockey/NHL",
            4: "https://www.boombet.com.au/sport-menu/Sport/Soccer/English%20Premier%20League",
        }

    def scrape_h2h(self, sport_id):
        print(f"Scraping Sport: {sport_id} Odds for Boombet")
        stored_games = self.db.get_upcoming_games(sport_id)
        if len(stored_games) == 0:
            print("No games scheduled")
            return
        soup = get_soup_playwright(self.SPORT_URLS[sport_id])

        try:
            if sport_id == 4:
                games_list = soup.find_all("div", class_="sc-etlBSa jlpBpx")
            else:
                games_list = soup.find_all("div", class_="sc-eFRbCa kVgTIN")
            if not games_list:
                print("Problem finding games for Boombet")
                return
        except AttributeError as ae:
            print(f"Problem finding games\nError: {ae}")
            return

        for li_game in games_list:
            try:
                if sport_id != 4:
                    teams = li_game.find_all("span", class_="market-title")
                    h2h_odds_element = li_game.find(lambda tag: tag.name == "span" and "H2H" in tag.get_text())
                    home = teams[0].get_text()
                    away = teams[1].get_text()
                    home_odds = h2h_odds_element.next_sibling.get_text()
                    away_odds = h2h_odds_element.next_sibling.next_sibling.get_text()
                    for game in stored_games:
                        self.update_h2h_market(home, away, game, 5, home_odds, away_odds)
                else:
                    teams = li_game.find_all("span", class_="teamName")
                    odds = li_game.find_all("span", class_="oddsValue")
                    home = teams[0].get_text()
                    away = teams[2].get_text()
                    home_odds = float(odds[0].get_text())
                    away_odds = float(odds[2].get_text())
                    draw_odds = float(odds[1].get_text())
                    for game in stored_games:
                        self.update_h2h_market(home, away, game, 5, home_odds, away_odds, draw_odds)

            except (IndexError, AttributeError) as e:
                print(f"Problem getting data for a game with sport id: {sport_id} on Boombet\nError: {e}")
                continue



    @staticmethod
    def date_format(date_string):
        date_object = datetime.strptime(date_string, "%a, %b %d %I:%M %p")
        return date_object.strftime(f"{datetime.now().year}-%m-%d")