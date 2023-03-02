from datetime import datetime, timedelta
from queue import Queue

from models.energy_system.battery.battery import Battery
from models.energy_system.plasma_heater.plasma_heater import PlasmaHeater
from models.model import Model

from usecases.abstract_scenario import AbstractAction, AbstractScenario


class FirstActAction(AbstractAction):
    def __init__(self, name: str, event_executor, model: Model, period: float = 1.0) -> None:
        super().__init__(name)
        self._period = period
        self.__event_executor = event_executor

        self.__start_time = None
        self.__model = model

    def __call__(self) -> bool:
        if not self.__start_time:
            self.__start_time = datetime.now()

        for power_cell in self.__model.power_cells.values():
            plasma_heater = power_cell.plasma_heater
            battery = power_cell.battery

            if plasma_heater.durability >= 90.0:
                for capicator in battery.capacitors:
                    if capicator.durability >= 30:
                        capicator.charge_level += 25.0
                        break

    def is_end(self) -> bool:
        return datetime.now() >= self.__start_time + timedelta(min=3)

    def is_extra_action(self) -> bool:
        return False

    def period(self) -> float:
        return 1.0

    __start_time = None


class BattertScenario(AbstractScenario):
    def __init__(self, model) -> None:
        super().__init__()
        self.__model = model

    def is_end(self) -> bool:
        return self._action_queue.qsize() == 0

    def is_win(self) -> bool | None:
        is_win = True
        for power_cell in self.__model.power_cells.values():
            battery = power_cell.battery

            fine_capicator_dur_count = 0
            for capicator in battery.capacitors:
                if capicator.durability >= 70:
                    fine_capicator_dur_count += 1
            if fine_capicator_dur_count < 20:
                is_win &= False

        return is_win

    def next_action_period(self) -> float:
        if self.__period_list.qsize() == 0:
            return 0

        return self.__period_list.get_nowait()

    __period_list: Queue[float] = [1, 180, 240]
