import unittest
import json
from ddt import ddt, data, unpack

def read_dict_json():
    return json.load(open('dictx.json', 'r', encoding='utf-8'))  # 使用json包读取json文件，并作为返回值返回
@ddt
class BasicTestCase(unittest.TestCase):
    @data(*read_dict_json())
    @unpack
    def test(self, name, age):    # 令形参名字和json中命名相同name=name,age=age
        print('姓名:', name, '年龄:', age)