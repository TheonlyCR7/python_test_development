import unittest
from ddt import ddt, data

def read_num():
    lis = []    # 以列表形式存储数据，以便传入@data区域
    with open('num', 'r', encoding='utf-8') as file:    # 以只读'r',编码方式为'utf-8'的方式,打开文件'num',并命名为file
        for line in file.readlines():   # 循环按行读取文件的每一行
            lis.append(line.strip('\n'))  # 每读完一行将此行数据加入列表元素，记得元素要删除'/n'换行符！！！
        return lis    # 将列表返回,作为@data接收的内容
@ddt
class BasicTestCase(unittest.TestCase):
    @data(*read_num())  # 入口参数设定为read_num(),因为返回值是列表，所以加*表示逐个读取列表元素
    def test(self, num):
        print('数据驱动的number:', num)