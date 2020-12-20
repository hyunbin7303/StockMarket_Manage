
import unittest
from stock.stock_manage import get_data

class TestStockManageMethods(unittest.TestCase):
    
    def test_getData(self):
        get_data('NVDA','print')



