from abc import ABC, abstractmethod


class BookieScraper(ABC):
    @abstractmethod
    def scrape_nfl_h2h(self):
        pass
