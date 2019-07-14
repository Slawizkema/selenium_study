import time
import unittest

from selenium.webdriver.common.by import *

import main


class TestRegistration(unittest.TestCase):

    def fill_fields(self):
        browser = self.browser
        input_first_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
        input_first_name.send_keys("Ivan")

        input_second_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
        input_second_name.send_keys("Petrov")

        input_email = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
        input_email.send_keys("Petrov@ivan.ru")

    def test_first_site(self):
        self.browser = main.get_connection('http://suninjuly.github.io/registration1.html')
        self.fill_fields()

        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(2)

        result = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual(result, "Поздравляем! Вы успешно зарегистировались!", "RegError")

    def test_second_site(self):
        self.browser = main.get_connection('http://suninjuly.github.io/registration2.html')
        self.fill_fields()

        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(2)

        result = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual(result, "Поздравляем! Вы успешно зарегистировались!", "RegError")

