from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Ffundamentos-de-la-programacion%2F&persist_locale=")
time.sleep(1)

correo = driver.find_element_by_css_selector("input#email--1")
contrasena = driver.find_element_by_css_selector("input#id_password")
time.sleep(1)

correo.send_keys("dfdflujogramas@gmail.com")
time.sleep(1)
contrasena.send_keys("12345678910")
time.sleep(1)

boton = driver.find_element_by_css_selector("input#submit-id-submit")
boton.click()
time.sleep(5)

driver.quit()