#  sandbox
from db.db import DB
from scrapers.betr_scraper import BetrScraper
from scrapers.boombet_scraper import BoombetScraper
from scrapers.games_scraper import GamesScraper
from scrapers.neds_scraper import NedsScraper
from scrapers.pointsbet_scraper import PointsbetScraper
from scrapers.sportsbet_scraper import SportsbetScraper
from scrapers.tab_scraper import TabScraper



def calculate_arbs_soccer(sport_id):
    db = DB()
    upcoming_games = db.get_upcoming_games(sport_id)
    all_games_with_arb_percent = []
    for game in upcoming_games:
        markets = db.get_all_markets_by_game(game["id"])
        for outer in markets:
            outer_opt1_win_percentage = 1 / outer["option_1_odds"]
            for inner in markets:
                if outer["game_id"] == inner["game_id"] and outer["bookmaker"] == inner["bookmaker"]:
                    continue
                inner_opt2_win_percentage = 1 / inner["option_2_odds"]
                for middle in markets:  # draw
                    middle_opt3_win_percentage = 1 / middle["option_3_odds"]
                    arb_sum = round(outer_opt1_win_percentage + inner_opt2_win_percentage + middle_opt3_win_percentage, 3)
                    all_games_with_arb_percent.append({
                        "date": game["game_date"],
                        "time": game["game_time"],
                        "sport": outer["sport"],
                        "book_1": outer["bookmaker"],
                        "team_1": outer["option_1"],
                        "odds_team_1": outer["option_1_odds"],
                        "book_2": inner["bookmaker"],
                        "team_2": inner["option_2"],
                        "odds_team_2": inner["option_2_odds"],
                        "odds_draw": middle["option_3_odds"],
                        "book_3": middle["bookmaker"],
                        "arbitrage_sum": arb_sum,
                        "profitable": True if arb_sum < 1 else False,
                        "book_1_url": outer[f"url_{sport_id}"],
                        "book_2_url": inner[f"url_{sport_id}"],
                        "book_3_url": middle[f"url_{sport_id}"]
                    })
    all_games_with_arb_percent.sort(key=lambda item: item["arbitrage_sum"])
    return all_games_with_arb_percent

def test():
    pass
    # gs = GamesScraper()
    # gs.get_upcoming_sport_schedule(2)

    # ned = NedsScraper()
    # ned.scrape_h2h(4)

    # sb = SportsbetScraper()
    # sb.scrape_h2h(4)
    # tab = TabScraper()
    # tab.scrape_h2h(4)

    # pb = PointsbetScraper()
    # pb.scrape_h2h(4)

    # bb = BoombetScraper()
    # bb.scrape_h2h(4)
    #
    # betr = BetrScraper()
    # betr.scrape_h2h(4)

calculate_arbs_soccer(4)
