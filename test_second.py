import unittest                #引入unittest类
class MyTest(unittest. TestCase):     #创建类
    def setUp(self):           #定义方法初始化
        print("初始化")         #打印初始化
    def test_a(self):          #定义方法
        print("我是测试用例1")
    def test_b(self):          #定义方法
        print("测试用例2")
    def test_c(self):          #定义方法
        print("测试用例3")
    def tearDown(self):          #定义方法
        print("清理")
if __name__ == '__main__':    #表示当前文件可以执行，执行的内容就在该方法的方法体中
    #unittest.main()   #main函数是默认的执行参数，按照ASCLL码的顺序执行用例
    suit = unittest.TestSuite()    #实例化测试套件TestSuite
    suit.addTest(MyTest("test_a"))    #将用例添加到套件中
    suit.addTest(MyTest("test_b"))    #将用例添加到套件中
    runner = unittest.TextTestRunner()    #实例化测试执行TextTestRunner
    runner.run(suit)                      #运行测试套件