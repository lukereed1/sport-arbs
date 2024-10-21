import sqlite3
from flask import Flask, render_template, url_for, redirect
from db.db import DB
from scrapers.games_scraper import GamesScraper

app = Flask(__name__)


@app.route("/")
def index():
    db = DB()
    games = db.get_all_games()
    return render_template("index.html", games=games)


@app.route("/scrape_upcoming_games", methods=["POST"])
def scrape_upcoming_games():
    scraper = GamesScraper()
    scraper.get_nfl_games()
    return redirect(url_for('index'))


