CREATE TABLE IF NOT EXISTS sports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sport TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sport_id INTEGER NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    game_date DATE NOT NULL,
    game_time TIME NOT NULL,
    FOREIGN KEY (sport_id) REFERENCES sports(id)
);

CREATE TABLE IF NOT EXISTS bookmakers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bookmaker TEXT NOT NULL,
    url_1 TEXT NOT NULL,
    url_2 TEXT NOT NULL,
    url_3 TEXT
);

CREATE TABLE IF NOT EXISTS markets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    market TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS game_markets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL,
    bookmaker_id INTEGER NOT NULL,
    market_id INTEGER NOT NULL,
    option_1 TEXT NOT NULL,
    option_1_odds FLOAT NOT NULL,
    option_2 TEXT,
    option_2_odds FLOAT,
    option_3 TEXT,
    option_3_odds FLOAT,
    FOREIGN KEY (game_id) REFERENCES games(id),
    FOREIGN KEY (bookmaker_id) REFERENCES bookmakers(id),
    FOREIGN KEY (market_id) REFERENCES markets(id)
);

INSERT INTO sports (sport) VALUES ('NFL');
INSERT INTO sports (sport) VALUES ('NBA');
INSERT INTO sports (sport) VALUES ('NHL');
INSERT INTO sports (sport) VALUES ('EPL');


INSERT INTO bookmakers(bookmaker, url_1, url_2, url_3)
VALUES ('Sportsbet', 'https://www.sportsbet.com.au/betting/american-football/nfl',
        'https://www.sportsbet.com.au/betting/basketball-us/nba',
        'https://www.sportsbet.com.au/betting/ice-hockey-us/nhl-games');

INSERT INTO bookmakers(bookmaker, url_1, url_2, url_3)
VALUES ('Neds', 'https://www.neds.com.au/sports/american-football/nfl',
        'https://www.neds.com.au/sports/basketball/usa/nba',
        'https://www.neds.com.au/sports/ice-hockey/usa/nhl');

INSERT INTO bookmakers(bookmaker, url_1, url_2, url_3)
VALUES ('TAB', 'https://www.tab.com.au/sports/betting/American%20Football/competitions/NFL',
        'https://www.tab.com.au/sports/betting/Basketball/competitions/NBA',
        'https://www.tab.com.au/sports/betting/Ice%20Hockey');

INSERT INTO bookmakers(bookmaker, url_1, url_2, url_3)
VALUES ('Pointsbet', 'https://pointsbet.com.au/sports/american-football/NFL',
        'https://pointsbet.com.au/sports/basketball/NBA',
        'https://pointsbet.com.au/sports/ice-hockey/NHL');

INSERT INTO bookmakers(bookmaker, url_1, url_2, url_3)
VALUES ('Boombet', 'https://www.boombet.com.au/sport-menu/Sport/American%20Football/NFL',
        'https://www.boombet.com.au/sport-menu/Sport/Basketball/NBA',
        'https://www.boombet.com.au/sport-menu/Sport/Ice%20Hockey/NHL');

INSERT INTO bookmakers(bookmaker, url_1, url_2, url_3)
VALUES ('Betr', 'https://www.betr.com.au/sports/American-Football/108/United-States-of-America/NFL-Matches/37249',
        'https://www.betr.com.au/sports/Basketball/107/United-States-of-America/NBA-Matches/39251',
        'https://www.betr.com.au/sports/Ice-Hockey/111/United-States-of-America/NHL-Matches/39252');
--INSERT INTO bookmakers(bookmaker) VALUES ('BetDeluxe');
--INSERT INTO bookmakers(bookmaker) VALUES ('Bluebet');
--INSERT INTO bookmakers(bookmaker) VALUES ('EliteBet');

INSERT INTO markets(market) VALUES("H2H");
INSERT INTO markets(market) VALUES("Line");