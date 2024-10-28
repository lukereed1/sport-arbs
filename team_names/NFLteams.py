from enum import Enum


class NFLTeam(Enum):
    ARIZONA_CARDINALS = "Arizona Cardinals"
    ATLANTA_FALCONS = "Atlanta Falcons"
    BALTIMORE_RAVENS = "Baltimore Ravens"
    BUFFALO_BILLS = "Buffalo Bills"
    CAROLINA_PANTHERS = "Carolina Panthers"
    CHICAGO_BEARS = "Chicago Bears"
    CINCINNATI_BENGALS = "Cincinnati Bengals"
    CLEVELAND_BROWNS = "Cleveland Browns"
    DALLAS_COWBOYS = "Dallas Cowboys"
    DENVER_BRONCOS = "Denver Broncos"
    DETROIT_LIONS = "Detroit Lions"
    GREEN_BAY_PACKERS = "Green Bay Packers"
    HOUSTON_TEXANS = "Houston Texans"
    INDIANAPOLIS_COLTS = "Indianapolis Colts"
    JACKSONVILLE_JAGUARS = "Jacksonville Jaguars"
    KANSAS_CITY_CHIEFS = "Kansas City Chiefs"
    LAS_VEGAS_RAIDERS = "Las Vegas Raiders"
    LOS_ANGELES_CHARGERS = "Los Angeles Chargers"
    LOS_ANGELES_RAMS = "Los Angeles Rams"
    MIAMI_DOLPHINS = "Miami Dolphins"
    MINNESOTA_VIKINGS = "Minnesota Vikings"
    NEW_ENGLAND_PATRIOTS = "New England Patriots"
    NEW_ORLEANS_SAINTS = "New Orleans Saints"
    NEW_YORK_GIANTS = "New York Giants"
    NEW_YORK_JETS = "New York Jets"
    PHILADELPHIA_EAGLES = "Philadelphia Eagles"
    PITTSBURGH_STEELERS = "Pittsburgh Steelers"
    SAN_FRANCISCO_49ERS = "San Francisco 49ers"
    SEATTLE_SEAHAWKS = "Seattle Seahawks"
    TAMPA_BAY_BUCCANEERS = "Tampa Bay Buccaneers"
    TENNESSEE_TITANS = "Tennessee Titans"
    WASHINGTON_COMMANDERS = "Washington Commanders"


def espn_mapping(team):
    map = {
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
    return map[team].value


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

