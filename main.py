#  sandbox
from scrapers.games_scraper import GamesScraper
from scrapers.neds_scraper import NedsScraper
from scrapers.sportsbet_scraper import SportsbetScraper


def test():
    ned = NedsScraper()
    ned.scrape_h2h(4)

    sb = SportsbetScraper()
    sb.scrape_h2h(4)

test()
