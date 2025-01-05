import unittest

class BasicTestCase(unittest.TestCase):
    judge = {'first': 0}

    def test2(self):
        print('执行test2')
        BasicTestCase.judge['first'] = 888    # 更改下个测试所要依赖的变量值

    def test3(self):
        if BasicTestCase.judge['first'] == 888:   # 设定判定条件看是否需要跳过
            print("test3")
            return    # 若满足条件则直接return结束，此test下的之后的语句均不执行
        # print('执行test3')  # 此段代码中这句话加与不加都并不会被执行，测试通过但执行语句并没有执行，因为根据依赖的条件test3已经结束

if __name__ == '__main__':  # 设定条件执行unittest的主函数
    unittest.main()