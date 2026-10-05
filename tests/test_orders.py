import unittest

from orders import calculate_total


class CouponTest(unittest.TestCase):
    def test_coupon_reduces_total(self):
        # 2 x 3000 = 6000, купон 10% -> 5400, доставка бесплатная
        self.assertEqual(calculate_total([(3000, 2)], coupon_percent=10), 5400)


if __name__ == "__main__":
    unittest.main()
