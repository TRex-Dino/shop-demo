import unittest

from orders import calculate_total


class CouponTest(unittest.TestCase):
    def test_coupon_reduces_total(self):
        # 2 x 3000 = 6000, купон 10% -> 5400, доставка бесплатная
        self.assertEqual(calculate_total([(3000, 2)], coupon_percent=10), 5400)

    def test_delivery_counted_after_discount(self):
        # 5000, купон 10% -> 4500 < 5000, значит доставка платная: 4800
        self.assertEqual(calculate_total([(5000, 1)], coupon_percent=10), 4800)

    def test_without_coupon(self):
        self.assertEqual(calculate_total([(1000, 1)]), 1300)


if __name__ == "__main__":
    unittest.main()
