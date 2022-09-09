from time import sleep

from selenium import webdriver


class BaseDemo:

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    def click(self, loc):
        self.locator(loc).click()

    def wait(self, time_):
        sleep(time_)

    def quit(self):
        self.quit()

    def clear(self):
        self.clear()
