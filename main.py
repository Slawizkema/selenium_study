import time

import math
from selenium import webdriver


def get_connection (url):

    browser = webdriver.Chrome(executable_path='C:/ChromeWebDriver/chromedriver.exe')
    time.sleep(2)
    browser.get(url)
    return browser

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))