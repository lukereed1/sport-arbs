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
    url_1 TEXT NOT NULL
--    url_2 TEXT NOT NULL
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
INSERT INTO sports (sport) VALUES ('NRL');
INSERT INTO sports (sport) VALUES ('AFL');


--INSERT INTO games (sport_id, home_team, away_team, game_date, game_time)
--VALUES (1, "Team_A", "Team_B", "2024-10-10", "14:13:00");
--
--INSERT INTO games (sport_id, home_team, away_team, game_date, game_time)
--VALUES (2, "Team_B", "Team_B", "2024-10-10", "16:13:00");
--
--INSERT INTO games (sport_id, home_team, away_team, game_date, game_time)
--VALUES (1, "Team_C", "Team_B", "2024-10-10", "20:13:00");

INSERT INTO bookmakers(bookmaker, url_1) VALUES ('Sportsbet', 'https://www.sportsbet.com.au/betting/american-football/nfl');
INSERT INTO bookmakers(bookmaker, url_1) VALUES ('Neds', 'https://www.neds.com.au/sports/american-football/nfl');
INSERT INTO bookmakers(bookmaker, url_1) VALUES ('TAB', 'https://www.tab.com.au/sports/betting/American%20Football/competitions/NFL');
INSERT INTO bookmakers(bookmaker, url_1) VALUES ('Pointsbet', 'https://pointsbet.com.au/sports/american-football/NFL');
INSERT INTO bookmakers(bookmaker, url_1) VALUES ('Boombet', 'https://www.boombet.com.au/sport-menu/Sport/American%20Football/NFL');
INSERT INTO bookmakers(bookmaker, url_1) VALUES ('Betr', 'https://www.betr.com.au/sports/American-Football/108/United-States-of-America/NFL-Matches/37249');
--INSERT INTO bookmakers(bookmaker) VALUES ('BetDeluxe');
--INSERT INTO bookmakers(bookmaker) VALUES ('Bluebet');

INSERT INTO markets(market) VALUES("H2H");
INSERT INTO markets(market) VALUES("Line");