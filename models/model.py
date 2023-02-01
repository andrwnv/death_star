from typing import Dict

from models.energy_system.power_cell import PowerCell


class Model:
    power_cells: Dict[str, PowerCell]
