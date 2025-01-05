import unittest

from demo3.HTMLTestReportCN import HTMLTestRunner
class Testcase1_login(unittest.TestCase):
    def test1(self):
        print('执行Testcase1_login的test1')
    def test2(self):
        print('执行Testcase1_login的test2')

class Testcase2_data(unittest.TestCase):
    def test1(self):
        print('执行Testcase2_data的test1')
    def test2(self):
        print('执行Testcase2_data的test2')


# 前文提到过滤装载器的代码
all_tests = unittest.defaultTestLoader.discover(start_dir='./', pattern='Testcase*.py')
runner = unittest.TextTestRunner()
runner.run(all_tests)

# 在过滤装载器代码基础上，改动runner部分生成HTML报告
# 笔者下载了HTMLTestReportCN为例，注意HTMLTestReportCN.py放在同一文件夹下
# 使用语句from HTMLTestReportCN import HTMLTestRunner导入生成HTML的Runner
all_tests = unittest.defaultTestLoader.discover(start_dir='./', pattern='Testcase*.py')
r = open('report_file.html', 'wb')  # 新建一个html文件并以二进制方式写入
runner = HTMLTestRunner(title='测试报告标题', description='测试描述', stream=r)   # 改变Runner,设置报告参数
runner.run(all_tests)