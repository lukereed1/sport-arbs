from util import get_soup
from bs4 import SoupStrainer
from datetime import datetime
from db.db import insert_game
import requests


class GamesScraper():
    def get_nfl_games(self):
        url = "https://www.espn.com.au/nfl/schedule"
        strainer = SoupStrainer("div", attrs={"class": "Wrapper Card__Content overflow-visible"})
        soup = get_soup(url, strainer)
        game_containers = soup.find_all(class_="ScheduleTables")
        all_games = []

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
                    continue  # Don't continue to get home/away teams of completed games

                home_team = game.find("td", class_="colspan__col Table__TD").find("a", class_="AnchorLink")["href"]
                if home_team is not None:
                    home_team = home_team.split("/")[6]
                away_team = game.find("td", class_="events__col Table__TD").find("a", class_="AnchorLink")["href"]
                if away_team is not None:
                    away_team = away_team.split("/")[6]

                game = {
                    "home": home_team,
                    "away": away_team,
                    "date": date,
                    "time": time
                }
                insert_game(game)
        return all_games

    @staticmethod
    def convert_date(date):
        arr = date.split(" ")
        return f"{arr[3]}-{datetime.strptime(arr[1], '%B').month}-{arr[2].replace(',', '')}"

    @staticmethod
    def convert_to_24hr(time):
        return datetime.strptime(time, "%I:%M %p").strftime("%H:%M")