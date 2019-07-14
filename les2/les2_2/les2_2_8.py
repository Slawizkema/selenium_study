import os

from selenium.webdriver.common.by import *

import main

browser = main.get_connection('http://suninjuly.github.io/file_input.html')

input_first_name = browser.find_element(By.CSS_SELECTOR, 'input[name=firstname]')
input_first_name.send_keys("Ivan")

input_second_name = browser.find_element(By.CSS_SELECTOR, 'input[name=lastname]')
input_second_name.send_keys("Petrov")

input_email = browser.find_element(By.CSS_SELECTOR, 'input[name=email]')
input_email.send_keys("Petrov@ivan.ru")

input_file = browser.find_element(By.CSS_SELECTOR, 'input#file')
file = open('input_file.txt', 'w').close()
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'input_file.txt')

input_file.send_keys(file_path)


submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
submit_button.click()