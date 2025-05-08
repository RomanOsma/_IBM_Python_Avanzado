from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")

checkbox = driver.find_elements_by_class_name("checkmark")

for cheque in checkbox:
    if  cheque.is_displayed() == True and cheque.is_selected() == False:
        time.sleep(3)
        cheque.click()
