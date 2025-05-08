from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html")
time.sleep(1)

correo = driver.find_element_by_css_selector("input.form-control")
clave = driver.find_element_by_css_selector("input.textInput")
time.sleep(1)

correo.send_keys("dfdflujogramas@gmail.com")
time.sleep(1)
clave.send_keys("12345678910")
time.sleep(1)

boton = driver.find_element_by_css_selector("input.btn-primary")
boton.click()
time.sleep(3)

driver.quit()