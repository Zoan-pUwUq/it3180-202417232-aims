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


if __name__ == "__main__":
    unittest.main()
