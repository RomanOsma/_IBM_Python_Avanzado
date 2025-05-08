from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
time.sleep(1)

driver.maximize_window()
time.sleep(5)
driver.get("https://www.google.com.sv/")
time.sleep(5)

driver.execute_script("window.open('');")
time.sleep(3)
driver.switch_to_window(driver.window_handles[1])
time.sleep(5)
driver.get("https://www.google.com.sv/")
time.sleep(5)
driver.get("https://www.facebook.com/")
time.sleep(5)

driver.execute_script("window.open('');")
time.sleep(3)
driver.switch_to_window(driver.window_handles[2])
time.sleep(5)
driver.get("https://www.google.com.sv/")
time.sleep(5)
driver.get("https://www.youtube.com/?hl=es")
time.sleep(5)
driver.back()
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.back()
time.sleep(5)

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.close()
time.sleep(1)
driver.switch_to_window(driver.window_handles[0])
driver.close()
time.sleep(3)

driver.switch_to_window(driver.window_handles[0])
driver.forward()
time.sleep(5)

driver.quit()