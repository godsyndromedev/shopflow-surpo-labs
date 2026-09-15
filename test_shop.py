import unittest

from shop import add_product, available, export_stock_csv, low_stock, order_total


class CatalogTests(unittest.TestCase):
    def test_add_product_increases_stock(self) -> None:
        catalog: dict[str, int] = {}
        add_product(catalog, "BOOK-001", 3)
        add_product(catalog, "BOOK-001", 2)
        self.assertEqual(available(catalog, "BOOK-001"), 5)

    def test_add_product_rejects_non_positive_quantity(self) -> None:
        with self.assertRaises(ValueError):
            add_product({}, "BOOK-001", 0)

    def test_order_total_uses_price_and_quantity(self) -> None:
        prices = {"BOOK-001": 450.0, "BOOK-002": 300.0}
        items = {"BOOK-001": 2, "BOOK-002": 1}
        self.assertEqual(order_total(prices, items), 1200.0)

    def test_export_stock_csv_has_stable_order(self) -> None:
        catalog = {"BOOK-010": 1, "BOOK-002": 4}
        self.assertEqual(export_stock_csv(catalog), "sku,quantity\nBOOK-002,4\nBOOK-010,1")

    def test_low_stock_uses_threshold(self) -> None:
        catalog = {"BOOK-001": 2, "BOOK-002": 8, "BOOK-003": 3}
        self.assertEqual(low_stock(catalog), ["BOOK-001", "BOOK-003"])


if __name__ == "__main__":
    unittest.main()
