'''
url
元素定位
业务流程

'''
from selenium.webdriver.common.by import By

from excel_driver_test.POM_test.base.base01 import BaseDemo
from selenium import webdriver


class OrderPage(BaseDemo):

    button00 = (By.XPATH, '//*[@id="floor1"]/div[2]/div[2]/div[7]/div/div/a')
    button01 = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[1]')
    button02 = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[2]/ul/li[2]')
    button03 = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[3]/ul/li[3]')
    button04 = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/button')

    def order(self):

        self.wait(5)
        self.click(self.button00)
        self.wait(2)
        self.click(self.button01)
        self.wait(2)
        self.click(self.button02)
        self.wait(2)
        self.click(self.button03)
        self.click(self.button04)

# 测试代码
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lg = OrderPage(driver)
#     lg.order()
