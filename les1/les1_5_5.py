import time

from selenium import webdriver
from selenium.webdriver.common import by

main_link = 'http://suninjuly.github.io/huge_form.html'

browser = webdriver.Chrome(executable_path='C:/ChromeWebDriver/chromedriver.exe')
time.sleep(5)

browser.get(main_link)

input_forms = browser.find_elements(by.By.TAG_NAME,  'input')

for input in input_forms:
    input.send_keys("blabla")

submit_button = browser.find_element(by.By.CSS_SELECTOR, "button.btn.btn-default")
submit_button.click()

