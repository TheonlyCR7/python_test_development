import unittest
from ddt import ddt, data, unpack

def read_dict():
    lis = []  # 以列表形式存储数据，以便传入@data区域
    with open('dict', 'r', encoding='utf-8') as file:
        for line in file.readlines():  # 循环按行读取文件的每一行
            lis.append(line.strip('\n').split(','))
        return lis  # 将列表返回，作为@data接收的内容
@ddt
class BasicTestCase(unittest.TestCase):
    @data(*read_dict())
    @unpack
    def test(self, name, age):  # 设置两个接收参数的形参
        print('姓名为:', name, '年龄为:', age)