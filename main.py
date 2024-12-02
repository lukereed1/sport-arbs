#  sandbox
from scrapers.games_scraper import GamesScraper
from scrapers.sportsbet_scraper import SportsbetScraper


def test():
    scraper = SportsbetScraper()
    scraper.scrape_h2h(4)

test()
