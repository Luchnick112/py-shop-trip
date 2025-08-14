import json
import os
from app.shops import Shops
from app.cars import Cars
from app.customers import Customers


def shop_trip() -> None:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_cost = config["FUEL_PRICE"]
    shops = [Shops(shop["name"], shop["location"], shop["products"])
             for shop in config["shops"]]
    customers = [Customers(custom["name"], custom["product_cart"],
                           custom["location"], custom["money"],
                           Cars(custom["car"]["brand"],
                                custom["car"]["fuel_consumption"]))
                 for custom in config["customers"]]

    for cust in customers:
        print(f"{cust.name} has {cust.money} dollars")
        trip_cost_dict = {}
        for shop in shops:
            distance = cust.distance_to_shop(shop.location)
            trip_cost = cust.car.cost_trip(distance, fuel_cost)
            total_expenses = (
                shop.products_cost(cust.product_cart) + trip_cost
            )
            trip_cost_dict[shop.name] = total_expenses
            print(f"{cust.name}'s trip to the {shop.name} "
                  f"costs {total_expenses}")

        cheap_value = min(trip_cost_dict.values())
        cheap_shop_name = ""
        for key, value in trip_cost_dict.items():
            if value == cheap_value:
                cheap_shop_name = key

        for shop in shops:
            if shop.name == cheap_shop_name:
                cheap_shop = shop

        if cheap_value <= cust.money:
            print(f"{cust.name} rides to {cheap_shop.name}")
            cheap_shop.receipt(cust.name, cust.product_cart)
            print(f"{cust.name} rides home")
            rest = round(cust.money - cheap_value, 2)
            print(f"{cust.name} now has {rest} dollars\n")
        else:
            print(f"{cust.name} doesn't have enough money to make a "
                  f"purchase in any shop")


if __name__ == "__main__":
    shop_trip()
