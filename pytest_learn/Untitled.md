一、pytest 简介
1.1 pytest 的背景和发展历史

  pytest 最初由 Holger Krekel 创建，于 2004 年首次发布，最初名为 py.test 。其目标是简化测试编写过程，同时提供强大的功能来满足复杂的测试需求。pytest 通过直观的语法、自动化的测试发现机制和强大的扩展性迅速获得了开发者的青睐。
发展历史：

    2004年pytest首次发布，目标是提供一个简单的、灵活的测试框架。
    2009年Pytest Development Team成立，推动pytest的持续发展。
    2011年 引入插件系统，极大地增强了pytest的灵活性和扩展性。
    2015年pytest采用率显著上升，成为 Python 社区中最受欢迎的测试框架之一。
    2017年 发布pytest 3.0版本，引入了许多新特性和改进，进一步提升了用户体验。
    2019年pytest迎来了 5.0 版本，持续改进和优化性能。
    2022年pytest 6.0版本发布，继续增强功能和改进用户体验。

1.2 pytest 的概念

  pytest 是一个用于 Python 的测试框架，支持简单的单元测试和复杂的功能测试。它以其简单、易用、灵活的特点，受到了许多开发者的青睐。

    pytest 框架可以轻松编写小型、可读的测试，并可以扩展支持应用程序和库的复杂功能测试。

pytest 官网：https://docs.pytest.org/en/8.2.x/
1.3 pytest 的特点

pytest 的主要特点包括：

    简洁的语法：无需继承特定的测试类，只需使用简单的函数即可编写测试。
    强大的断言：内置丰富的断言方法，提供详细的失败信息。
    自动发现：自动发现测试文件和测试函数，无需显式地注册测试。
    插件系统：丰富的插件生态系统，支持扩展和定制。

1.4 测试阶段分类

测试一般分为四个方面的测试：

    单元测试：称模块测试，针对软件设计中的最小单位——程序模块，进行正确性检查的测试工作
    集成测试：称组装测试，通常在单元测试的基础上，将所有程序模块进行有序的、递增测试，重点测试不同模块的接口部分
    系统测试：将整个软件系统看成一个整体进行测试，包括对功能、性能以及软件所运行的软硬件环境进行测试
    验收测试：按照项目任务书或合同、供需双方约定的验收依据文档进行的对整个系统的测试于评审，决定是否验收或拒收系统

1.5 单元测试框架的主要功能

    发现测试用例
    执行测试用例
    判断测试结果
    生成测试报告
    
    requirements.txt 是一个用于管理 Python 项目的依赖包的文件。它包含了项目运行所需的所有 Python 包及其版本信息。通过这个文件，开发者可以方便地分享和安装项目的依赖包，确保项目在不同环境下的一致性。

本文所采用的依赖包

# requestment.txt文件
pytest-html
pytest-xdist
pytest-ordering
pytest-rerunfailures

    1
    2
    3
    4
    5

安装命令

pip install -r requirements.txt

    1

二、pytest 的基本使用
2.1 pytest 默认测试用例

pytest 默认测试用例的格式：

    模块名：模块名（文件名）通常被统一放在一个testcases文件夹中，然后需要保证模块名以test_开头或_test结尾，例如test_demo1或demo2_test
    类名：测试类类名必须以Test开头，并且不能带有init方法
    方法名：测试方法名（Case 名）必须以test_开头，例如test_demo1(self)、test_demo2(self)

test_demo1.py

class TestDemo:
    def test_demo1(self):
        print("测试用例1")

    def test_demo2(self):
        print("测试用例2")
    
    1
    2
    3
    4
    5
    6

2.2 全局配置文件 pytest.ini

  我们可以在 pytest.ini 中进行一些属性的配置来修改 pytest 的默认属性，我们需要在根目录下创建，名称必须是 pytest.ini。

[pytest]
#参数
addopts = ‐vs
# 默认的执行路径，它会默认执行该文件夹下所有的满足条件的测试case
testpaths = ./testcases	
# 文件命名规则
python_files = test_*.py
# 类名命名规则
python_classes = Test*
# Case命名规则
python_functions = test_*

# 标记
markers =		
# 冒烟规则
smoke:冒烟用例		 
product_manage:商品管理

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17

