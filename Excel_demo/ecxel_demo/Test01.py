from time import sleep

from selenium import webdriver

class Demo():

    driver = webdriver.Chrome()

    def dakai(self,url):
        self.driver.get(url)

    def chazhao(self,id,txt):
        self.driver.find_element_by_xpath(id,txt)
        return

    def imput(self,id,txt,txt1):
        self.chazhao(id,txt).send_keys(txt1)

    def dianji(self,id,txt):
        self.chazhao(id,txt).click()

    def wait(self,t):
        sleep(t)

    def clear(self,id,txt):
        self.chazhao(id,txt).clear()

    def quit(self):
        self.quit()



