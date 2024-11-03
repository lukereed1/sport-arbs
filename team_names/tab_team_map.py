from team_names.nba_teams_enum import NBATeam
from team_names.nfl_teams_enum import NFLTeam


def tab_mapping(team, sport_id):
    if sport_id == 1:
        nfl_map = {
            "arizona": NFLTeam.ARIZONA_CARDINALS,
            "atlanta": NFLTeam.ATLANTA_FALCONS,
            "baltimore": NFLTeam.BALTIMORE_RAVENS,
            "buffalo": NFLTeam.BUFFALO_BILLS,
            "carolina": NFLTeam.CAROLINA_PANTHERS,
            "chicago": NFLTeam.CHICAGO_BEARS,
            "cincinnati": NFLTeam.CINCINNATI_BENGALS,
            "cleveland": NFLTeam.CLEVELAND_BROWNS,
            "dallas": NFLTeam.DALLAS_COWBOYS,
            "denver": NFLTeam.DENVER_BRONCOS,
            "detroit": NFLTeam.DETROIT_LIONS,
            "green bay": NFLTeam.GREEN_BAY_PACKERS,
            "houston": NFLTeam.HOUSTON_TEXANS,
            "indianapolis": NFLTeam.INDIANAPOLIS_COLTS,
            "jacksonville": NFLTeam.JACKSONVILLE_JAGUARS,
            "kansas city": NFLTeam.KANSAS_CITY_CHIEFS,
            "la chargers": NFLTeam.LOS_ANGELES_CHARGERS,
            "la rams": NFLTeam.LOS_ANGELES_RAMS,
            "las vegas": NFLTeam.LAS_VEGAS_RAIDERS,
            "miami": NFLTeam.MIAMI_DOLPHINS,
            "minnesota": NFLTeam.MINNESOTA_VIKINGS,
            "new england": NFLTeam.NEW_ENGLAND_PATRIOTS,
            "new orleans": NFLTeam.NEW_ORLEANS_SAINTS,
            "ny giants": NFLTeam.NEW_YORK_GIANTS,
            "ny jets": NFLTeam.NEW_YORK_JETS,
            "philadelphia": NFLTeam.PHILADELPHIA_EAGLES,
            "pittsburgh": NFLTeam.PITTSBURGH_STEELERS,
            "seattle": NFLTeam.SEATTLE_SEAHAWKS,
            "tampa bay": NFLTeam.TAMPA_BAY_BUCCANEERS,
            "tennessee": NFLTeam.TENNESSEE_TITANS,
            "washington": NFLTeam.WASHINGTON_COMMANDERS
        }
        return nfl_map[team].value
    elif sport_id == 2:
        nba_map = {
            "atlanta": NBATeam.ATLANTA_HAWKS,
            "boston": NBATeam.BOSTON_CELTICS,
            "brooklyn": NBATeam.BROOKLYN_NETS,
            "charlotte": NBATeam.CHARLOTTE_HORNETS,
            "chicago": NBATeam.CHICAGO_BULLS,
            "cleveland": NBATeam.CLEVELAND_CAVALIERS,
            "dallas": NBATeam.DALLAS_MAVERICKS,
            "denver": NBATeam.DENVER_NUGGETS,
            "detroit": NBATeam.DETROIT_PISTONS,
            "golden state": NBATeam.GOLDEN_STATE_WARRIORS,
            "houston": NBATeam.HOUSTON_ROCKETS,
            "indiana": NBATeam.INDIANA_PACERS,
            "la clippers": NBATeam.LA_CLIPPERS,
            "los angeles": NBATeam.LOS_ANGELES_LAKERS,
            "memphis": NBATeam.MEMPHIS_GRIZZLIES,
            "miami": NBATeam.MIAMI_HEAT,
            "milwaukee": NBATeam.MILWAUKEE_BUCKS,
            "minnesota": NBATeam.MINNESOTA_TIMBERWOLVES,
            "new orleans": NBATeam.NEW_ORLEANS_PELICANS,
            "new york": NBATeam.NEW_YORK_KNICKS,
            "oklahoma city": NBATeam.OKLAHOMA_CITY_THUNDER,
            "orlando": NBATeam.ORLANDO_MAGIC,
            "philadelphia": NBATeam.PHILADELPHIA_76ERS,
            "phoenix": NBATeam.PHOENIX_SUNS,
            "portland": NBATeam.PORTLAND_TRAIL_BLAZERS,
            "sacramento": NBATeam.SACRAMENTO_KINGS,
            "san antonio": NBATeam.SAN_ANTONIO_SPURS,
            "toronto": NBATeam.TORONTO_RAPTORS,
            "utah": NBATeam.UTAH_JAZZ,
            "washington": NBATeam.WASHINGTON_WIZARDS
        }

        return nba_map[team].value
