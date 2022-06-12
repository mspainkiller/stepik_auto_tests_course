import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_xpath_form"
browser.get(link)
elements = browser.find_elements(By.TAG_NAME, "input")
for element in elements:
    element.send_keys("test")
browser.find_element(By.XPATH, '//div/button[@type="submit"]').click()
time.sleep(20)
browser.quit()

