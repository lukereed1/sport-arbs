#  sandbox
from scrapers.games_scraper import GamesScraper


def test():
    scraper = GamesScraper()
    scraper.get_upcoming_sport_schedule(4)


test()