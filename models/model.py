from typing import Dict

from models.energy_system.power_cell import PowerCell


class Model:
    def __init__(self):
        self.power_cells = {
            'alpha_cell': PowerCell(),
            'theta_cell': PowerCell()
        }

    power_cells: Dict[str, PowerCell]
