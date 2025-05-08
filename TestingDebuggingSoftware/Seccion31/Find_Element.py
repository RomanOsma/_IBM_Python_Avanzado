from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F")
driver.maximize_window()
time.sleep(5)

correo = driver.find_element(By., "form-control")
clave = driver.find_element(By.CLASS_NAME, "textInput")
time.sleep(5)

correo.send_keys("dfdflujogramas@gmail.com")
time.sleep(5)
clave.send_keys("12345678910")
time.sleep(5)

boton = driver.find_element(By.CLASS_NAME, "btn-primary")
boton.click()
time.sleep(5)

driver.quit()