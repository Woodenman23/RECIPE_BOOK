import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:/Users/ASUS/Documents/pyprojects/seleniumdrivers"

url = "https://apps.microsoft.com/detail/netflix/9WZDNCRFJ3TJ?hl=en-us&gl=US"

website = url.replace("https://www.", "")
website = website.replace(".com/", "")

driver = webdriver.Firefox()

driver.get(url)

_class = "logo view-transition"

