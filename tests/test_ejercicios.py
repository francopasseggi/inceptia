from ejercicio1 import GeoAPI
from ejercicio2 import is_product_available
from ejercicio3 import validate_discount_code

def test_is_hot_in_pehuajo():
    assert GeoAPI.is_hot_in_pehuajo() == True

    # Wrong api key, should return False
    GeoAPI.API_KEY = ''
    assert GeoAPI.is_hot_in_pehuajo() == False


def test_is_product_available():
    assert is_product_available("Chocolate", 2) == True
    assert is_product_available("Chocolate", 4) == False
    assert is_product_available("Limon", 1) == False
    assert is_product_available("Limon", 2) == False
    assert is_product_available("Dulce de Leche", 5) == True
    assert is_product_available("Dulce de Leche", 6) == False
    assert is_product_available("Granizado", 10) == True
    assert is_product_available("Granizado", 11) == False
    assert is_product_available("Cerveza", 1) == False


def test_validate_discount_code():
    assert validate_discount_code("primavera2021") == True
    assert validate_discount_code("Verano2021") == True
    assert validate_discount_code("xxxxxxx") == False
