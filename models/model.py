from typing import Dict

from models.energy_system.power_cell import PowerCell
from models.repair_team.team import RepairTeam

class Model:
    def __init__(self):
        self.power_cells = {
            'alpha_cell': PowerCell(),
            'theta_cell': PowerCell()
        }

        self.repair_teams = {
            'alpha_team': RepairTeam(),
            'beta_team': RepairTeam(),
            'gamma_team': RepairTeam()
        }

    power_cells: Dict[str, PowerCell]
    repair_teams: Dict[str, RepairTeam]
