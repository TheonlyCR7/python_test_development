import unittest
from ddt import ddt, data, unpack

@ddt
class BasicTestCase(unittest.TestCase):
    @data(['张三', '18'], ['李四', '19'])  # 设置@data装饰器，并将同一组参数写进中括号[]
    @unpack  # 设置@unpack装饰器顺序解包，缺少解包则相当于name = ['张三', '18']
    def test(self, name, age):
        print('姓名:', name, '年龄:', age)