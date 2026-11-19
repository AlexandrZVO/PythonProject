class Product:
    """Товар."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Инициализация товара."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
