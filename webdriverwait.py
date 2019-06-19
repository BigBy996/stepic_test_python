import time
from math import sin, log
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def calc(x):
    return str(log(abs(12*sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
driver.get(link)

WebDriverWait(driver, 20).until(
    expected_conditions.text_to_be_present_in_element((By.ID, "price"), "10000")
)

driver.find_element_by_id("book").click()

value = driver.find_element_by_id("input_value").text
input_answer = driver.find_element_by_id("answer")
input_answer.send_keys(calc(value))

driver.find_element_by_id("solve").click()
time.sleep(40)

driver.quit()
