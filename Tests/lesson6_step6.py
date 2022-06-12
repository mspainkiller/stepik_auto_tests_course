import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/huge_form.html"
browser.get(link)
elements = browser.find_elements(By.TAG_NAME, "input")
for element in elements:
    element.send_keys("test")
browser.find_element(By.CLASS_NAME, "btn").click()

time.sleep(20)
browser.quit()
