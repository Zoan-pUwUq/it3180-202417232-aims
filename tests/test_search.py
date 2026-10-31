import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95),
            DigitalVideoDisc("Aladdin", "Animation", cost=18.99),
        ]

    def test_search_by_title_found(self):
        results = search_by_title(self.dvds, "Star")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Star Wars")

    def test_search_by_title_not_found(self):
        results = search_by_title(self.dvds, "Nonexistent")
        self.assertEqual(len(results), 0)

    def test_search_by_category(self):
        results = search_by_category(self.dvds, "animation")
        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main()
