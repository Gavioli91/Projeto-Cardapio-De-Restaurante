from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path):
        self.dishes = set()
        self.df = pd.read_csv(source_path)

        recipes = {}
        for items in self.df.itertuples(index=False):
            dish, price, ingr, amount = items
            if dish not in recipes:
                item_info = Dish(dish, price)
                recipes[dish] = item_info
                self.dishes.add(item_info)
            item_info = Ingredient(ingr)
            recipes[dish].add_ingredient_dependency(item_info, amount)
