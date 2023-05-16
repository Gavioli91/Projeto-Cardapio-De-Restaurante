from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    pancake = 'panqueca'
    pizza = 'pizza'
    instance_pancake = Dish(pancake, 20.00)
    instance_pizza = Dish(pizza, 45.00)

    dish_invalid = 'feijoada'
    dish_not_flexible = 'Dish price must be float'
    value_bigger_of_zero = 'Dish price must be greater then zero'

    with pytest.raises(TypeError, match=dish_not_flexible):
        Dish(dish_invalid, dish_invalid)
    with pytest.raises(ValueError, match=value_bigger_of_zero):
        Dish(dish_invalid, -17)

    assert instance_pancake == instance_pancake
    assert instance_pancake != instance_pizza
    assert hash(instance_pancake) == hash(repr(instance_pancake))
    assert repr(instance_pancake) == f"Dish('{pancake}', R$20.00)"
    assert instance_pancake.name == pancake

    instance_pancake.add_ingredient_dependency(Ingredient('testing'), 50)
    assert instance_pancake.recipe == {Ingredient('testing'): 50}
    assert instance_pancake.get_restrictions() == set()
    assert instance_pancake.get_ingredients() == set(
        instance_pancake.recipe.keys())
