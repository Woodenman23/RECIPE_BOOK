import time
import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

os.environ['PATH'] += r"C:/Users/fosterj/pyprojects/seleniumdrivers"
URL = f"https://www.bbcgoodfood.com/search/"
TUTORIAL_URL = f"https://www.simplyrecipes.com/latest/"

driver = webdriver.Chrome()

def connect(url=TUTORIAL_URL):
    """
    create chrome driver
    :return: chrome driver:obj
    """
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options, executable_path='../../seleniumdrivers')
    try:
        driver.get(url)
        time.sleep(5)
    except TimeoutException:
        print('new connection try')
        driver.get(url)
        time.sleep(5)

    return driver

