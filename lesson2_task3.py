from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://localhost/litecart/admin/login.php"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    username = browser.find_element_by_name("username")
    password = browser.find_element_by_name("password")
    button = browser.find_element_by_name("login")
    username.send_keys("admin")
    password.send_keys("admin")
    time.sleep(5)
    button.click()
    time.sleep(5)
finally:
    browser.quit()