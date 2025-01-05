import unittest
import Testcase    # 导入测试用例，这里模块名是自己建立的测试用例文件名

suite = unittest.TestSuite()    # 类的实例化！！！要加括号才是实例化

# 一次添加单个测试用例
suite.addTest(Testcase.Testcase1_login('test1'))     # 添加第1类测试用例中的第1个测试用例
suite.addTest(Testcase.Testcase2_data('test1'))     # 添加第2类测试用例中的第1次测试用例

if __name__ == '__main__':
    r = unittest.TextTestRunner()     # 类的实例化！！！要加括号才是实例化，文本运行测试
    r.run(suite)  # 运行测试套件