from team_names.sportsbet_team_map import sportsbet_mapping
from util import get_soup
from scrapers.bookie_scraper import BookieScraper
from bs4 import SoupStrainer


class SportsbetScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.SPORT_URLS = {
            1: "https://www.sportsbet.com.au/betting/american-football/nfl",
            2: "https://www.sportsbet.com.au/betting/basketball-us/nba",
            3: "https://www.sportsbet.com.au/betting/ice-hockey-us/nhl-games",
            4: "https://www.sportsbet.com.au/betting/soccer/united-kingdom/english-premier-league",
        }

    def scrape_h2h(self, sport_id):
        print(f"Scraping Sport: {sport_id} Odds for Sportsbet")
        games = self.db.get_upcoming_games(sport_id)
        if games is None:
            return
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
            for game in games:
                curr_date_games_list = container.next_sibling.find_all("li")
                for li_game in curr_date_games_list:
                    try:
                        live_element = li_game.find("div", class_="live_fst4f0d")
                        if live_element is not None:  # Skip live games
                            continue
                        if sport_id != 4:
                            away = li_game.find("div", {"data-automation-id": "participant-one"})
                            home = li_game.find("div", {"data-automation-id": "participant-two"})

                            if away is None or home is None:
                                teams = li_game.find_all("span", class_="size14_f7opyze Endeavour_fhudrb0 "
                                                                        "medium_f1wf24vo"
                                                                        "participant_f1adow81")
                                away = teams[0].get_text().replace("@", "").strip()
                                home = teams[1].get_text().replace("@", "").strip()

                            odds = li_game.find_all("span", class_="size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9")
                            home_odds = float(odds[1].get_text())
                            away_odds = float(odds[0].get_text())
                            self.update_h2h_market(home, away, game, 1, home_odds, away_odds)
                        else:  # soccer
                            home_details = li_game.find("div", class_="outcomeDetailsFirst_fj7k5vv")
                            away_details = li_game.find("div", class_="outcomeDetailsLast_fu8m1aj")
                            draw_details = li_game.find("div", class_="outcomeDetails_fssdpgi outcomeDetails_fssdpgi "
                                                                      "threeOutcomes_flpw9cb")
                            away = home_details.find("span",
                                                     class_="size12_fq5j3k2 normal_fgzdi7m caption_f4zed5e").get_text()
                            away_odds = float(home_details.find("span", class_="size14_f7opyze bold_f1au7gae "
                                                                               "priceTextSize_frw9zm9").get_text())
                            home = away_details.find("span",
                                                     class_="size12_fq5j3k2 normal_fgzdi7m caption_f4zed5e").get_text()
                            home_odds = float(away_details.find("span", class_="size14_f7opyze bold_f1au7gae "
                                                                               "priceTextSize_frw9zm9").get_text())
                            draw_odds = float(draw_details.find("span", class_="size14_f7opyze bold_f1au7gae "
                                                                               "priceTextSize_frw9zm9").get_text())

                            home = sportsbet_mapping(home.lower(), sport_id)
                            away = sportsbet_mapping(away.lower(), sport_id)

                            self.update_h2h_market(home, away, game, 1, home_odds, away_odds, draw_odds)

                    except (AttributeError, IndexError) as e:
                        print(f"Problem getting data for a game with sport id: {sport_id} on Sportsbet\nError: {e}")
