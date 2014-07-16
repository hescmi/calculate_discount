import unittest

from calculate_discount import discountGen

class DiscountCalculatorTests(unittest.TestCase):
    def testNormalDiscount(self):
        x = {"ddis" : 30, "pdis" : 10, "price" : 100}
        find_cost = discountGen(x)
        self.assertEqual(find_cost, 60.0)

    def testZeroDiscount(self):
        x = {"ddis" : 0, "pdis" : 0, "price" : 100}
        find_cost = discountGen(x)
        self.assertEqual(find_cost, 100)

    def testFullDiscount(self):
        x = {"ddis" : 100, "pdis" : 100, "price" : 100}
        find_cost = discountGen(x)
        self.assertEqual(find_cost, 1)

if __name__ == "__main__":
    unittest.main()
