import time

from selenium import webdriver
from selenium.webdriver.common.by import *

main_link = 'http://suninjuly.github.io/registration2.html'

#browser = webdriver.Chrome(executable_path='C:/ChromeWebDriver/chromedriver.exe')
browser = webdriver.Chrome()

time.sleep(2)

browser.get(main_link)

input_first_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
input_first_name.send_keys("Ivan")

input_second_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
input_second_name.send_keys("Petrov")

input_email = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
input_email.send_keys("Petrov@ivan.ru")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(2)

result = browser.find_element_by_tag_name("h1").text
assert result == "Поздравляем! Вы успешно зарегистировались!"
