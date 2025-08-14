from datetime import datetime


class Shops:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = tuple(location)
        self.products = products

    def products_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for key, value in product_cart.items():
            cost = value * self.products[key]
            total_cost += cost
        return total_cost

    def receipt(self, customer: str, product_cart: dict) -> None:
        time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        print(f"\nDate: {time}")
        print(f"Thanks, {customer}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for key, value in product_cart.items():
            cost = value * self.products[key]
            total_cost += cost
            print(f"{value} {key}s for {cost: .2f} dollars")
        print(f"Total cost is {total_cost: .2f} dollars")
        print("See you again!\n")
