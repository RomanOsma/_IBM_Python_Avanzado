from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

s=Service("Drivers/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F%3Futm_source%3Dadwords-brand%26utm_medium%3Dudemyads%26utm_campaign%3DBrand-Udemy_la.EN_cc.ROW%26utm_term%3D_._ag_80315195513_._ad_535757779892_._de_c_._dm__._pl__._ti_kwd-298663929108_._li_1012108_._pd__._%26utm_term%3D_._pd__._kw_udemy.com_._%26matchtype%3De%26gclid%3DEAIaIQobChMIn-iRzcnf8wIViY7ICh1K-wLUEAAYASAAEgJhNfD_BwE")
time.sleep(1)

email = driver.find_element_by_class_name("form-control")
clave = driver.find_element_by_class_name("textinput textInput form-control")
time.sleep(1)

email.send_keys("dfdfujogramas@gmail.com")
time.sleep(5)
clave.send_keys("12345678910")
time.sleep(5)

boton = driver.find_element_by_class_name("btn btn-primary ")
boton.click()
time.sleep(10)

driver.close()