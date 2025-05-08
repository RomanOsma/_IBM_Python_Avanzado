from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import unittest


class menu_desplegable(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("Drivers/chromedriver.exe")
        self.driver.maximize_window()

    def test_recorrer(self):
        self.driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")

        menu = Select(self.driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        time.sleep(3)

        menu.select_by_index(11)
        time.sleep(5)

        menu.select_by_value("6")
        time.sleep(5)

        menu.select_by_visible_text("Ford")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
