import re

from util import get_soup, get_soup_playwright, get_soup_pyppeteer, get_soup_playwright_async
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer
import asyncio


class BetrScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.SPORT_URLS = {
            1: "https://www.betr.com.au/sports/American-Football/108/United-States-of-America/NFL-Matches/37249",
            2: "https://www.betr.com.au/sports/Basketball/107/United-States-of-America/NBA-Matches/39251",
            3: "https://www.betr.com.au/sports/Ice-Hockey/111/United-States-of-America/NHL-Matches/39252"
        }

    def scrape_h2h(self, sport_id):
        print(f"Scraping Sport: {sport_id} Odds for Betr")
        stored_games = self.db.get_upcoming_games(sport_id)
        soup = asyncio.run(get_soup_playwright_async(self.SPORT_URLS[sport_id]))

        try:
            containers = soup.find_all("div", class_="MuiPaper-elevation1")
            if not containers:
                print("Problem finding games for Betr")
                return
        except AttributeError as ae:
            print(f"Problem finding games for Betr\nError: {ae}")
            return

        for li_game in containers:
            try:
                team_and_odds_element = li_game.find_all("button", class_="MuiButton-disableElevation")
                if not team_and_odds_element:
                    continue
                teams = []
                odds = []
                for team_odds in team_and_odds_element:
                    team_and_odds = team_odds.get_text().strip()
                    match = re.match(r"(.+?)(\d+\.\d+)", team_and_odds)
                    if match:
                        team_name = match.group(1).strip()
                        odds_value = float(match.group(2).strip())
                        teams.append(team_name)
                        odds.append(odds_value)
            except (IndexError, AttributeError) as e:
                print(f"Problem getting data for a game with sport id: {sport_id} on Betr\nError: {e}")
                continue
            home = teams[0]
            away = teams[1]
            home_odds = odds[0]
            away_odds = odds[1]
            for game in stored_games:
                self.update_h2h_market(home, away, game, 6, home_odds, away_odds)
