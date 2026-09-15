"""Базовая модель каталога учебного интернет-магазина ShopFlow."""


def add_product(catalog: dict[str, int], sku: str, quantity: int) -> None:
    """Добавляет товар или увеличивает его остаток."""
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля")
    catalog[sku] = catalog.get(sku, 0) + quantity


def available(catalog: dict[str, int], sku: str) -> int:
    """Возвращает доступный остаток товара."""
    return catalog.get(sku, 0)


def reserve_product(catalog: dict[str, int], sku: str, quantity: int) -> None:
    """Резервирует товар для заказа и уменьшает свободный остаток."""
    if quantity <= 0:
        raise ValueError("Количество должно быть положительным")
    if available(catalog, sku) < quantity:
        raise ValueError("Недостаточный остаток")
    catalog[sku] -= quantity


def create_order(catalog: dict[str, int], items: dict[str, int]) -> dict[str, int]:
    """Создаёт заказ после проверки всех позиций."""
    for sku, quantity in items.items():
        if available(catalog, sku) < quantity:
            raise ValueError(f"Недостаточный остаток для {sku}")
    for sku, quantity in items.items():
        reserve_product(catalog, sku, quantity)
    return dict(items)


if __name__ == "__main__":
    demo_catalog: dict[str, int] = {}
    add_product(demo_catalog, "BOOK-001", 5)
    print(f"Остаток BOOK-001: {available(demo_catalog, 'BOOK-001')}")
