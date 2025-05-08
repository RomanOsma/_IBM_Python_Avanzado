from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")
time.sleep(3)

driver.maximize_window()
driver.get("file:///C:/Users/Usuario/Desktop/Confirm.html")
time.sleep(3)

btn = driver.find_element_by_name("boton")
btn.click()
time.sleep(3)

alerta = driver.switch_to_alert()
alerta.accept()
time.sleep(3)

driver.quit()