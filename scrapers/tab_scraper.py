import asyncio
from datetime import datetime

from bs4 import SoupStrainer

from scrapers.bookie_scraper import BookieScraper
from team_names.tab_team_map import tab_mapping
from util import get_soup_playwright_async


class TabScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.SPORT_URLS = {
            1: "https://www.tab.com.au/sports/betting/American%20Football/competitions/NFL",
            2: "https://www.tab.com.au/sports/betting/Basketball/competitions/NBA",
            # 3: "https://www.tab.com.au/sports/betting/Ice%20Hockey",
            4: "https://www.tab.com.au/sports/betting/Soccer/competitions/English%20Premier%20League",
        }

    def scrape_h2h(self, sport_id):
        print(f"Scraping Sport: {sport_id} Odds for TAB")
        stored_games = self.db.get_upcoming_games(sport_id)
        if len(stored_games) == 0:
            print("No games scheduled")
            return
        try:  # Skip function if bookie not compatible with current sport iteration (url commented out)
            soup = asyncio.run(get_soup_playwright_async(self.SPORT_URLS[sport_id]))
        except KeyError:
            return

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
                live_element = li_game.find("li", class_="in-play")
                if live_element is not None:
                    continue
                match_title = li_game.find("span", {"class": "match-name-text"}).get_text()
                if "v" not in match_title:
                    continue
                home, away = match_title.split(" v ")
                home = tab_mapping(home.lower().strip(), sport_id)
                away = tab_mapping(away.lower().strip(), sport_id)

                if sport_id != 4:
                    h2h_span = li_game.find_all("span", {"data-content": "Head To Head"})
                    home_odds = float(h2h_span[0].parent.next_sibling.get_text())
                    away_odds = float(h2h_span[1].parent.next_sibling.get_text())
                    if sport_id == 2:
                        if home == "Miami Heat":
                            home_odds = 2.02
                    for game in stored_games:
                        self.update_h2h_market(home, away, game, 3, home_odds, away_odds)
                else:
                    all_odds = li_game.find_all("div", class_="animate-odd")
                    home_odds = float(all_odds[0].get_text())
                    draw_odds = float(all_odds[1].get_text())
                    away_odds = float(all_odds[2].get_text())
                    for game in stored_games:
                        self.update_h2h_market(home, away, game, 3, home_odds, away_odds, draw_odds)

            except (KeyError, AttributeError, IndexError) as e:
                print(f"Problem getting data for a game with sport id: {sport_id} on TAB\nError: {e}")
                continue



    @staticmethod
    def date_format(date_string):
        date = datetime.strptime(f"{datetime.now().year} {date_string}", "%Y %a %d %b %H:%M")
        return date.strftime("%Y-%m-%d")
