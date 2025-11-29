import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def first_category():
    return Category(
        name="category_n",
        description="category_dec",
        products=[
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="category_n2",
        description="category_dec2",
        products=[
            Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7),
        ],
    )


@pytest.fixture
def product():
    return Product(
        name="product_n",
        description="product_dec",
        price=12.2,
        quantity=10,
    )


@pytest.fixture
def product_with1():
    return Product(
        name="product_n1",
        description="product_dec",
        price=12.1,
        quantity=11,
    )


@pytest.fixture
def product_with2():
    return Product(
        name="product_n2",
        description="product_dec",
        price=12.2,
        quantity=12,
    )


@pytest.fixture
def product_iterator(second_category):
    return ProductIterator(second_category)
