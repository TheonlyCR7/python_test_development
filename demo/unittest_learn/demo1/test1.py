import unittest

class BasicTestCase(unittest.TestCase):  # 设置基础测试类名，继承库中测试用例的属性
    # setUp()和tearDown()是每个测试用例进行时都会执行的测试方法，前者为起始，后者为结束
    # 程序执行流程：setUp()-test1()-tearDown()---setUp()-test2()-tearDown()---
    def setUp(self):  # 复写父类的方法，Pycharm环境左侧有标识，是每一个测试用例都会执行的"起始方法"
        print("测试开始")  # 自定义设置起始步骤

    def tearDown(self):  # 复写父类的方法，Pycharm环境左侧有标识，是每一个测试用例都会执行的"结束方法"
        print("测试结束")  # 自定义设置结束步骤

    def way(self):  # 根据实际需求编写的测试方法
        print("测试方法")


    def testdemo(self):  # 设置测试用例3
        print("testdemo")

    def testcat(self):
        print("testcat")

    def testapple(self):
        print("testapple")

    def test2(self):  # 设置测试用例2
        print("test2")  # 执行程序+断言(自定义断言方法，灵活多变)

    def test1(self):  # 设置测试用例1,命名为test+xxx,会按照test后的阿拉伯数字顺序执行,testdemo也执行，带test都会执行
        print("test1")  # 执行程序+断言(自定义断言方法，灵活多变)


if __name__ == '__main__':  # 设定条件执行unittest的主函数
    unittest.main()  # 调用主函数进行多个测试用例测试