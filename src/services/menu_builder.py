import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        menu_dishes = []

        for recipes in self.menu_data.dishes:
            items = {
                'dish_name': recipes.name,
                'ingredients': recipes.get_ingredients(),
                'price': recipes.price,
                'restrictions': recipes.get_restrictions(),
            }
            if restriction not in recipes.get_restrictions(
            ) and self.inventory.check_recipe_availability(recipes.recipe):
                menu_dishes.append(items)
        return pd.DataFrame(menu_dishes)
