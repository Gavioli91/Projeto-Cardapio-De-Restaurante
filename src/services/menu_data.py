from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path):
        self.recipes = set()
        self.df = pd.read_csv(source_path)

        recipes = {}

        for items in self.df.itertuples(index=False):
            dish, price, ingr, amount = items
            if dish not in recipes:
                menu = Dish(dish, price)
                recipes[dish] = menu
                self.recipes.add(menu)
            item_info = Ingredient(ingr)
            recipes[dish].add_ingredient_dependency(item_info, amount)
