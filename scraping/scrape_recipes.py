from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from my_selenium import DRIVER

# Replace with the URL of the site with the cookie pop-up
url = "https://allrecipes.com"

DRIVER.get(url)

# Define a function to handle the cookie pop-up
def handle_cookie_popup():
    try:
        # wait for element to appear

        # Find the element that accepts or agrees to cookies (modify the selector as needed)
        reject_button = DRIVER.find_element(By.ID, "onetrust-reject-all-handler")

        # Click the button to accept cookies
        reject_button.click()
    except:
        print("No cookie pop-up found or encountered an error.")

# Call the function to handle the cookie pop-up
handle_cookie_popup()

#