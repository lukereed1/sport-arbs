from team_names.epl_teams_enum import EPLTeam


def neds_mapping(team, sport_id):
    if sport_id == 4:
        epl_map = {
            "arsenal": EPLTeam.ARSENAL,
            "aston villa": EPLTeam.ASTON_VILLA,
            "brentford": EPLTeam.BRENTFORD,
            "brighton & hove albion": EPLTeam.BRIGHTON_AND_HOVE_ALBION,
            "chelsea": EPLTeam.CHELSEA,
            "crystal palace": EPLTeam.CRYSTAL_PALACE,
            "everton fc": EPLTeam.EVERTON,
            "fulham": EPLTeam.FULHAM,
            "leeds-united": EPLTeam.LEEDS_UNITED,
            "leicester city": EPLTeam.LEICESTER_CITY,
            "liverpool": EPLTeam.LIVERPOOL,
            "manchester city": EPLTeam.MANCHESTER_CITY,
            "manchester united": EPLTeam.MANCHESTER_UNITED,
            "newcastle united": EPLTeam.NEWCASTLE_UNITED,
            "nottingham forest": EPLTeam.NOTTINGHAM_FOREST,
            "southampton fc": EPLTeam.SOUTHAMPTON_FC,
            "tottenham hotspur": EPLTeam.TOTTENHAM_HOTSPUR,
            "west ham united": EPLTeam.WEST_HAM_UNITED,
            "wolverhampton wanderers": EPLTeam.WOLVERHAMPTON_WANDERERS,
            "afc bournemouth": EPLTeam.AFC_BOURNEMOUTH,
            "ipswich town": EPLTeam.IPSWICH_TOWN
        }
        return epl_map[team].value
