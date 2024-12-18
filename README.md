# Sport Arbitrage Finder
A Python based web application built with Flask that identifies potential arbitrage opportunities across different sports and bookmakers. It automates the process of scraping game schedules and odds, performing calculations to detect mismatched odds that guarantee profit regardless of the outcome. The results are presented in a table for each sport. Table cells which are highlighted green represent a game where profit can be locked.

## Features
- **Game Scraping:** Scrapes upcoming games across various sports
- **Odds Collecting:** Gathers odds from multiple bookmakers for each available game
- **Arbitrage detection**: Identifies arbitrage opportunities by comparing odds across multiple bookmakers
- **Calculator:** Built in calculator to determine bet size for each outcome when profit is guaranteed (click coloured cell of a table row)

## Images
![arbs](images/arbs.png)
![calc](images/calc.png)
![upcoming](images/upcoming.png)

## Current Sports/Leagues
- NFL
- NBA
- NHL
- EPL

## To-do
- Scrape more books
- Scrape more markets - Line, pick your own line, total points etc
- Scrape more leagues across all sports