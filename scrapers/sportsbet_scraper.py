from util import get_soup
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class SportsbetScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.NFL_URL = "https://www.sportsbet.com.au/betting/american-football/nfl"

    def scrape_nfl_h2h(self):
        print("Scraping NFL H2H Odds for Sportsbet")
        games = self.db.get_upcoming_games(1)
        strainer = SoupStrainer("div", attrs={"data-automation-id": "competition-matches-container"})
        soup = get_soup(self.NFL_URL, strainer)
        game_containers = soup.find_all("div", class_="groupTitleContainerDesktop_fukjuk5 groupTitleExtra_f1r0fg9l")
        if not game_containers:
            return
        for container in game_containers:
            date = container.find("time").get('datetime')
            if date is None:
                continue

            for game in games:
                if game['game_date'] != date:
                    continue

                curr_date_games_list = container.next_sibling.find_all("li")
                if not curr_date_games_list:
                    continue
                for li_game in curr_date_games_list:
                    away = li_game.find("div", {"data-automation-id": "participant-one"}).get_text()
                    home = li_game.find("div", {"data-automation-id": "participant-two"}).get_text()
                    if away is None or home is None:
                        continue

                    odds = li_game.find_all("span", class_="size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9")
                    home_odds = float(odds[1].get_text())
                    away_odds = float(odds[0].get_text())
                    if home_odds is None or away_odds is None:
                        continue

                    self.update_db_h2h_market(home, away, game, 1, home_odds, away_odds)