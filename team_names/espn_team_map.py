from team_names.nba_teams_enum import NBATeam
from team_names.nfl_teams_enum import NFLTeam


def espn_mapping(team, sport_id):
    if sport_id == 1:
        nfl_map = {
            "arizona-cardinals": NFLTeam.ARIZONA_CARDINALS,
            "atlanta-falcons": NFLTeam.ATLANTA_FALCONS,
            "baltimore-ravens": NFLTeam.BALTIMORE_RAVENS,
            "buffalo-bills": NFLTeam.BUFFALO_BILLS,
            "carolina-panthers": NFLTeam.CAROLINA_PANTHERS,
            "chicago-bears": NFLTeam.CHICAGO_BEARS,
            "cincinnati-bengals": NFLTeam.CINCINNATI_BENGALS,
            "cleveland-browns": NFLTeam.CLEVELAND_BROWNS,
            "dallas-cowboys": NFLTeam.DALLAS_COWBOYS,
            "denver-broncos": NFLTeam.DENVER_BRONCOS,
            "detroit-lions": NFLTeam.DETROIT_LIONS,
            "green-bay-packers": NFLTeam.GREEN_BAY_PACKERS,
            "houston-texans": NFLTeam.HOUSTON_TEXANS,
            "indianapolis-colts": NFLTeam.INDIANAPOLIS_COLTS,
            "jacksonville-jaguars": NFLTeam.JACKSONVILLE_JAGUARS,
            "kansas-city-chiefs": NFLTeam.KANSAS_CITY_CHIEFS,
            "las-vegas-raiders": NFLTeam.LAS_VEGAS_RAIDERS,
            "los-angeles-chargers": NFLTeam.LOS_ANGELES_CHARGERS,
            "los-angeles-rams": NFLTeam.LOS_ANGELES_RAMS,
            "miami-dolphins": NFLTeam.MIAMI_DOLPHINS,
            "minnesota-vikings": NFLTeam.MINNESOTA_VIKINGS,
            "new-england-patriots": NFLTeam.NEW_ENGLAND_PATRIOTS,
            "new-orleans-saints": NFLTeam.NEW_ORLEANS_SAINTS,
            "new-york-giants": NFLTeam.NEW_YORK_GIANTS,
            "new-york-jets": NFLTeam.NEW_YORK_JETS,
            "philadelphia-eagles": NFLTeam.PHILADELPHIA_EAGLES,
            "pittsburgh-steelers": NFLTeam.PITTSBURGH_STEELERS,
            "san-francisco-49ers": NFLTeam.SAN_FRANCISCO_49ERS,
            "seattle-seahawks": NFLTeam.SEATTLE_SEAHAWKS,
            "tampa-bay-buccaneers": NFLTeam.TAMPA_BAY_BUCCANEERS,
            "tennessee-titans": NFLTeam.TENNESSEE_TITANS,
            "washington-commanders": NFLTeam.WASHINGTON_COMMANDERS
        }
        return nfl_map[team].value

    elif sport_id == 2:
        nba_map = {
            "atlanta-hawks": NBATeam.ATLANTA_HAWKS,
            "boston-celtics": NBATeam.BOSTON_CELTICS,
            "brooklyn-nets": NBATeam.BROOKLYN_NETS,
            "charlotte-hornets": NBATeam.CHARLOTTE_HORNETS,
            "chicago-bulls": NBATeam.CHICAGO_BULLS,
            "cleveland-cavaliers": NBATeam.CLEVELAND_CAVALIERS,
            "dallas-mavericks": NBATeam.DALLAS_MAVERICKS,
            "denver-nuggets": NBATeam.DENVER_NUGGETS,
            "detroit-pistons": NBATeam.DETROIT_PISTONS,
            "golden-state-warriors": NBATeam.GOLDEN_STATE_WARRIORS,
            "houston-rockets": NBATeam.HOUSTON_ROCKETS,
            "indiana-pacers": NBATeam.INDIANA_PACERS,
            "la-clippers": NBATeam.LA_CLIPPERS,
            "los-angeles-lakers": NBATeam.LOS_ANGELES_LAKERS,
            "memphis-grizzlies": NBATeam.MEMPHIS_GRIZZLIES,
            "miami-heat": NBATeam.MIAMI_HEAT,
            "milwaukee-bucks": NBATeam.MILWAUKEE_BUCKS,
            "minnesota-timberwolves": NBATeam.MINNESOTA_TIMBERWOLVES,
            "new-orleans-pelicans": NBATeam.NEW_ORLEANS_PELICANS,
            "new-york-knicks": NBATeam.NEW_YORK_KNICKS,
            "oklahoma-city-thunder": NBATeam.OKLAHOMA_CITY_THUNDER,
            "orlando-magic": NBATeam.ORLANDO_MAGIC,
            "philadelphia-76ers": NBATeam.PHILADELPHIA_76ERS,
            "phoenix-suns": NBATeam.PHOENIX_SUNS,
            "portland-trail-blazers": NBATeam.PORTLAND_TRAIL_BLAZERS,
            "sacramento-kings": NBATeam.SACRAMENTO_KINGS,
            "san-antonio-spurs": NBATeam.SAN_ANTONIO_SPURS,
            "toronto-raptors": NBATeam.TORONTO_RAPTORS,
            "utah-jazz": NBATeam.UTAH_JAZZ,
            "washington-wizards": NBATeam.WASHINGTON_WIZARDS
        }
        return nba_map[team].value




