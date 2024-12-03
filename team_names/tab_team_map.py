from team_names.epl_teams_enum import EPLTeam
from team_names.nba_teams_enum import NBATeam
from team_names.nfl_teams_enum import NFLTeam
from team_names.nhl_teams_enum import NHLTeam


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
            "san francisco": NFLTeam.SAN_FRANCISCO_49ERS,
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
            "la lakers": NBATeam.LOS_ANGELES_LAKERS,
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
    elif sport_id == 3:
        nhl_map = {
            "anaheim": NHLTeam.ANAHEIM_DUCKS,
            "arizona": NHLTeam.ARIZONA_COYOTES,
            "boston": NHLTeam.BOSTON_BRUINS,
            "buffalo": NHLTeam.BUFFALO_SABRES,
            "calgary": NHLTeam.CALGARY_FLAMES,
            "carolina": NHLTeam.CAROLINA_HURRICANES,
            "chicago": NHLTeam.CHICAGO_BLACKHAWKS,
            "colorado": NHLTeam.COLORADO_AVALANCHE,
            "columbus": NHLTeam.COLUMBUS_BLUE_JACKETS,
            "dallas": NHLTeam.DALLAS_STARS,
            "detroit": NHLTeam.DETROIT_RED_WINGS,
            "edmonton": NHLTeam.EDMONTON_OILERS,
            "florida": NHLTeam.FLORIDA_PANTHERS,
            "los angeles": NHLTeam.LOS_ANGELES_KINGS,
            "minnesota": NHLTeam.MINNESOTA_WILD,
            "montreal": NHLTeam.MONTREAL_CANADIENS,
            "nashville": NHLTeam.NASHVILLE_PREDATORS,
            "new jersey": NHLTeam.NEW_JERSEY_DEVILS,
            "ny islanders": NHLTeam.NEW_YORK_ISLANDERS,
            "ny rangers": NHLTeam.NEW_YORK_RANGERS,
            "ottawa": NHLTeam.OTTAWA_SENATORS,
            "philadelphia": NHLTeam.PHILADELPHIA_FLYERS,
            "pittsburgh": NHLTeam.PITTSBURGH_PENGUINS,
            "san jose": NHLTeam.SAN_JOSE_SHARKS,
            "seattle": NHLTeam.SEATTLE_KRAKEN,
            "st. louis": NHLTeam.ST_LOUIS_BLUES,
            "tampa bay": NHLTeam.TAMPA_BAY_LIGHTNING,
            "toronto": NHLTeam.TORONTO_MAPLE_LEAFS,
            "utah": NHLTeam.UTAH_HOCKEY_CLUB,
            "vancouver": NHLTeam.VANCOUVER_CANUCKS,
            "vegas": NHLTeam.VEGAS_GOLDEN_KNIGHTS,
            "washington": NHLTeam.WASHINGTON_CAPITALS,
            "winnipeg": NHLTeam.WINNIPEG_JETS
        }
        return nhl_map[team].value
    elif sport_id == 4:
        epl_map = {
            "arsenal": EPLTeam.ARSENAL,
            "aston villa": EPLTeam.ASTON_VILLA,
            "brentford": EPLTeam.BRENTFORD,
            "brighton hovealb": EPLTeam.BRIGHTON_AND_HOVE_ALBION,
            "chelsea": EPLTeam.CHELSEA,
            "crystal palace": EPLTeam.CRYSTAL_PALACE,
            "everton": EPLTeam.EVERTON,
            "fulham": EPLTeam.FULHAM,
            "leeds-united": EPLTeam.LEEDS_UNITED,
            "leicester": EPLTeam.LEICESTER_CITY,
            "liverpool": EPLTeam.LIVERPOOL,
            "manchester city": EPLTeam.MANCHESTER_CITY,
            "man united": EPLTeam.MANCHESTER_UNITED,
            "newcastle": EPLTeam.NEWCASTLE_UNITED,
            "nottinghm forest": EPLTeam.NOTTINGHAM_FOREST,
            "southampton": EPLTeam.SOUTHAMPTON_FC,
            "tottenham": EPLTeam.TOTTENHAM_HOTSPUR,
            "west ham": EPLTeam.WEST_HAM_UNITED,
            "wolverhampton": EPLTeam.WOLVERHAMPTON_WANDERERS,
            "bournemouth": EPLTeam.AFC_BOURNEMOUTH,
            "ipswich": EPLTeam.IPSWICH_TOWN
        }
        return epl_map[team].value
