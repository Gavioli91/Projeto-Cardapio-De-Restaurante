from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    item = Ingredient("ovo")
    instance_pancake = Dish('panqueca', 20.00)
    instance_pizza = Dish('pizza', 45.00)

    with pytest.raises(TypeError):
        Dish('panqueca', 'lasanha')
    with pytest.raises(ValueError):
        Dish('panqueca', 0)

    assert instance_pancake.__eq__(instance_pancake) is True
    assert instance_pancake.__eq__(instance_pizza) is False
    assert hash(instance_pancake) == hash(instance_pancake)
    assert hash(instance_pancake) != hash(instance_pizza)
    assert repr(instance_pancake) == "Dish('panqueca', R$20.00)"

    instance_pancake.add_ingredient_dependency(item, 1)
    assert instance_pancake.name == 'panqueca'
    assert instance_pancake.get_restrictions() == {Restriction.ANIMAL_DERIVED}
    assert instance_pancake.get_ingredients() == {Ingredient("ovo")}
