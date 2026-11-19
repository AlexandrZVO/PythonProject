from typing import Iterator

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counters() -> Iterator[None]:
    """Сброс счётчиков перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


def test_product_init() -> None:
    """Проверка полей объекта Product."""
    p = Product("Milk", "Fresh milk", 89.50, 10)
    assert p.name == "Milk"
    assert p.description == "Fresh milk"
    assert p.price == 89.50
    assert p.quantity == 10


def test_category_init() -> None:
    """Проверка полей объекта Category."""
    p = Product("Bread", "White bread", 45.0, 20)
    c = Category("Bakery", "Baked goods", [p])
    assert c.name == "Bakery"
    assert c.description == "Baked goods"
    assert isinstance(c.products, list)
    assert c.products == [p]


def test_category_count() -> None:
    """Проверка счётчика категорий."""
    Category("C1", "d1", [])
    Category("C2", "d2", [])
    Category("C3", "d3", [])
    assert Category.category_count == 3


def test_product_count() -> None:
    """Проверка счётчика товаров."""
    p1 = Product("P1", "d", 1.0, 1)
    p2 = Product("P2", "d", 2.0, 2)
    p3 = Product("P3", "d", 3.0, 3)
    Category("C1", "d1", [p1, p2, p3])
    assert Category.product_count == 3
