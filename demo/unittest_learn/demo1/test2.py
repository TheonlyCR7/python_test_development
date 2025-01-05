import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 先存疑
class BasicTestCase(unittest.TestCase):     # 设置基础测试类名，继承库中测试用例的属性

    # setUp()和tearDown()是每个测试用例进行时都会执行的测试方法，前者为起始，后者为结束
    def setUp(self):    # 复写父类的方法，最左侧有标识，是每一个测试用例都会执行的 起始方法
        # 自定义设置开始步骤
        ########################################
        # 示例：
        # 使用浏览器载入登录页面流程，每个测试用例都会执行
        # 注意驱动写作self.driver，否则会变成方法变量，而不是实例变量
        s = Service(r'D:\myCode\Github\python_test_development\demo\chrome-win64\chrome.exe')  # 设置驱动所在路径
        self.driver = webdriver.Chrome(service=s)  # 从路径提取驱动
        self.driver.implicitly_wait(10)  # 设置每个步骤最大等待时间
        self.driver.get('http://localhost:8001/login/')  # GET方法访问本机端口，即注册页面
        self.driver.maximize_window()   # 最大化窗口

    def tearDown(self):     # 复写父类的方法，最左侧有标识，是每一个测试用例都会执行的 结束方法
        # 自定义设置结束步骤
        ########################################
        # 示例：
        # 关闭浏览器页面，每个测试用例都会执行
        self.driver.close()

########################################################################################

    def input(self, user=None, password=None, vcode=None):  # 根据实际需求编写的测试方法
        ########################################
        # 示例：
        # 写入用户名，密码，验证码，并且点击登录
        if user:    # 设定判定条件，有输入才键入，否则不键入
            self.driver.find_element('id', 'LAY-user-login-username').send_keys(user)   # 将参数键入指定位置
        if password:
            self.driver.find_element('id', 'LAY-user-login-password').send_keys(password)
        if vcode:
            self.driver.find_element('id', 'LAY-user-login-vercode').send_keys(vcode)
        self.driver.find_element('id', 'loginButton').click()   # 点击登录按钮
        pass
########################################################################################
    def test1_login_success(self):    # 设置测试用例1,测试成功登录的情况，命名为test+xxx,会按照test后的阿拉伯数字顺序执行,testdemo也执行，带test都会执行
        # 执行+断言(自定义断言方法，灵活多变)
        ########################################
        # 示例：
        # 执行
        user, password, vcode = 'admin', '123456', '1234'   # 给定参数
        self.input(user, password, vcode)   # 传入参数给测试方法，并通过self.实例调用方法
        # 断言
        time.sleep(2)   # 断言之前要设置一定时间，以便浏览器反应
        # 注意此断言方法的文本属性.text
        self.assertEqual(self.driver.find_element('class name', 'layui-logo').text, '接口自动化测试')
        # 断言因素必须得设置注册页的元素而不是跳转后页面的元素

    def test2_errorpassword(self):    # 设置测试用例2，测试输入7位错误密码的情况
        # 执行+断言(自定义断言方法，灵活多变)
        ########################################
        # 示例：
        # 执行
        user, password, vcode = 'admin', '1234567', '1234'   # 给定参数
        self.input(user, password, vcode)   # 传入参数给测试方法，并通过self.实例调用方法
        # 断言
        time.sleep(1)   # 断言之前要设置一定时间，以便浏览器反应
        # 注意此断言方法的文本属性.text
        self.assertEqual(self.driver.find_element('class name', 'layui-layer-title').text, '出错了')
if __name__ == '__main__':  # 设定条件执行unittest的主函数
    unittest.main()     # 调用主函数进行多个测试用例测试