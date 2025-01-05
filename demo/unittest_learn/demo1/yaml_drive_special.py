import unittest
from ddt import ddt, file_data

@ddt
class BasicTestCase(unittest.TestCase):
    @file_data('dict_special.yml')
    def test(self, **cdata):  # Python中可变参数传递的知识：**按对象顺序执行
        print('姓名是：', cdata['name'], '年龄为：', cdata['age'])    # 通过对象访问语法即可调用