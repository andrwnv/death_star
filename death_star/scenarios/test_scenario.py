from queue import Queue

from random import randrange

from death_star.scenarist.abstract_scenario import AbstractAction, AbstractScenario
from death_star.entities.models.energy_system.battery.battery import Battery


class DebugBreakAction(AbstractAction):
    def __init__(self, name: str, battery: Battery, is_extra: bool = False, period: float = 2.0) -> None:
        super().__init__(name)
        self.__is_extra = is_extra
        self._period = period
        self.__battery = battery

        self.__pre_start()

    def __pre_start(self) -> None:
        for _, capicator in enumerate(self.__battery.capacitors):
            capicator.charge_level = 100.0
            capicator.durability = 100.0

    def __call__(self) -> bool:
        import random

        for capicator in self.__battery.capacitors:
            capicator.durability = round(random.uniform(50.555, 100.0), 2)
            capicator.charge_level = round(random.uniform(30.555, 100.0), 2)

        return True

    def is_end(self) -> bool:
        self.__counter += 1
        return self.__counter > 3

    def is_extra_action(self) -> bool:
        return self.__is_extra

    __is_extra: bool
    __counter = 0
    __battery: Battery = None


class TestScenario(AbstractScenario):
    def __init__(self, model) -> None:
        super().__init__()
        self._model = model

    def is_end(self) -> bool:
        return self._action_queue.qsize() == 0

    def is_win(self) -> bool | None:
        return False

    def next_action_period(self) -> float:
        self._action_queue.put_nowait(DebugBreakAction(
            f"Debug break action {self._prev_cell_name}",
            self._model.power_cells[self._curr_cell_name].battery)
        )

        self._prev_cell_name, self._curr_cell_name = self._curr_cell_name, self._prev_cell_name

        return 3  # 1 action per 5 sec.

    _prev_cell_name = 'alpha_cell'
    _curr_cell_name = 'theta_cell'
