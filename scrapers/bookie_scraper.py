from abc import ABC, abstractmethod


class BookieScraper(ABC):
    def get_nfl_games(self):
        pass

    @abstractmethod
    def scrape_nfl_h2h(self):
        pass

    def hello_word(self):
        print("hello world")