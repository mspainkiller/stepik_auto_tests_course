import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link = "http://suninjuly.github.io/find_link_text"
str1 = str(math.ceil(math.pow(math.pi, math.e) * 10000))
#try:
driver = webdriver.Chrome()
driver.get(link)
needed_link = driver.find_element_by_link_text(str1)
needed_link.click()
input1 = driver.find_element(By.NAME, "first_name")
input1.send_keys("First" + Keys.TAB)
input2 = driver.find_element(By.NAME, "last_name")
input2.send_keys("First" + Keys.TAB)
input3 = driver.find_element(By.CLASS_NAME, "city")
input3.send_keys("City" + Keys.TAB)
input4 = driver.find_element(By.ID, "country")
input4.send_keys("country" + Keys.TAB)
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(20)
driver.quit()


