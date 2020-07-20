from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()  # 实例化
driver.implicitly_wait(5)  # 设置页面等待时间5秒
driver.maximize_window()  # 窗口最大化

driver.get("http://192.168.1.41/upload/admin/")  # 进入ecshop后台登录页面
driver.find_element(By.NAME, "username").send_keys("lily")  # 输入用户名
driver.find_element(By.NAME, "password").send_keys("871208lily")   #输入密码
driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input").click()  #点击确定
handles = driver.window_handles  # 以list形式返回当前浏览器所有window的句柄
driver.switch_to.window(handles[-1])  # 切换窗口，进入商品管理

driver.switch_to.frame("menu-frame")  # 跳到左侧菜单栏
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]').click()  # 定位商品管理
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]/ul/li[1]/a').click()  # 点击商品列表
driver.switch_to.default_content()  # 跳出所有页面

driver.switch_to.frame("main-frame")  # 进入右侧菜单栏
time.sleep(3)
fenlei = driver.find_element(By.NAME,'cat_id')  #定位“分类”下拉菜单
select = Select(fenlei)  #将定位实例化到Select
select.select_by_value('132')   #选择第一个男装
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[1]').send_keys('裤子')  #关键词输入裤子
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[2]').click()   #点击确定

driver.quit()  # 关闭
