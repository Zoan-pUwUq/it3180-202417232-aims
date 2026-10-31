import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

    def test_add_dvd_until_full(self):
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {i}", cost=10.0)
            self.assertTrue(self.cart.add_dvd(dvd))

        # Thử thêm đĩa thứ 21 -> phải trả về False
        dvd_21 = DigitalVideoDisc("DVD 21", cost=10.0)
        self.assertFalse(self.cart.add_dvd(dvd_21))

    def test_total_cost_with_discount(self):
        # 100 -> giảm 20% = 80
        self.cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))
        self.assertAlmostEqual(self.cart.total_cost_with_discount(20), 80.0)

        # percent 150 -> ValueError
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        d1 = DigitalVideoDisc("Star Wars", cost=24.95)
        d2 = DigitalVideoDisc("Aladdin", cost=18.99)
        self.cart.add_dvd(d1)
        self.cart.add_dvd(d2)
        self.cart.sort_by_title()
        self.assertEqual(self.cart.items[0].title, "Aladdin")
        self.assertEqual(self.cart.items[1].title, "Star Wars")

    def test_sort_by_cost(self):
        d1 = DigitalVideoDisc("Star Wars", cost=24.95)
        d2 = DigitalVideoDisc("Aladdin", cost=18.99)
        self.cart.add_dvd(d1)
        self.cart.add_dvd(d2)
        self.cart.sort_by_cost()
        self.assertEqual(self.cart.items[0].cost, 18.99)
        self.assertEqual(self.cart.items[1].cost, 24.95)



if __name__ == "__main__":
    unittest.main()
