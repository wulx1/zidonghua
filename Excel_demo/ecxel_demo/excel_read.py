import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://47.101.179.76:8089/me/my-views/view/all/')
driver.find_element_by_xpath('//*[@id="j_username"]').send_keys('wulx')
driver.find_element_by_xpath('/html/body/div/div/form/div[2]/input').send_keys('wulx123456')
driver.find_element_by_xpath('/html/body/div/div/form/div[3]/input').click()

driver.find_element_by_xpath('//*[@id="job_test_skipnewbie"]/td[3]/a').click()
driver.find_element_by_xpath('//*[@id="tasks"]/div[4]/span/a/span[2]').click()
#清除账号信息
driver.find_element_by_xpath('//*[@id="main-panel"]/form/div[1]/div[1]/div[2]/div/input[2]').clear()
#输入账号
driver.find_element_by_xpath('//*[@id="main-panel"]/form/div[1]/div[1]/div[2]/div/input[2]').send_keys('gltpdtest6')
#选择服务器
sql = driver.find_element_by_xpath('//*[@id="main-panel"]/form/div[1]/div[3]/div[2]/div/select')
Select(sql).select_by_value('改时服')
time.sleep(3)

driver.find_element_by_xpath('//*[@id="main-panel"]/form/div[1]/div[3]/div[2]/div/select').click()

#输入等级
driver.find_element_by_xpath('//*[@id="main-panel"]/form/div[1]/div[5]/div[2]/div/input[2]').clear()
driver.find_element_by_xpath('//*[@id="main-panel"]/form/div[1]/div[5]/div[2]/div/input[2]').send_keys('30')
#开始执行
driver.find_element_by_xpath('//*[@id="yui-gen1-button"]').click()

time.sleep(3)

