from selenium import webdriver
import time

controlador = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

controlador.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(1)

usuario = controlador.find_element_by_name("email")
clave = controlador.find_element_by_name("password")
time.sleep(1)

usuario.send_keys("dfdflujogramas@gmail.com")
time.sleep(5)
clave.send_keys("12345678910")
time.sleep(5)

boton = controlador.find_element_by_name("submit")
boton.click()
time.sleep(10)

controlador.quit()