2.3 执行 pytest

    方式一：使用命令行执行
    
      最简单的就是直接在 console 命令行输入 pytest，如果存在 pytest.ini，它会根据文件内容进行执行； 如果没有就按照默认格式执行。但是我们可以通过一些参数来强化 pytest 参数指令：
    
    # -vs： -v输出详细信息 -s输出调试信息
    pytest -vs
    
    # -n： 多线程运行（前提安装插件：pytest-xdist）
    pytest -vs -n=2
    
    # --reruns num: 失败重跑（前提安装插件：pytest-rerunfailres）
    pytest -vs --reruns=2
    
    # -x: 出现一个用例失败则停止测试
    pytest -vs -x
    
    # --maxfail: 出现几个失败才终止
    pytest -vs --maxfail=2
    
    # --html: 生成html的测试报告,后面 需要跟上所创建的文件位置及文件名称（前提安装插件：pytest-html）
    pytest -vs --html ./reports/result.html
    
    # -k： 运行测试用例名称中包含某个字符串的测试用例，我们可以采用or表示或者，采用and表示都
    pytest -vs -k "qiuluo"
    pytest -vs -k "qiuluo or weiliang"
    pytest -vs -k "qiuluo and weiliang"
    
    # -m：冒烟用例执行，后面需要跟一个冒烟名称，执行user_manage这个分组
    pytest -vs -m user_manage
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        12
        13
        14
        15
        16
        17
        18
        19
        20
        21
        22
        23
        24
        25
    
    class TestDemo:
        
        # 我们在Case上采用@pytest.mark. + 分组名称，就相当于该方法被划分为该分组中
        # 注意：一个分组可以有多个方法，一个方法也可以被划分到多个分组中
        @pytest.mark.user_manage
        def test_demo1(self):
            print("user_manage_test1")
    
        @pytest.mark.product_manage
        def test_demo2(self):
            print("product_manage_test1")
         
        @pytest.mark.user_manage
        @pytest.mark.product_manage
        def test_demo3(self):
            print("manage_test1")


    # 执行
    pytest -vs -m user_manage
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        12
        13
        14
        15
        16
        17
        18
        19
        20
    
    方式二：使用 main 方法执行
    
    if __name__ == '__main__':
    	pytest.main()
        
    if __name__ == '__main__':
    	pytest.main(["‐vs"])
        1
        2
        3
        4
        5

2.4 跳过方法

  pytest 的跳过案例方法其实和 unittest 是完全相同的，我们只需采用 skip 或 skipif 方法来指定参数并贴在方法上即可跳过。

# @pytest.mark.skip(跳过原因)

# @pytest.mark.skipif(跳过条件,跳过原因)

# 示例
class TestDemo:
    
    workage2 = 5
    workage3 = 20
    
    @pytest.mark.skip(reason="无理由跳过")
    def test_demo1(self):
        print("我被跳过了")
    
    @pytest.mark.skipif(workage2<10,reason="工作经验少于10年跳过")    
    def test_demo2(self):
        print("由于经验不足，我被跳过了")
    
    @pytest.mark.skipif(workage3<10,reason="工作经验少于10年跳过")
    def test_demo3(self):
        print("由于经验过关，我被执行了")
        
    def test_demo3(self):
        print("我没有跳过条件，所以我被执行了")
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24

2.5 pytest 前后置方法
2.5.1 使用固件实现前后置

    前后置就是针对不同层级方法执行前和执行后所需要执行的步骤进行封装并执行
    这个层级通常被划分为：文件层、类层、方法层（比如说要执行打印日志操作）
    
        方法层：它会在每个方法执行前后去执行该操作
    
        # 方法执行之前
        	def setUp(self):
                print("方法执行之前")
        		pass
        # 方法执行之后
        	def tearDown(self):
                print("每个测试方法执行之后都会执行")
        		pass
            1
            2
            3
            4
            5
            6
            7
            8
    
        类层：它会在调用这个类内所有方法的前后去执行该操作，无论类的方法执行多少次，它只会调用一次，它是一个类方法
    
        # 类中所有方法之前
            @classmethod
            def setUpClass(cls):
                print("类中所有方法之前")
            	pass
        # 类中所有方法之后
        	@classmethod
        	def tearDownClass(cls):
                print("类中所有方法之后")
        		pass
            1
            2
            3
            4
            5
            6
            7
            8
            9
            10
    
        文件层：也叫模块层，在每个代码文件执行前后去执行该操作，模块级别的需要卸载类的外边直接定义函数即可
    
        # 代码文件之前
        	def setup_module():
                print("代码文件之前")
        		pass
        # 代码文件之后
        	def teardown_module():
                print("代码文件之后")
        		pass
            1
            2
            3
            4
            5
            6
            7
            8

