import os
import sqlite3
from flask import Flask, render_template, url_for, redirect, request
from db.db import DB
from scrapers.sportsbet_scraper import SportsbetScraper
from scrapers.neds_scraper import NedsScraper
from scrapers.games_scraper import GamesScraper

app = Flask(__name__)
scrapers = [SportsbetScraper(), NedsScraper()]


def init_db():
    if os.path.exists("./db/odds.db"):
        return

    connection = sqlite3.connect("./db/odds.db")

    with open("./db/schema.sql") as f:
        connection.executescript(f.read())


init_db()


@app.route("/")
def index():
    db = DB()
    games = db.get_all_games()
    return render_template("index.html", games=games)


@app.route("/sport")
def sport():
    db = DB()
    title = request.args.get("sport")
    sport_id = request.args.get("id")
    markets = db.get_all_markets(sport_id)
    return render_template("sport.html", markets=markets, title=title)


# make route for individual sports eventually, with a tab for each one on the website
@app.route("/scrape_upcoming_games", methods=["POST"])
def scrape_upcoming_games():
    scraper = GamesScraper()
    scraper.get_nfl_games()
    for scraper in scrapers:
        scraper.scrape_nfl_h2h()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
