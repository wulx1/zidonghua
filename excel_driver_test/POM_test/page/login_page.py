'''
url
元素定位
业务流程

'''
from selenium.webdriver.common.by import By

from excel_driver_test.POM_test.base.base01 import BaseDemo
from selenium import webdriver


class LoginPage(BaseDemo):
    url = "http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html"
    username = (By.NAME, "accounts")
    password = (By.NAME, "pwd")
    button = (By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button")

    def login(self, user, pwd):
        self.get(self.url)
        self.input(self.username, user)
        self.input(self.password, pwd)
        self.click(self.button)


#测试代码
if __name__ == '__main__':
    driver = webdriver.Chrome()
    user = 'xuzhu666'
    pwd = '123456'
    lg = LoginPage(driver)
    lg.login(user, pwd)
