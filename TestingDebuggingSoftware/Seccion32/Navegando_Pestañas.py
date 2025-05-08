from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

driver.maximize_window()
time.sleep(1)
driver.get("https://www.udemy.com/")
time.sleep(5)

driver.execute_script("window.open('');")
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(5)

driver.switch_to_window(driver.window_handles[0])
time.sleep(5)
driver.close()
time.sleep(5)

driver.quit()