from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html")
time.sleep(1)

usuario = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/input[1]")
usuario.send_keys("dfdflujogramas@gmail.com")
time.sleep(1)

clave = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/form[1]/div[1]/div[2]/div[1]/input[1]")
clave.send_keys("12345678910")
time.sleep(1)

boton = driver.find_element_by_xpath("//input[@name='submit']")
boton.click()
time.sleep(5)

driver.quit()