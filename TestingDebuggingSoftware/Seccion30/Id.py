from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\\Users\\Usuario\\PycharmProjects\\PruebasTesting\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html")
time.sleep(1)

usuario = driver.find_element_by_id("email--1")
clave = driver.find_element_by_id("id_password")
time.sleep(1)

usuario.send_keys("dfdflujogramas@gmail.com")
time.sleep(5)

clave.send_keys("12345678910")
time.sleep(5)

boton = driver.find_element_by_id("submit-id-submit")
boton.click()
time.sleep(5)

driver.quit()