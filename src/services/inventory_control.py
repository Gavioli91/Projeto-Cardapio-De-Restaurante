from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Dict:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY):
        self.inventory = read_csv_inventory(inventory_file_path)

    def check_recipe_availability(self, recipe: Recipe):
        for ingr in recipe:
            if ingr not in self.inventory or int(
                recipe[ingr]
            ) > self.inventory[ingr]:
                return False
        return True

    def consume_recipe(self, recipe: Recipe):
        if not recipe:
            return None

        if self.check_recipe_availability(recipe):
            for ingr in recipe:
                self.inventory[ingr] -= recipe[ingr]
            return None
        raise ValueError
