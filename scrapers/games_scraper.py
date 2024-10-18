from util import get_soup
from bs4 import SoupStrainer
from datetime import datetime
import requests


class GamesScraper():
    def get_nfl_games(self):
        url = "https://www.espn.com.au/nfl/schedule"
        strainer = SoupStrainer("div", attrs={"class": "Wrapper Card__Content overflow-visible"})
        soup = get_soup(url, strainer)

        game_containers = soup.find_all(class_="ScheduleTables")

        for daily_games in game_containers:
            # Gets date of games and converts to db format
            date = daily_games.find("div", class_="Table__Title").get_text()
            if date is not None:
                date = self.convert_date(date)


            print(date)
    @staticmethod
    def convert_date(date):
        arr = date.split(" ")
        return f"{arr[3]}-{datetime.strptime(arr[1], '%B').month}-{arr[2].replace(',', '')}"