类似于 Srping AOP 里面的前置、后置通知。

    示例：用户账户登录

import unittest

class TestLogin(unittest.TestCase):
    
    # 在执行该类前所需要调用的方法
    @classmethod
    def setUpClass(cls) -> None:
    	print('------打开浏览器')
    
    # 在执行该类后所需要调用的方法
    @classmethod
    def tearDownClass(cls) -> None:
    	print('------关闭浏览器')
    
    # 每个测试方法执行之前都会先调用的方法
    def setUp(self):
    	print('输入网址......')
    
    # 每个测试方法执行之后都会调用的方法
    def tearDown(self) -> None:
    	print('关闭当前页面......')
    
    # 测试Case1
    def test_1(self):
    	print('输入正确用户名密码验证码,点击登录 1')
      
    # 测试Case2
    def test_2(self):
    	print('输入错误用户名密码验证码,点击登录 2')
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29

结果
image.png
2.5.2 使用 Fixtrue 实现前后置

  Fixtrue 所实现的功能基本和固件所实现的功能是一样的，但是会更加方便。语法格式：@pytest.fixture(scope=None,autouse=False,params=None,ids=None ,name=None)

    scope：作用范围，参数主要有三种：function函数、class类、package/session包
    
        function：在函数层面上执行前后置，我们通常采用 yield 进行前后置划分，yield 前是前置，yield 后是后置。
    
        @pytest.fixture(scope="function")
        	def exe_database_sql():
        		print("执行SQL查询")
        		yield
        		print("关闭数据库连接")
            1
            2
            3
            4
            5
    
        我们还可以 通过yield 或 return 去返回一些参数在方法中使用。注意： yield 返回参数后后置仍旧可以执行，但是 return 返回参数后后置操作无法执行。
    
        @pytest.fixture(scope="function")
        	def exe_database_sql():
        		print("执行SQL查询")
        		yield "success"
                # return "success" 执行后无法执行后置操作
        		print("关闭数据库连接")
            1
            2
            3
            4
            5
            6
    
        我们的方法在调用时，可以直接使用 exe_database_sql 表示返回信息进行输出
    
        def test_2(self，exe_database_sql):
            	print(exe_database_sql)
            1
            2
    
        class：在类之前和之后执行
    
        @pytest.fixture(scope="class")
        	def exe_database_sql():
        		print("执行SQL查询")
        		yield
        		print("关闭数据库连接")
            1
            2
            3
            4
            5
    
        package/session：在整个项目会话之前和之后执行
    
        @pytest.fixture(scope="session")
        	def exe_database_sql():
        		print("执行SQL查询")
        		yield
        		print("关闭数据库连接")
            1
            2
            3
            4
            5
    
    autouse：是否自动启动，该参数默认为 False ，我们可以将其修改为 True，该参数的功能主要在判断该固件是否在自定义范围内可以自动启动，若自动启动，则所有方法在执行时都会自动执行该前后置；若为 False，则我们需要手动启动
    
    # 1. 自动启动，则我们无需关心任何参数，我们的所有方法都会自动调用
    	@pytest.fixture(scope="function"，autoues=True)
    	def exe_database_sql():
    		print("执行SQL查询")
    		yield
    		print("关闭数据库连接")
            
    # 2. 关闭自动启动，我们在不同的scope下有不同的调用方法
    	@pytest.fixture(scope="function"，autoues=Flase)
    	def exe_database_sql():
    		print("执行SQL查询")
    		yield
    		print("关闭数据库连接")
            
    # 2.1 scope = function：我们需要在方法后加上该Fixture方法名
    	def test_2(self，exe_database_sql):
        	print(exe_database_sql)
    
    # 2.2 scope = class：我们需要在对应的类上添加@pytest.mark.usefixtures("exe_database_sql")装饰器调用
    @pytest.mark.usefixtures("exe_database_sql")
    class TestDemo:
        pass
    
    # 2.3 scope = session: 一般会结合conftest.py文件来实现
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        12
        13
        14
        15
        16
        17
        18
        19
        20
        21
        22
        23
        24
    
    autouse 仅限于在自己的类中使用上述方法，如果要跨类使用，那我们也需要在conftest.py 中配置
    
    params：实现参数化配置
    
    通常我们的脚本都是根据导出的 yaml 文件进行属性填充，params 通常后面跟上具体的数据（列表，元组等），然后我们在调用时有固定的写法。
    首先我们需要在 Fixture 方法参数中定义一个request，然后使用 request.param 来使用我们传递的 params
    
    class TestDemo:
        def read_yaml(self):
            return ["张三","李四","王五"]
        
        # 首先我们的参数需要获取数据：params=read_yaml()
        @pytest.fixture(scope="function",autouse=False,params=read_yaml(None))
        # 然后我们的Fixture方法需要一个request参数
    	def exe_database_sql(self, request):
            print("执行SQL查询")
            # 我们通过request.param获取数据，可以采用yield返回该数据
            yield request.param
            print("关闭数据库连接")
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        12
    
    ids：参数别名id
    
    不能单独使用，必须和 params 一起使用， 作用时对参数其别名，我们在采用 pytest 进行测试数据输出时会有对应的方法调用 n 次，该 n 次采用不同的 params 参数，这个 ids 就是修改了 console 控制台展示数据
    
    class TestDemo2:
    
        def read_yaml(self):
            return ["张三","李四","王五"]
    
        @pytest.fixture(scope="function", autouse=False, params=read_yaml(None), ids=["1", "2", "3"])
        def exe_database_sql(self, request):
            print("执行SQL查询")
            logging.info("打印")
            yield request.param
            print("关闭数据库连接")
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
    
    name：Fixture 别名
    
    作用时给 fixture 起别名，一旦使用了别名，那么 fixtrue 的名称就不能再用了，只能用别名
    
    class TestDemo:
        
        # 如果我们在这里使用到了别名
        @pytest.fixture(scope="function",name="exe_datebase_sql_name")
    	def exe_database_sql(request):
            print("执行SQL查询")
            yield 
            print("关闭数据库连接")
            
        # 我们这里就需要使用别名进行操作，之前的名称无法使用
    	def test_2(self，exe_datebase_sql_name):
        	print(exe_database_sql)    
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        12

