from abc import ABC, abstractmethod


class Scraper(ABC):
    def get_nfl_games(self):
        print("Hello, world!")


    @abstractmethod
    def scrape_nfl_h2h(self):
        pass

