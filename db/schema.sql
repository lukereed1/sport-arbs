CREATE TABLE sports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sport TEXT NOT NULL
);

CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sport_id INTEGER NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    game_date DATE NOT NULL,
    game_time TIME NOT NULL,
    FOREIGN KEY (sport_id) REFERENCES sports(id)
);

