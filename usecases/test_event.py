from datetime import timedelta, datetime
from usecases.abstract_event import AbstractEvent


class TestEvent(AbstractEvent):
    def __init__(self) -> None:
        super().__init__()

        import uuid
        self._name = str(uuid.uuid4())
        self._description = f'SOME LOOOOOOOOOOOOOOOOOOOOOOOOONG DESCRIIIIIIIIIIIIIIIIIIPTION OF {self._name} xd'
        self._start_time = datetime.now() + timedelta(seconds=5)
        self._duration = timedelta(seconds=5)

    def positive_effect(self) -> None:
        print(f'positive_effect of {self._name}')

    def negative_effect(self) -> None:
        print(f'negative_effect of {self._name}')
