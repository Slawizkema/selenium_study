import time

import math

from selenium import webdriver
from selenium.webdriver.common.by import *


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

main_link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome(executable_path='C:/ChromeWebDriver/chromedriver.exe')

time.sleep(2)

browser.get(main_link)

x_element = browser.find_element(By.CSS_SELECTOR, 'img#treasure').get_attribute("valuex")
calc_result = calc(x_element)

input_answer_field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
input_answer_field.send_keys(calc_result)

input_robot_checkbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
input_robot_checkbox.click()

input_robot_radio = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
input_robot_radio.click()

submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
submit_button.click()


