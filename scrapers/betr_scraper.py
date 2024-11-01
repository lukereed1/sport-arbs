import re

from util import get_soup, get_soup_playwright, get_soup_pyppeteer, get_soup_playwright_async
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer
import asyncio


class BetrScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.NFL_URL = "https://www.betr.com.au/sports/American-Football/108"

    def scrape_nfl_h2h(self):
        print("Scraping NFL H2H Odds for Betr")
        stored_games = self.db.get_upcoming_games(1)
        url = "https://www.betr.com.au/sports/American-Football/108/United-States-of-America/NFL-Matches/37249"
        soup = asyncio.run(get_soup_playwright_async(url))

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
                print(f"Problem getting data for an NFL game on Betr - Game might be live\nError: {e}")
                continue
            home = teams[0]
            away = teams[1]
            home_odds = odds[0]
            away_odds = odds[1]
            for game in stored_games:
                self.update_h2h_market(home, away, game, 6, home_odds, away_odds)
