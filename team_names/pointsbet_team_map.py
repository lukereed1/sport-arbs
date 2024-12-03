from team_names.epl_teams_enum import EPLTeam


def pointsbet_mapping(team, sport_id):
    if sport_id == 4:
        epl_map = {
            "arsenal": EPLTeam.ARSENAL,
            "aston villa": EPLTeam.ASTON_VILLA,
            "brentford": EPLTeam.BRENTFORD,
            "brighton": EPLTeam.BRIGHTON_AND_HOVE_ALBION,
            "chelsea": EPLTeam.CHELSEA,
            "crystal palace": EPLTeam.CRYSTAL_PALACE,
            "everton": EPLTeam.EVERTON,
            "fulham": EPLTeam.FULHAM,
            "leeds-united": EPLTeam.LEEDS_UNITED,
            "leicester": EPLTeam.LEICESTER_CITY,
            "liverpool": EPLTeam.LIVERPOOL,
            "man city": EPLTeam.MANCHESTER_CITY,
            "man utd": EPLTeam.MANCHESTER_UNITED,
            "newcastle": EPLTeam.NEWCASTLE_UNITED,
            "nottm forest": EPLTeam.NOTTINGHAM_FOREST,
            "southampton": EPLTeam.SOUTHAMPTON_FC,
            "tottenham": EPLTeam.TOTTENHAM_HOTSPUR,
            "west ham": EPLTeam.WEST_HAM_UNITED,
            "wolves": EPLTeam.WOLVERHAMPTON_WANDERERS,
            "bournemouth": EPLTeam.AFC_BOURNEMOUTH,
            "ipswich": EPLTeam.IPSWICH_TOWN
        }
        return epl_map[team].value
