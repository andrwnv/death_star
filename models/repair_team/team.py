from typing import List

import names

from models.repair_team.employee import Employee
from models.location import Location
from models.repair_team.employee_grade import EmployeeGrade

from utils.json_serializable import IJsonSerializable


class RepairTeam(IJsonSerializable):
    def __init__(self, name: str = 'repair_team', employees: List[Employee] = []) -> None:
        self.name = name
        self.is_busy = False
        self.current_location = Location.HOME

        self.employees = employees

        if not len(employees):
            for ix in range(15):
                employee = Employee(name=names.get_full_name(), grade=EmployeeGrade.BEGINNER)
                
                if ix % 3 == 0:
                    employee.grade = EmployeeGrade.ENGINEER
                if ix % 6 == 0:
                    employee.grade = EmployeeGrade.LEAD_ENGINEER
                
                self.employees.append(employee)

    name: str
    is_busy: bool

    current_location: Location

    employees: List[Employee]
