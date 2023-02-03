from typing import List

from models.repair_team.employee import Employee
from models.location import Location

from utils.json_serializable import IJsonSerializable


class RepairTeam(IJsonSerializable):
    def __init__(self, name: str = 'repair_team', employees: List[Employee] = []) -> None:
        self.name = name
        self.is_busy = False
        self.current_location = Location.HOME
        self.employees = employees

    name: str
    is_busy: bool

    current_location: Location

    employees: List[Employee]
