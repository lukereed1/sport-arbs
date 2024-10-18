CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- Add foreign sport id key
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    game_date DATE NOT NULL,
    game_time TIME NOT NULL
)