import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge() # 选择Chrome浏览器
driver.get('http://internet.tenda.cn/ac_portal/default/pc.html?tabs=pwd') # 打开网站
time.sleep(2)
username = "pansonglin" # 请替换成你的用户名
password = "tenda0043408..." # 请替换成你的密码
driver.find_element(By.ID,'password_name').send_keys(username) # 自动敲入用户名
driver.find_element(By.ID,'password_pwd').send_keys(password) # 自动敲入密码
a=driver.find_element(By.NAME,'btlogin')
a.click()
time.sleep(2)
driver.close()
 
