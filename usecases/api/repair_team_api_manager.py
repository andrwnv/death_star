from copy import copy
from typing import Dict, List, Optional

from models.repair_team.team import RepairTeam
from models.location import Location

class RepairTeamApiManager:
    def __init__(self, teams: Dict[str, RepairTeam]) -> None:
        self.__repair_teams = teams

    def team_list(self) -> Dict[str, RepairTeam]:
        return copy(self.__repair_teams)

    def team_info(self, team_name: str) -> Optional[RepairTeam]:
        if team_name not in self.__repair_teams:
            return None
        return copy(self.__repair_teams[team_name])

    def send_team(self, team_name: str, location: Location) -> bool:
        # TODO(andrwnv): add logic

        if team_name not in self.__repair_teams:
            return False
        return True  

    __repair_teams: Dict[str, RepairTeam]
