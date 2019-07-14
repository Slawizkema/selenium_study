# waiting

import time


from selenium.webdriver.common.by import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import main

browser = main.get_connection('http://suninjuly.github.io/explicit_wait2.html')


text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))

# click redirect button
submit_button = browser.find_element(By.CSS_SELECTOR, 'button#book')
browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
submit_button.click()



# calc answer
x_element = browser.find_element(By.CSS_SELECTOR, '.form-group .nowrap#input_value')
calc_result = main.calc(x_element.text)

input_answer_field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
input_answer_field.send_keys(calc_result)

submit_button = browser.find_element(By.CSS_SELECTOR, 'button#solve')
browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
submit_button.click()

time.sleep(2)

confirm = browser.switch_to.alert
print(confirm.text)
confirm.accept()
browser.close()