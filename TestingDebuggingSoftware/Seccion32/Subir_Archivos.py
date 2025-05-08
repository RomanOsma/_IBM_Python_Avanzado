from selenium import webdriver
import time

driver = webdriver.Chrome("Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")

boton = driver.find_element_by_id("myFile")
boton.send_keys("C:\Users\Usuario\Desktop\Infografias\Portada.jpg")
time.sleep(5)

driver.quit()