'''
url
元素定位
业务流程

'''
from selenium.webdriver.common.by import By

from excel_driver_test.POM_test.base.base01 import BaseDemo
from selenium import webdriver


class SousuoPage(BaseDemo):
    # url = "http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html"
    sousuo = (By.XPATH, '//*[@id="search-input"]')
    button = (By.XPATH, '//*[@id="ai-topsearch"]')
    button1 = (By.XPATH, '/html/body/div[4]/div/ul/li[1]/div/a/p')
    suit = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[1]')
    color = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[2]/ul/li[1]')
    sikp = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[3]/ul/li[2]')
    join = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/button')

    def Sousuo(self, name):
        self.input(self.sousuo, name)
        self.click(self.button)
        self.click(self.button1)
        self.wait(3)

    def order(self):
        self.click(self.suit)
        self.wait(2)
        self.click(self.color)
        self.wait(2)
        self.click(self.sikp)
        self.wait(2)
        self.click(self.join)

# #测试代码
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     user = 'xuzhu666'
#     pwd = '123456'
#     lg = LoginPage(driver)
#     lg.login(user, pwd)
