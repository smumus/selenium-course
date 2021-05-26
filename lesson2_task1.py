from selenium import webdriver
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://google.com")
time.sleep(5)
driver.quit()
