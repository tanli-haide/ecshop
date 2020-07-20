from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import unittest                #引入unittest类


class MyTest(unittest.TestCase):     #创建类
    def setUp(self):           #定义方法初始化
        print("初始化")         #打印初始化

    def test_backup(self):          #定义方法
        driver = webdriver.Chrome()
        driver.maximize_window()  # 窗口最大化
        driver.get("http://192.168.1.41/upload/admin/")  # 进入ecshop后台登录页面
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("lily")  # 输入用户名
        driver.find_element(By.NAME, "password").send_keys("871208lily")  # 输入密码
        driver.find_element(By.XPATH,
                            "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input").click()  # 点击确定
        handles = driver.window_handles  # 以list形式返回当前浏览器所有window的句柄
        driver.switch_to.window(handles[-1])  # 切换窗口，进入后台

        driver.switch_to.frame("menu-frame")  # 跳到左侧菜单栏
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[11]').click()  # 点击数据库管理
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[11]/ul/li[1]/a').click()  # 点击数据备份
        driver.switch_to.default_content()  # 跳出所有页面

        driver.switch_to.frame("main-frame")  # 进入右侧菜单栏
        time.sleep(2)
        driver.find_element(By.XPATH, '//div[@id="listDiv"]/table[1]/tbody[1]/tr[3]/td[1]').click()  # 点击标准备份
        driver.find_element(By.XPATH, '//div[@id="listDiv"]/table[2]/tbody/tr[2]/td[2]/input[2]').click()  # 使用扩展插入选择否
        time.sleep(2)
        driver.find_element(By.XPATH, '//div[@id="listDiv"]/table[2]/tbody/tr[3]/td[2]/input').clear()  # 清空本分文件名默认值
        time.sleep(2)
        driver.find_element(By.XPATH, '//div[@id="listDiv"]/table[2]/tbody/tr[3]/td[2]/input').send_keys(
            '20200719ecshopbackup1.sql')  # 备份文件名输入20200719ecshopbackup1.sql
        driver.find_element(By.XPATH, '//div[@id="listDiv"]/center/input').click()  # 点击开始备份

        driver.quit()  # 退出
    def test_goods_add(self):          #定义方法
        driver = webdriver.Chrome()
        driver.maximize_window()  # 窗口最大化
        driver.get("http://192.168.1.41/upload/admin/")  # 进入ecshop后台登录页面
        driver.find_element(By.NAME, "username").send_keys("lily")  # 登录
        driver.find_element(By.NAME, "password").send_keys("871208lily")
        driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input").click()
        handles = driver.window_handles  # 以list形式返回当前浏览器所有window的句柄
        driver.switch_to.window(handles[-1])  # 切换窗口，进入商品管理

        driver.switch_to.frame("menu-frame")  # 跳到左侧菜单栏
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]').click()  # 定位商品管理
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]/ul/li[2]/a').click()  # 进入添加新商品
        driver.switch_to.default_content()  # 跳出所有页面

        driver.switch_to.frame("main-frame")  # 进入右侧菜单栏
        time.sleep(3)  # 等待3秒
        driver.find_element(By.XPATH, '//*[@id="general-tab"]').click()
        driver.find_element(By.XPATH, '//*[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').send_keys('睡衣')

        driver.find_element(By.NAME, 'cat_id').send_keys('睡衣')
        fenlei = driver.find_element(By.NAME, 'cat_id')  # 定位“分类”下拉菜单
        select = Select(fenlei)  # 将定位实例化到Select
        select.select_by_value('132')  # 选择第一个男装
        driver.find_element(By.NAME, "shop_price").clear()
        time.sleep(3)

        driver.find_element(By.NAME, "shop_price").send_keys('88')  # 本店售价输入88
        js = "window.scrollTo(200,1200)"  # 页面滚动到下面页
        driver.execute_script(js)  # 转换代码，实现页面滚动
        driver.find_element(By.XPATH, '//div[@id="tabbody-div"]/form/div/input[2]').click()  # 点击确定按钮
        driver.switch_to.default_content()  # 跳出所有页面

        driver.quit()  # 退出
    def test_goods_delete(self):          #定义方法
        driver = webdriver.Chrome()
        driver.maximize_window()  # 窗口最大化
        driver.get("http://192.168.1.41/upload/admin/")  # 进入ecshop后台登录页面
        driver.find_element(By.NAME, "username").send_keys("lily")  # 登录
        driver.find_element(By.NAME, "password").send_keys("871208lily")
        driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input").click()
        handles = driver.window_handles  # 以list形式返回当前浏览器所有window的句柄
        driver.switch_to.window(handles[-1])  # 切换窗口，进入商品管理

        driver.switch_to.frame("menu-frame")  # 跳到左侧菜单栏
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]').click()  # 定位商品管理
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]/ul/li[1]/a').click()  # 点击商品列表
        driver.switch_to.default_content()  # 跳出所有页面

        driver.switch_to.frame("main-frame")  # 进入右侧菜单栏
        time.sleep(3)  # 等待3秒
        driver.find_element(By.XPATH, '//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[4]').click()  # 点击删除按钮
        time.sleep(3)  # 等待3秒
        driver.switch_to.alert.text  # 出现警告框
        driver.switch_to.alert.accept()  # 点击确定

        driver.quit()  # 关闭
    def test_goods_fixed(self):
        driver = webdriver.Chrome()
        driver.maximize_window()  # 窗口最大化
        driver.get("http://192.168.1.41/upload/admin/")  # 进入ecshop后台登录页面
        driver.find_element(By.NAME, "username").send_keys("lily")  # 输入用户名
        driver.find_element(By.NAME, "password").send_keys("871208lily")  # 输入密码
        driver.find_element(By.XPATH,
                            "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input").click()  # 点击确定
        handles = driver.window_handles  # 以list形式返回当前浏览器所有window的句柄
        driver.switch_to.window(handles[-1])  # 切换窗口，进入商品管理

        driver.switch_to.frame("menu-frame")  # 跳到左侧菜单栏
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]').click()  # 定位商品管理
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]/ul/li[1]/a').click()  # 点击商品列表
        driver.switch_to.default_content()  # 跳出所有页面

        driver.switch_to.frame("main-frame")  # 进入右侧菜单栏
        time.sleep(3)  # 等待3秒
        driver.find_element(By.XPATH, '//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[2]').click()  # 点击编辑按钮
        time.sleep(3)  # 等待3秒

        driver.find_element(By.XPATH, '//table[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').clear()  # 清楚默认值
        driver.find_element(By.XPATH, '//table[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').send_keys(
            '高领毛衣')  # 输入高领毛衣
        driver.find_element(By.XPATH, '//div[@id="tabbody-div"]/form/div/input[2]').click()  # 点击确定

        driver.quit()  # 关闭

    def test_goods_select(self):
        driver = webdriver.Chrome()
        driver.maximize_window()  # 窗口最大化
        driver.get("http://192.168.1.41/upload/admin/")  # 进入ecshop后台登录页面
        driver.find_element(By.NAME, "username").send_keys("lily")  # 输入用户名
        driver.find_element(By.NAME, "password").send_keys("871208lily")  # 输入密码
        driver.find_element(By.XPATH,
                            "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input").click()  # 点击确定
        handles = driver.window_handles  # 以list形式返回当前浏览器所有window的句柄
        driver.switch_to.window(handles[-1])  # 切换窗口，进入商品管理

        driver.switch_to.frame("menu-frame")  # 跳到左侧菜单栏
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]').click()  # 定位商品管理
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]/ul/li[1]/a').click()  # 点击商品列表
        driver.switch_to.default_content()  # 跳出所有页面

        driver.switch_to.frame("main-frame")  # 进入右侧菜单栏
        time.sleep(3)
        fenlei = driver.find_element(By.NAME, 'cat_id')  # 定位“分类”下拉菜单
        select = Select(fenlei)  # 将定位实例化到Select
        select.select_by_value('132')  # 选择第一个男装
        driver.find_element(By.XPATH, '/html/body/div[1]/form/input[1]').send_keys('裤子')  # 关键词输入裤子
        driver.find_element(By.XPATH, '/html/body/div[1]/form/input[2]').click()  # 点击确定

        driver.quit()  # 关闭

    def test_report_select(self):
        driver = webdriver.Chrome()
        driver.maximize_window()  # 窗口最大化
        driver.get("http://192.168.1.41/upload/admin/")  # 进入ecshop后台登录页面
        driver.find_element(By.NAME, "username").send_keys("lily")  # 输入用户名
        driver.find_element(By.NAME, "password").send_keys("871208lily")  # 输入密码
        driver.find_element(By.XPATH,
                            "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input").click()  # 点击登录
        handles = driver.window_handles  # 以list形式返回当前浏览器所有window的句柄
        driver.switch_to.window(handles[-1])  # 切换窗口，进入商品管理

        driver.switch_to.frame("menu-frame")  # 跳到左侧菜单栏
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[5]').click()  # 定位报表统计
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[5]/ul/li[3]/a').click()  # 点击订单统计
        driver.switch_to.default_content()  # 跳出所有页面

        driver.switch_to.frame("main-frame")  # 进入右侧菜单栏
        time.sleep(3)
        js = "document.getElementsByName('start_date').removeAttribute('readonly')"  # 删除开始时间框的只读属性
        driver.find_element(By.NAME, 'start_date').clear()  # 清空开始时间的默认值
        driver.find_element(By.NAME, 'start_date').send_keys('2020-07-17')  # 输入时间

        driver.find_element(By.NAME, 'end_date').clear()  # 清空结束时间的默认值
        driver.find_element(By.NAME, 'end_date').send_keys('2020-07-19')  # 输入时间
        driver.find_element(By.NAME, 'submit').click()  # 点击查询

        driver.quit()  # 关闭

    def tearDown(self):          #定义方法
        print("清理")

if __name__ == '__main__':    #表示当前文件可以执行，执行的内容就在该方法的方法体中
    unittest.main()   #main函数是默认的执行参数，按照ASCLL码的顺序执行用例
