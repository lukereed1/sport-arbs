import os
import sqlite3
from flask import Flask, render_template, url_for, redirect
from db.db import DB
from scrapers.SportsbetScraper import SportsbetScraper
from scrapers.games_scraper import GamesScraper

app = Flask(__name__)


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
    markets = db.get_all_markets()
    return render_template("index.html", games=games, markets=markets)


@app.route("/scrape_upcoming_games", methods=["POST"])
def scrape_upcoming_games():
    scraper = GamesScraper()
    scraper.get_nfl_games()
    sb = SportsbetScraper()
    sb.scrape_nfl_h2h()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
