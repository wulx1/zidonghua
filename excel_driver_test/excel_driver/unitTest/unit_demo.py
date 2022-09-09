'''
   UnitTest测试框架应用
   1.类名继承unittest.TestCase
   2.测试用例：所有的测试用例，都是以函数的形式存在，函数的名称必须以test开头
   3.用例加载顺序：UnitTest中有默认加载顺序：0-9，a-z,A-Z
   4.所有的前置后置条件都是有等级的，class级别，method级别，前置与后置有且只有一个
            method级别前置后置：
            每一条用例运行前会执行前置，运行后执行后置
            class级别前置后置：
            1.必须定义装饰器@classmethod
            2.前置是所有内容运行前运行一次，后置是所有内容运行结束后运行一次

'''
#导入unitTest模块
import unittest
#如何真正意义上应用UnitTest框架：必须在类名继承unittest.TestCase
class UnitDemo(unittest.TestCase):
    #前置条件class级别
    @classmethod
    def setUpClass(cls) -> None:
        print('这是class级别的前置条件')

    @classmethod
    def tearDownClass(cls) -> None:
        print('这是class级别的后置条件')



    #前置条件;method级别
    def setUp(self) -> None:
        print('这是method级别前置条件')

    #后置条件
    def tearDown(self) -> None:
        print('这是method级别的后置条件')
    #测试用例：所有的测试用例，都是以函数的形式存在，函数的名称必须以test开头

    def test_01(self):
        print('这是测试用例1')
        self.login()

    def test_02(self):
        print('这是测试用例2')
     #普通函数；封装逻辑代码，以便在测试用例中进行调用
    def login(self):
        print('这是login函数')

if __name__ == '__main__':
    unittest.main()



