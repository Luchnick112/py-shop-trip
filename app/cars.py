class Cars:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_trip(self, distance: float, fuel_cost: float) -> float:
        return round((self.fuel_consumption / 100)
                     * distance * fuel_cost * 2, 2)
