from selenium.webdriver.common.by import *

import main

browser = main.get_connection('http://suninjuly.github.io/alert_accept.html ')

submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
submit_button.click()

confirm = browser.switch_to.alert
confirm.accept()


x_element = browser.find_element(By.CSS_SELECTOR, '.form-group .nowrap#input_value')
calc_result = main.calc(x_element.text)

input_answer_field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
input_answer_field.send_keys(calc_result)

submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
submit_button.click()