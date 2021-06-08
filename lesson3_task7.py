from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://localhost/litecart/admin/"
browser = webdriver.Chrome()
browser.get(link)
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
button = browser.find_element_by_name("login")
username.send_keys("admin")
password.send_keys("admin")
time.sleep(5)
button.click()
event = browser.find_elements_by_id("app-")
for items in event:
	button2 = items.find_element_by_id("app-")
	button2.click()
	time.sleep(3)
time.sleep(5)
browser.quit()