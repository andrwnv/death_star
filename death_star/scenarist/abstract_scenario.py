from abc import abstractmethod

from queue import Queue


class AbstractAction:
    def __init__(self, name: str) -> None:
        self._name = name

    @abstractmethod
    def __call__(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_end(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_extra_action(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def period(self) -> float:
        return self._period

    def name(self) -> str:
        return self._name

    _name: str = ""


class AbstractScenario:
    def __init__(self) -> None:
        self._action_queue = Queue()

    @abstractmethod
    def is_end(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_win(self) -> bool | None:
        raise NotImplementedError

    @abstractmethod
    def next_action_period(self) -> float:
        raise NotImplementedError

    def push_action(self, action: AbstractAction) -> None:
        self._action_queue.put_nowait(action)

    def next_action(self) -> AbstractAction | None:
        if self._action_queue.empty():
            return None
        return self._action_queue.get_nowait()

    _action_queue: Queue[AbstractAction]
