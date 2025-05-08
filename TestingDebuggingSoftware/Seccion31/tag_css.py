from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F")
time.sleep(1)

usuario = driver.find_element_by_css_selector("input[id='email--1']")
clave = driver.find_element_by_css_selector("input[name='password']")
time.sleep(1)

usuario.send_keys("dfdflujogramas@gmail.com")
time.sleep(3)
clave.send_keys("12345678910")
time.sleep(3)

boton = driver.find_element_by_css_selector("input[name='submit']")
boton.click()
time.sleep(5)

driver.quit()