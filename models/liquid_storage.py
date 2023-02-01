class LiquidStorage:
    def __init__(self, name: str = 'liquid_storage'):
        self.name = name

        self.durability = 100.0
        self.liquid_level = 100.0

    durability: float
    liquid_level: float
