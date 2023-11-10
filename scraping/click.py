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
try:
    # Wait for the element with ID 'notice' to be visible
    notice = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'notice')))
    
    # Wait for the AGREE button to be clickable
    agree_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sp_choice_type_11')))
    agree_button.click()

except Exception as e:
    print("An error occurred:", e)

driver.close()

