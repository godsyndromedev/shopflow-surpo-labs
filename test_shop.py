import unittest

from shop import add_product, available


class CatalogTests(unittest.TestCase):
    def test_add_product_increases_stock(self) -> None:
        catalog: dict[str, int] = {}
        add_product(catalog, "BOOK-001", 3)
        add_product(catalog, "BOOK-001", 2)
        self.assertEqual(available(catalog, "BOOK-001"), 5)

    def test_add_product_rejects_non_positive_quantity(self) -> None:
        with self.assertRaises(ValueError):
            add_product({}, "BOOK-001", 0)


if __name__ == "__main__":
    unittest.main()
