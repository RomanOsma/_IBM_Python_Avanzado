from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")
driver.maximize_window()
time.sleep(3)
driver.get("file:///C:/Users/Usuario/Desktop/Promt.html")

boton = driver.find_element_by_id("btn")
time.sleep(3)
boton.click()
time.sleep(3)

alerta = driver.switch_to_alert()
alerta.dismiss()
time.sleep(5)

driver.quit()