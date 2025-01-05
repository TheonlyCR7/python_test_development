import unittest
from ddt import ddt, file_data

@ddt
class BasicTestCase(unittest.TestCase):
    @file_data('dict_spe.yml')
    def test(self, **cdata):  # 使用 ** 解包
        print('姓名是：', cdata['person']['name'], '年龄为：', cdata['person']['age'])

