'''
关键字驱动类
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select


def browser(type_):
    try:
        driver = getattr(webdriver,type_)()
    except:
        print('出现异常，启动默认浏览器Chorem')
        driver = webdriver.Chrome()
    return driver

class WebDemo:
    def __init__(self,type_):
        self.driver = browser(type_)

    def open(self,**kwargs):
        self.driver.get(kwargs['txt'])
#元素定位
    def locator(self,**kwargs):
        return self.driver.find_element(kwargs['name'],kwargs['value'])

    def input(self,**kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    def click(self,**kwargs):
        self.locator(**kwargs).click()

    def quit(self,**kwargs):
        self.driver.quit()

    def wait(self,**kwargs):
        sleep(kwargs['txt'])

    def clear(self,**kwargs):
        self.locator(**kwargs).clear()

    def seclect(self,**kwargs):

        return

      









