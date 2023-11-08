import time
import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

os.environ['PATH'] += r"C:/Users/fosterj/pyprojects/seleniumdrivers"

driver = webdriver.Firefox()

