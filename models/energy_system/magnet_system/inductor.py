"""
    https://en.wikipedia.org/wiki/Inductor
"""


class Inductor:
    is_on: bool

    storable_energy: float
    electromotive_force: float

    starter_current: float
    output_current: float
    current_loss: float

    q_factor: float
