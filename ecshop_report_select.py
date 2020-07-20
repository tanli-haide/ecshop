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
driver.find_element(By.NAME, "password").send_keys("871208lily")  #输入密码
driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input").click()  #点击登录
handles = driver.window_handles  # 以list形式返回当前浏览器所有window的句柄
driver.switch_to.window(handles[-1])  # 切换窗口，进入商品管理

driver.switch_to.frame("menu-frame")  # 跳到左侧菜单栏
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[5]').click()  # 定位报表统计
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[5]/ul/li[3]/a').click()  # 点击订单统计
driver.switch_to.default_content()  # 跳出所有页面

driver.switch_to.frame("main-frame")  # 进入右侧菜单栏
time.sleep(3)
js = "document.getElementsByName('start_date').removeAttribute('readonly')"  #删除开始时间框的只读属性
driver.find_element(By.NAME,'start_date').clear()  #清空开始时间的默认值
driver.find_element(By.NAME,'start_date').send_keys('2020-07-17')  #输入时间

driver.find_element(By.NAME,'end_date').clear()  #清空结束时间的默认值
driver.find_element(By.NAME,'end_date').send_keys('2020-07-19')  #输入时间
driver.find_element(By.NAME,'submit').click()   #点击查询

driver.quit()  #关闭