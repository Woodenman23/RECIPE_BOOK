import time
import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

os.environ['PATH'] += r"C:/Users/ASUS/Documents/pyprojects/seleniumdrivers"

url = "https://twinflamesuniverse.com/"

website = url.replace("https://www.", "")
website = website.replace(".com/", "")

driver = webdriver.Firefox()

driver.get(url)

page_source = driver.page_source

phrase = "here"

count = page_source.lower().count(phrase)

print(f"The phrase {phrase} appears {count} times on my {website} homepage.")



