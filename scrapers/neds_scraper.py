import asyncio
from datetime import datetime

from bs4 import SoupStrainer

from scrapers.bookie_scraper import BookieScraper
from team_names.neds_team_map import neds_mapping
from util import get_soup_playwright, get_soup_playwright_async, get_soup_pyppeteer


class NedsScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.SPORT_URLS = {
            1: "https://www.neds.com.au/sports/american-football/nfl",
            2: "https://www.neds.com.au/sports/basketball/usa/nba",
            3: "https://www.neds.com.au/sports/ice-hockey/usa/nhl",
            4: "https://www.neds.com.au/sports/soccer/uk-ireland/premier-league",
        }

    def scrape_h2h(self, sport_id):
        print(f"Scraping Sport: {sport_id} Odds for Neds")
        games = self.db.get_upcoming_games(sport_id)
        # soup = asyncio.run(get_soup_pyppeteer(self.SPORT_URLS[sport_id]))
        soup = get_soup_playwright(self.SPORT_URLS[sport_id])
        # print(soup.prettify())
        try:
            game_containers = soup.find_all("div", class_="sport-events__date-group")
            if not game_containers:
                print("Problem finding games for Neds")
                return
        except AttributeError as ae:
            print(f"Problem finding games\nError: {ae}")
            return

        for container in game_containers:
            for game in games:
                curr_date_games_list = container.find_all("div", class_="sports-market-primary")

                for li_game in curr_date_games_list:
                    try:
                        teams = li_game.find_all("div", class_="price-button-name")
                        odds = li_game.find_all("div", class_="price-button-odds-price")
                        home = teams[0].get_text()
                        home_odds = float(odds[0].get_text())

                        if sport_id != 4:
                            away = teams[1].get_text()
                            away_odds = float(odds[1].get_text())
                            self.update_h2h_market(home, away, game, 2, home_odds, away_odds)
                        else:
                            home = neds_mapping(home.lower(), 4)
                            away = teams[2].get_text()
                            away = neds_mapping(away.lower(), 4)
                            away_odds = float(odds[2].get_text())
                            draw_odds = float(odds[1].get_text())

                            self.update_h2h_market(home, away, game, 2, home_odds, away_odds, draw_odds)
                    except (AttributeError, IndexError) as e:
                        print(f"Problem getting data for a game with sport id: {sport_id} on Neds\nError: {e}")

    @staticmethod
    def date_format(date_string):
        date = datetime.strptime(date_string.split(' ')[1], "%d/%m/%Y")
        return date.strftime("%Y-%m-%d")
