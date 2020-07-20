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
if __name__ == '__main__':
    unittest.main()

