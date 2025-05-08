from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")
time.sleep(3)

driver.get("file:///C:/Users/Usuario/Desktop/Alert.html")
driver.maximize_window()
time.sleep(3)

boton = driver.find_element_by_id("btn")
boton.click()
time.sleep(3)

alerta = driver.switch_to_alert()
alerta.dismiss()
time.sleep(3)

driver.quit()