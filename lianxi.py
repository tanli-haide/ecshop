import unittest
from mytest_a import MyTest
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        print("初始化")
    def test_a(self):
        print("我是测试用例1")
    def test_b(self):
        print("测试用例2")
    def test_c(self):
        print("测试用例3")
    def tearDown(self):
        print("清理")
#if __name__ == '__main__':
   # unittest.main()

suite = unittest.TestSuite()  # 实例化测试套件testsuite
suite.addTest(MyTest('test_b'))  # 将用例添加到测试套件
runner = unittest.TextTestRunner()  # 实例化测试执行TestTestRunner
runner.run(suite)  # 运行测试套件


