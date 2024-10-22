from team_names.NFLteams import espn_mapping
from util import get_soup
from bs4 import SoupStrainer
from datetime import datetime
from db.db import DB
from team_names import NFLteams

class GamesScraper:
    def __init__(self):
        self.NFL_URL = "https://www.espn.com.au/nfl/schedule/_/week/8/year/2024/seasontype/2" #  for testing
        # https://www.espn.com.au/nfl/schedule

    def get_nfl_games(self):
        strainer = SoupStrainer("div", attrs={"class": "Wrapper Card__Content overflow-visible"})
        soup = get_soup(self.NFL_URL, strainer)
        game_containers = soup.find_all(class_="ScheduleTables")

        if not game_containers:
            return

        for container in game_containers:
            # Gets date of games and converts to db format
            date = container.find("div", class_="Table__Title").get_text()
            if date is not None:
                date = self.convert_date(date)

            games = container.find_all("tr", class_="Table__TR Table__TR--sm Table__even")
            for game in games:
                # Gets time of games and converts to 24hr format
                time = game.find("td", class_="date__col")
                if time is not None:
                    time = self.convert_to_24hr(time.get_text())
                else:
                    continue  # Don't get data if games completed

                home_team = game.find("td", class_="colspan__col Table__TD").find("a", class_="AnchorLink")["href"]
                if home_team is not None:
                    home_team = home_team.split("/")[6]
                away_team = game.find("td", class_="events__col Table__TD").find("a", class_="AnchorLink")["href"]
                if away_team is not None:
                    away_team = away_team.split("/")[6]

                game = {
                    "sport": 1,
                    "home": espn_mapping(home_team),
                    "away": espn_mapping(away_team),
                    "date": date,
                    "time": time
                }

                db = DB()
                if not db.check_game_exists(game):
                    db.insert_game(game)

    @staticmethod
    def convert_date(date):
        arr = date.split(" ")
        return f"{arr[3]}-{datetime.strptime(arr[1], '%B').month}-{arr[2].replace(',', '')}"

    @staticmethod
    def convert_to_24hr(time):
        return datetime.strptime(time, "%I:%M %p").strftime("%H:%M")