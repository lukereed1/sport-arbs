import asyncio
from datetime import datetime, timedelta

from scrapers.bookie_scraper import BookieScraper
from team_names.pointsbet_team_map import pointsbet_mapping
from util import get_soup_playwright_async


class PointsbetScraper(BookieScraper):
    def __init__(self):
        super().__init__()
        self.SPORT_URLS = {
            1: "https://pointsbet.com.au/sports/american-football/NFL",
            2: "https://pointsbet.com.au/sports/basketball/NBA",
            3: "https://pointsbet.com.au/sports/ice-hockey/NHL",
            4: "https://pointsbet.com.au/sports/soccer/English-Premier-League",
        }

    def scrape_h2h(self, sport_id):
        print(f"Scraping Sport: {sport_id} Odds for Pointsbet")
        stored_games = self.db.get_upcoming_games(sport_id)
        if len(stored_games) == 0:
            print("No games scheduled")
            return
        soup = asyncio.run(get_soup_playwright_async(self.SPORT_URLS[sport_id]))

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
                odds_boxes = li_game.find_all("span", class_="f11v6oas f1xlhiok")
                if sport_id != 4:
                    if len(odds_boxes) != 6:
                        continue
                    h2h_odds = [box.get_text() for box in odds_boxes if box.find_previous_sibling() is None]
                    team_names = li_game.find_all("div", class_="fddsvlq")
                    home_odds = h2h_odds[1]
                    away_odds = h2h_odds[0]
                    home = team_names[1].get_text()
                    away = team_names[0].get_text()
                    for game in stored_games:
                        self.update_h2h_market(home, away, game, 4, home_odds, away_odds)
                else:
                    if len(odds_boxes) != 3:
                        continue
                    team_text = li_game.find("div", class_="f1ybkwy0").get_text()
                    home, away = team_text.split(" v ")
                    home = pointsbet_mapping(home.lower(), 4)
                    away = pointsbet_mapping(away.lower(), 4)
                    home_odds = float(odds_boxes[0].get_text())
                    away_odds = float(odds_boxes[2].get_text())
                    draw_odds = float(odds_boxes[1].get_text())
                    for game in stored_games:
                        self.update_h2h_market(home, away, game, 4, home_odds, away_odds, draw_odds)
            except (IndexError, AttributeError) as e:
                print(f"Problem getting data for a game with sport id: {sport_id} on Pointsbet\nError: {e}")
                continue

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
