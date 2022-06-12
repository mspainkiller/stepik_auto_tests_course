from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "input[value='robots']").click()
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
