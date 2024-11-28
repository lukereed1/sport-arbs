from team_names.espn_team_map import espn_mapping
from util import get_soup
from bs4 import SoupStrainer
from datetime import datetime
from db.db import DB


class GamesScraper:
    def __init__(self):
        self.SPORT_URLS = {
            1: "https://www.espn.com.au/nfl/schedule",
            2: "https://www.espn.com.au/nba/schedule",
            3: "https://www.espn.com.au/nhl/schedule",
            4: "https://www.espn.com.au/football/fixtures/_/league/eng.1",
        }
    # scrape following week eventually too

    def get_upcoming_sport_schedule(self, sport_id):
        strainer = SoupStrainer("div", attrs={"class": "Wrapper Card__Content overflow-visible"})
        soup = get_soup(self.SPORT_URLS[sport_id], strainer)
        game_containers = soup.find_all(class_="ScheduleTables")

        if not game_containers:
            return

        for container in game_containers:
            # Gets date of games and converts to db format
            try:
                date = container.find("div", class_="Table__Title").get_text()
                date = self.convert_date(date)
            except AttributeError as ae:
                print(f"Problem getting the data for some upcoming games\nError: {ae}")
                continue

            games = container.find_all("tr", class_="Table__TR Table__TR--sm Table__even")
            for game in games:
                # Gets time of games and converts to 24hr format
                time = game.find("td", class_="date__col")
                if time is not None:
                    if time.get_text().strip() == "LIVE":
                        continue
                    time = self.convert_to_24hr(time.get_text())
                else:
                    continue  # Don't get data if games completed

                if sport_id == 4:
                    home_team_links = game.find("td", class_="colspan__col Table__TD").find_all("a", class_="AnchorLink")
                    home_team = home_team_links[1]["href"]
                else:
                    home_team = game.find("td", class_="colspan__col Table__TD").find("a", class_="AnchorLink")["href"]

                if home_team is not None:
                    home_team = home_team.split("/")[6]

                away_team = game.find("td", class_="events__col Table__TD").find("a", class_="AnchorLink")["href"]
                if away_team is not None:
                    away_team = away_team.split("/")[6]

                try:
                    game = {
                        "sport": sport_id,
                        "home": espn_mapping(home_team, sport_id),
                        "away": espn_mapping(away_team, sport_id),
                        "date": date,
                        "time": time
                    }
                except KeyError as ke:
                    print(f"Problem with getting a game for sport: {sport_id}\nError: {ke}")
                    continue

                print(game)
                db = DB()
                if not db.check_game_exists(game):
                    db.insert_game(game)

    @staticmethod
    def convert_date(date):
        arr = date.split(" ")
        month = str(datetime.strptime(arr[1], '%B').month).zfill(2)
        day = arr[2].replace(',', '').zfill(2)
        return f"{arr[3]}-{month}-{day}"

    @staticmethod
    def convert_to_24hr(time):
        return datetime.strptime(time, "%I:%M %p").strftime("%H:%M")
