import unittest
from ddt import ddt, data

@ddt
class BasicTestCase(unittest.TestCase):
    @data('666', '777', '888')
    def test(self, num):
        num = int(num) + 1
        print('数据驱动的number:', num)