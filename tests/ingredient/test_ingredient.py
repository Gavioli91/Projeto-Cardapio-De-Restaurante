from src.models.ingredient import Ingredient


def test_ingredient():
    potato = 'batata'
    tomato = 'tomate'
    instance_batata = Ingredient(potato)
    instance_tomato = Ingredient(tomato)

    assert instance_batata == instance_batata
    assert instance_batata != instance_tomato
    assert repr(instance_batata) == f"Ingredient('{potato}')"
    assert hash(instance_batata) == hash(potato)
    assert instance_batata.restrictions == set()
    assert instance_batata.name == potato
