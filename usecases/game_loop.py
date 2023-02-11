from utils.abstract_game_loop import AbstractGameLoop
from utils.event_executor import EventExecutor


class GameLoop(AbstractGameLoop):
    def __init__(self, interval: float, event_executor: EventExecutor, debug_mode: bool = False) -> None:
        super().__init__(interval, event_executor, debug_mode)

    def tick_handler(self) -> None:
        # TODO(andrwnv): add tick logic
        pass
