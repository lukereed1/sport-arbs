#  sandbox
from scrapers.games_scraper import GamesScraper
from scrapers.neds_scraper import NedsScraper
from scrapers.sportsbet_scraper import SportsbetScraper
from scrapers.tab_scraper import TabScraper


def test():
    # ned = NedsScraper()
    # ned.scrape_h2h(4)
    #
    # sb = SportsbetScraper()
    # sb.scrape_h2h(4)
    tab = TabScraper()
    tab.scrape_h2h(4)


test()
