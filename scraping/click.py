import time
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:/Users/ASUS/Documents/pyprojects/seleniumdrivers"

url = "https://www.bbcgoodfood.com"

website = url.replace("https://www.", "")
website = website.replace(".com/", "")

driver = webdriver.Firefox()

driver.get(url)

# Wait for the cookie consent banner to be visible
driver.implicitly_wait(20)
alert = driver.switch_to.alert
alert.accept()
try:
    popup = driver.find_element(By.ID, 'notice')

    agree_button = popup.find_element(By.CSS_SELECTOR, 'button[title="AGREE"]')
    agree_button.click()

except Exception as e:
    print("An error occurred:", e)



