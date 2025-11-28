from src.product import Product


def test_product_init(product):
    """test product class"""
    assert product.name == "product_n"
    assert product.description == "product_dec"
    assert product.price == 12.2
    assert product.quantity == 10


def test_product_new_product():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product.name = "Samsung Galaxy S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = 180000.0
    product.quantity = 5


def test_product_price(capsys, product):
    product.price = -5
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