2.6 conftest.py 文件

  该文件主要就是用来存储我们的 Fixture，然后我们会根据该文件的不同位置来判断可以使用的方法，conftest 可以在不同的目录级别下创建，如果我们在根目录下创建，那么所有case都会使用到该Fixture，但是如果我们在testcases文件夹下的某个模块文件下创建 conftest.py，那么它的作用范围就只包含在该目录下

    在根目录创建conftest.py，我们在该目录下的conftest文件里写的所有fixture可以在任意测试类下执行
    
    import pytest
    @pytest.fixture(scope="function",name="exe_datebase_sql_name")
    def exe_database_sql():
        print("全部方法运行前均可以执行")
        yield 
        print("全部方法运行后均可以执行")
        1
        2
        3
        4
        5
        6
    
    testcases文件夹下的usercases文件夹下创建的conftest.py，我们在该目录下创建的conftest文件里写的所有fixture仅可以在该目录下的测试类中使用，在其他测试类中使用会出现报错
    
    import pytest
    @pytest.fixture(scope="function",name="usercases_fixture")
    def exe_database_sql():
        print("usercases方法运行前均可以执行")
        yield 
        print("usercases方法运行后均可以执行")
    # testcases文件下的usercases文件夹下的测试类
    import pytest
    class TestUserCases1:
        # 测试Case1
        def test_1(self,usercases_fixture):
            print('输入正确用户名密码验证码,点击登录 1' + usercases_fixture)
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        12
    
    前后置执行顺序优先级：fixture_session > fixture_class > setup_class > fixture_function > setup

前后置执行的一个总体逻辑顺序：

    查询当前目录下的conftest.py文件
    查询当前目录下的pytest.ini文件并找到测试用例的位置
    查询用例目录下的conftest.py文件
    查询测试用例的py文件中是否有setup,teardown,setup_class,teardown_class
    再根据pytest.ini文件的测试用例的规则去查找用例并执行

三、pytest 进阶内容
3.1 Allure 效果美化

 我们在使用Pytest所生成的页面往往不够美观且展示信息杂乱不好分析，所以我们通常搭载allure来实现界面美化：

    Allure框架是一个灵活轻量级多语言测试报告工具
    它不仅可以以WEB的方式展示简介的测试结果，而且允许参与开发过程的每个人从日常执行的测试中最大限度的提取有用信息

步骤：

    下载 allure 并配置好环境变量，下载地址 https://github.com/allure-framework/allure2/releases
    
    安装 allure-pytest
    
    pip install allure-pytest
        1
    
    生成 allure 临时 json 文件，--alluredir 为文件目录
    
    pytest --alluredir=./allure-results
        1
    
    启动 allure
    
    allure serve ./allure-results  
