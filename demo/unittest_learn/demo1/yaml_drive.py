from ddt import file_data     # 导入file_data驱动数据
import unittest
from ddt import ddt, data

@ddt
class BasicTestCase(unittest.TestCase):
    @file_data('num.yml')   # 采用文件数据驱动
    def test(self, num):
        print('读取的数字是', num)