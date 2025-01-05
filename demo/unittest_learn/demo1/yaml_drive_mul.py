import unittest
from ddt import ddt, file_data
@ddt
class BasicTestCase(unittest.TestCase):
    @file_data('dict.yml')
    def test(self, name, age):  # 设置入口参数名字与数据参数命名相同即可
        print('姓名是：', name, '年龄为：', age)