import asyncio
from datetime import datetime

from team_names.NFLteams import tab_mapping
from util import get_soup_pyppeteer
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class TabScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.NFL_URL = "https://www.tab.com.au/sports/betting/American%20Football/competitions/NFL"

    def scrape_nfl_h2h(self):
        print("Scraping NFL H2H Odds for TAB")
        strainer = SoupStrainer("div", class_="customised-template")
        soup = asyncio.run(get_soup_pyppeteer(self.NFL_URL, strainer))
        stored_games = self.db.get_upcoming_games(1)

        try:
            games_list = soup.find_all("div", class_="template-item")
        except AttributeError as ae:
            print(f"Problem finding games\nError: {ae}")
            return

        for li_game in games_list:
            try:
                date = li_game.find("li", {"data-test": "close-time"}).get_text()
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
                if self.date_format(date) != game['game_date']:
                    continue
                self.update_h2h_market(home, away, game, 3, home_odds, away_odds)
                #
                # if home == game['home_team']:
                #     if away == game['away_team']:
                #         # Gets existing game market if exists for SB H2H
                #         existing_game_market = self.db.check_game_market_exists(game['id'], 3, 1)
                #
                #         # if game market exists, checks odds to see if they require updating
                #         if existing_game_market is not None:
                #             existing_home_odds = existing_game_market['option_1_odds']
                #             existing_away_odds = existing_game_market['option_2_odds']
                #             if existing_home_odds != home_odds or existing_away_odds != away_odds:
                #                 self.db.update_game_market_odds(existing_game_market['id'], home_odds, away_odds)
                #         else:
                #             game_market = {
                #                 "id": game['id'],
                #                 "bookmaker_id": 3,
                #                 "market_id": 1,
                #                 "opt_1": home,
                #                 "opt_1_odds": home_odds,
                #                 "opt_2": away,
                #                 "opt_2_odds": away_odds
                #             }
                #             self.db.insert_game_market(game_market)

    @staticmethod
    def date_format(date_string):
        date = datetime.strptime(f"{datetime.now().year} {date_string}", "%Y %a %d %b %H:%M")
        return date.strftime("%Y-%m-%d")
