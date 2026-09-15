"""Базовая модель каталога учебного интернет-магазина ShopFlow."""


def add_product(catalog: dict[str, int], sku: str, quantity: int) -> None:
    """Добавляет товар или увеличивает его остаток."""
    if quantity <= 0:
        raise ValueError("Количество должно быть положительным")
    catalog[sku] = catalog.get(sku, 0) + quantity


def available(catalog: dict[str, int], sku: str) -> int:
    """Возвращает доступный остаток товара."""
    return catalog.get(sku, 0)


if __name__ == "__main__":
    demo_catalog: dict[str, int] = {}
    add_product(demo_catalog, "BOOK-001", 5)
    print(f"Остаток BOOK-001: {available(demo_catalog, 'BOOK-001')}")
