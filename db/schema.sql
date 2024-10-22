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

INSERT INTO sports (sport) VALUES ('NFL');
INSERT INTO sports (sport) VALUES ('NBA');
INSERT INTO sports (sport) VALUES ('NRL');
INSERT INTO sports (sport) VALUES ('AFL');

INSERT INTO games (sport_id, home_team, away_team, game_date, game_time)
VALUES (1, "Team_A", "Team_B", "2024-10-10", "14:13:00");

INSERT INTO games (sport_id, home_team, away_team, game_date, game_time)
VALUES (2, "Team_B", "Team_B", "2024-10-10", "16:13:00");

INSERT INTO games (sport_id, home_team, away_team, game_date, game_time)
VALUES (1, "Team_AC", "Team_B", "2024-10-10", "20:13:00");

