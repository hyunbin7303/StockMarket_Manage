import unittest
import sys
from stock.stock_calculator import stock_calculator

class TestStockCalculator(unittest.TestCase):

    def test_stock_calculator(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


    def test_stock_peg(self):
        stock_calculator.get_peg("NVDA", "")
        print('testing PEG')
        assert ("")



if __name__ =='__main__':
    test_stock_calculator()
    test_stock_peg()
    unittest.main()