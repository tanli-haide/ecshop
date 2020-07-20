from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
import time
driver.maximize_window()   #窗口最大化

driver.get("http://192.168.1.41/upload/admin/")  # 进入ecshop后台登录页面
time.sleep(3)
driver.find_element(By.NAME, "username").send_keys("lily")  # 输入用户名
driver.find_element(By.NAME, "password").send_keys("871208lily")  #输入密码
driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input").click()  #点击确定
handles = driver.window_handles  # 以list形式返回当前浏览器所有window的句柄
driver.switch_to.window(handles[-1])  # 切换窗口，进入后台

driver.switch_to.frame("menu-frame")  # 跳到左侧菜单栏
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[11]').click()  # 点击数据库管理
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[11]/ul/li[1]/a').click()  # 点击数据备份
driver.switch_to.default_content()  # 跳出所有页面

driver.switch_to.frame("main-frame")  # 进入右侧菜单栏
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody[1]/tr[3]/td[1]').click()#点击标准备份
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[2]/tbody/tr[2]/td[2]/input[2]').click()#使用扩展插入选择否
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[2]/tbody/tr[3]/td[2]/input').clear()  #清空本分文件名默认值
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[2]/tbody/tr[3]/td[2]/input').send_keys('20200719ecshopbackup1.sql')#备份文件名输入20200719ecshopbackup1.sql
driver.find_element(By.XPATH,'//div[@id="listDiv"]/center/input').click()#点击开始备份

driver.quit()  #退出