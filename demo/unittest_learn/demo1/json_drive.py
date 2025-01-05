import unittest
import json
from ddt import ddt, data, unpack

def read_num_json():
    # 使用json包读取json文件，并作为返回值返回，注意读取的文件名
    return json.load(open('num.json', 'r', encoding='utf-8'))
@ddt  # 数据驱动步骤和txt相同
class BasicTestCase(unittest.TestCase):
    # @data(*read_num_json())
    @data(read_num_json())
    @unpack
    def test(self, num):
        print('读取的数字是', num)