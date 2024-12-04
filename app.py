import os
import sqlite3
from flask import Flask, render_template, url_for, redirect, request, abort
from db.db import DB
from scrapers.boombet_scraper import BoombetScraper
from scrapers.pointsbet_scraper import PointsbetScraper
from scrapers.sportsbet_scraper import SportsbetScraper
from scrapers.neds_scraper import NedsScraper
from scrapers.games_scraper import GamesScraper
from scrapers.tab_scraper import TabScraper
from scrapers.betr_scraper import BetrScraper

app = Flask(__name__)

sports = ["NFL", "NBA", "NHL", "EPL"]
# scrapers = [TabScraper()]
scrapers = [SportsbetScraper(), PointsbetScraper(),  NedsScraper(), TabScraper(), BoombetScraper(), BetrScraper()]


def init_db():
    if os.path.exists("./db/odds.db"):
        return

    connection = sqlite3.connect("./db/odds.db")

    with open("./db/schema.sql") as f:
        connection.executescript(f.read())


init_db()


def calculate_arbs(sport_id):
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
                arb_sum = round(outer_opt1_win_percentage + inner_opt2_win_percentage, 3)

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
                    "arbitrage_sum": arb_sum,
                    "profitable": True if arb_sum < 1 else False,
                    "book_1_url": outer[f"url_{sport_id}"],
                    "book_2_url": inner[f"url_{sport_id}"]
                })
          
    all_games_with_arb_percent.sort(key=lambda item: item["arbitrage_sum"])
    return all_games_with_arb_percent[:100]


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
    return all_games_with_arb_percent[:100]  # Top 100


@app.route("/")
def index():
    db = DB()
    games = db.get_all_games()
    games.sort(key=lambda row: (row[4], row[5]))
    return render_template("index.html", games=games)


@app.route("/sport")
def sport():
    db = DB()
    title = request.args.get("sport")
    if title not in sports:
        abort(404)
    sport_id = request.args.get("id")

    if sport_id == '4':
        arbs = calculate_arbs_soccer(sport_id)
    else:
        arbs = calculate_arbs(sport_id)
    return render_template("arb.html", arbs=arbs, title=title)

    # markets = db.get_all_markets(sport_id)
    # return render_template("sport.html", markets=markets, title=title)


@app.route("/scrape_upcoming_games", methods=["POST"])
def scrape_upcoming_games():
    scraper = GamesScraper()
    for i in range(len(sports)):
        scraper.get_upcoming_sport_schedule(i + 1)

    return redirect(url_for('index'))


@app.route("/scrape_markets", methods=["POST"])
def scrape_sport_markets():
    sport = request.args.get("sport")
    sport_id = None
    if sport == "NFL":
        sport_id = 1
    elif sport == "NBA":
        sport_id = 2
    elif sport == "NHL":
        sport_id = 3
    elif sport == "EPL":
        sport_id = 4
    else:
        abort(404)

    for scraper in scrapers:
        scraper.scrape_h2h(sport_id)
    return redirect(url_for('sport', sport=sport, id=sport_id))


if __name__ == "__main__":
    app.run(debug=True)
