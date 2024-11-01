from team_names.nfl_teams_enum import NFLTeam


def tab_mapping(team):
    map = {
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
    return map[team].value
