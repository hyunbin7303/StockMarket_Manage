

# def test_my_add():
#     assert add.my_add([9, 0, 2], [0, 1]) == [9, 0, 2, 0, 1]
#     assert add.my_add('beverly ', 'hills') == 'beverly hills'
# 


import unittest
from stock.stock_manage import get_data

class TestStockManageMethods(unittest.TestCase):
    
    def test_getData(self):
        get_data('NVDA','print')



