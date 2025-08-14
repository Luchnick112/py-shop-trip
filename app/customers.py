import math
from app.cars import Cars


class Customers:
    def __init__(self, name: str, product_cart: dict, location: list,
                 money: float, car: Cars) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = tuple(location)
        self.money = money
        self.car = car
        self.home_location = self.location

    def distance_to_shop(self, shop_location: tuple) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location
        distance = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
        return distance
