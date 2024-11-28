from team_names.epl_teams_enum import EPLTeam
from team_names.nba_teams_enum import NBATeam
from team_names.nfl_teams_enum import NFLTeam
from team_names.nhl_teams_enum import NHLTeam


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

    elif sport_id == 3:
        nhl_map = {
            "anaheim-ducks": NHLTeam.ANAHEIM_DUCKS,
            "arizona-coyotes": NHLTeam.ARIZONA_COYOTES,
            "boston-bruins": NHLTeam.BOSTON_BRUINS,
            "buffalo-sabres": NHLTeam.BUFFALO_SABRES,
            "calgary-flames": NHLTeam.CALGARY_FLAMES,
            "carolina-hurricanes": NHLTeam.CAROLINA_HURRICANES,
            "chicago-blackhawks": NHLTeam.CHICAGO_BLACKHAWKS,
            "colorado-avalanche": NHLTeam.COLORADO_AVALANCHE,
            "columbus-blue-jackets": NHLTeam.COLUMBUS_BLUE_JACKETS,
            "dallas-stars": NHLTeam.DALLAS_STARS,
            "detroit-red-wings": NHLTeam.DETROIT_RED_WINGS,
            "edmonton-oilers": NHLTeam.EDMONTON_OILERS,
            "florida-panthers": NHLTeam.FLORIDA_PANTHERS,
            "los-angeles-kings": NHLTeam.LOS_ANGELES_KINGS,
            "minnesota-wild": NHLTeam.MINNESOTA_WILD,
            "montreal-canadiens": NHLTeam.MONTREAL_CANADIENS,
            "nashville-predators": NHLTeam.NASHVILLE_PREDATORS,
            "new-jersey-devils": NHLTeam.NEW_JERSEY_DEVILS,
            "new-york-islanders": NHLTeam.NEW_YORK_ISLANDERS,
            "new-york-rangers": NHLTeam.NEW_YORK_RANGERS,
            "ottawa-senators": NHLTeam.OTTAWA_SENATORS,
            "philadelphia-flyers": NHLTeam.PHILADELPHIA_FLYERS,
            "pittsburgh-penguins": NHLTeam.PITTSBURGH_PENGUINS,
            "san-jose-sharks": NHLTeam.SAN_JOSE_SHARKS,
            "seattle-kraken": NHLTeam.SEATTLE_KRAKEN,
            "st-louis-blues": NHLTeam.ST_LOUIS_BLUES,
            "tampa-bay-lightning": NHLTeam.TAMPA_BAY_LIGHTNING,
            "toronto-maple-leafs": NHLTeam.TORONTO_MAPLE_LEAFS,
            "utah-hockey-club": NHLTeam.UTAH_HOCKEY_CLUB,
            "vancouver-canucks": NHLTeam.VANCOUVER_CANUCKS,
            "vegas-golden-knights": NHLTeam.VEGAS_GOLDEN_KNIGHTS,
            "washington-capitals": NHLTeam.WASHINGTON_CAPITALS,
            "winnipeg-jets": NHLTeam.WINNIPEG_JETS
        }
        return nhl_map[team].value

    elif sport_id == 4:
        epl_map = {
            "arsenal": EPLTeam.ARSENAL,
            "aston-villa": EPLTeam.ASTON_VILLA,
            "brentford": EPLTeam.BRENTFORD,
            "brighton-hove-albion": EPLTeam.BRIGHTON_AND_HOVE_ALBION,
            "chelsea": EPLTeam.CHELSEA,
            "crystal-palace": EPLTeam.CRYSTAL_PALACE,
            "everton": EPLTeam.EVERTON,
            "fulham": EPLTeam.FULHAM,
            "leeds-united": EPLTeam.LEEDS_UNITED,
            "leicester-city": EPLTeam.LEICESTER_CITY,
            "liverpool": EPLTeam.LIVERPOOL,
            "manchester-city": EPLTeam.MANCHESTER_CITY,
            "manchester-united": EPLTeam.MANCHESTER_UNITED,
            "newcastle-united": EPLTeam.NEWCASTLE_UNITED,
            "nottingham-forest": EPLTeam.NOTTINGHAM_FOREST,
            "southampton": EPLTeam.SOUTHAMPTON_FC,
            "tottenham-hotspur": EPLTeam.TOTTENHAM_HOTSPUR,
            "west-ham-united": EPLTeam.WEST_HAM_UNITED,
            "wolverhampton-wanderers": EPLTeam.WOLVERHAMPTON_WANDERERS,
            "afc-bournemouth": EPLTeam.AFC_BOURNEMOUTH,
            "ipswich-town": EPLTeam.IPSWICH_TOWN
        }
        return epl_map[team].value
