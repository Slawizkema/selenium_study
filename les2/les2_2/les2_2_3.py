from selenium.webdriver.support.select import Select

import main
from selenium.webdriver.common.by import *

browser = main.get_connection('http://suninjuly.github.io/selects1.html')
first_num = browser.find_element(By.CSS_SELECTOR, 'span#num1').text
second_num = browser.find_element(By.CSS_SELECTOR, 'span#num2').text

num_sum = int(first_num)+int(second_num)

select = Select(browser.find_element(By.CSS_SELECTOR, "select.custom-select"))
select.select_by_value(str(num_sum))

submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
submit_button.click()
