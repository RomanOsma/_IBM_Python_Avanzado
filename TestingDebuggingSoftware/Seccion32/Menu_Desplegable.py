from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("Drivers/chromedriver.exe")

driver.maximize_window()
time.sleep(5)
driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")

menu = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
opciones = driver.find_elements_by_tag_name("option")

for opcion in opciones:
    opcion.click()
    time.sleep(1)