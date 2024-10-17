import lxml
from bs4 import BeautifulSoup, SoupStrainer
import requests


def get_soup(url, strainer):
    response = requests.get(url)
    return BeautifulSoup(response.content, "lxml", parse_only=strainer)

url = "https://www.sportsbet.com.au/betting/american-football/nfl"
strainer = SoupStrainer("div", attrs={"class": "multiMarketCouponContainer_f234ak7"})
soup = get_soup(url, strainer)

game_containers = soup.find_all(class_="multiMarketCouponContainer_f234ak7")


for container in game_containers:
    away = container.find("div", {"data-automation-id": "participant-one"}).get_text()
    home = container.find("div", {"data-automation-id": "participant-two"}).get_text()
    print(f"home: {home}")
    print(f"away: {away}")
    print(" ")