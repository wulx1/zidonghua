import unittest

from selenium import webdriver
from ddt import ddt, file_data

from excel_driver_test.POM_test.page.login_page import LoginPage
from excel_driver_test.POM_test.page.order_page import OrderPage
from excel_driver_test.POM_test.page.sousuo_page import SousuoPage


@ddt
class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lg = LoginPage(cls.driver)
        cls.od = OrderPage(cls.driver)
        cls.ss = SousuoPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test01_login(self, user, pwd, name):
        self.lg.login(user, pwd)
        self.ss.Sousuo(name)
        self.ss.wait(5)




    def test02_order(self):
        pass

    # self.od.order()
       #self.ss.order()


if __name__ == '__main__':
    unittest.main()
