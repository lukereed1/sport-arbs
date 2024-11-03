from util import get_soup
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class SportsbetScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.SPORT_URLS = {
            1: "https://www.sportsbet.com.au/betting/american-football/nfl",
            2: "https://www.sportsbet.com.au/betting/basketball-us/nba"
        }

    def scrape_h2h(self, sport_id):
        print(f"Scraping Sport: {sport_id} Odds for Sportsbet")
        games = self.db.get_upcoming_games(sport_id)
        strainer = SoupStrainer("div", attrs={"data-automation-id": "competition-matches-container"})
        soup = get_soup(self.SPORT_URLS[sport_id], strainer)

        try:
            game_containers = soup.find_all("div", class_="groupTitleContainerDesktop_fukjuk5 groupTitleExtra_f1r0fg9l")
            if not game_containers:
                print("Problem finding games for Sportsbet")
                return
        except AttributeError as ae:
            print(f"Problem finding games\nError: {ae}")
            return

        for container in game_containers:
            # date = container.find("time").get('datetime')
            for game in games:
                # if game['game_date'] != date:
                #     continue

                curr_date_games_list = container.next_sibling.find_all("li")

                for li_game in curr_date_games_list:
                    try:
                        live_element = li_game.find("div", class_="live_fst4f0d")
                        if live_element is not None:  # Skip live games
                            continue
                        away = li_game.find("div", {"data-automation-id": "participant-one"}).get_text()
                        home = li_game.find("div", {"data-automation-id": "participant-two"}).get_text()

                        odds = li_game.find_all("span", class_="size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9")
                        home_odds = float(odds[1].get_text())
                        away_odds = float(odds[0].get_text())

                        self.update_h2h_market(home, away, game, 1, home_odds, away_odds)
                    except (AttributeError, IndexError) as e:
                        print(f"Problem getting data for a game with sport id: {sport_id} on Sportsbet\nError: {e}")