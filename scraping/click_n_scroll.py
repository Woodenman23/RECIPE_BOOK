import time
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


os.environ['PATH'] += r"C:/Users/ASUS/Documents/pyprojects/seleniumdrivers"

url = "https://www.inmotionhosting.com/"

driver = webdriver.Firefox()

driver.get(url)

button = driver.find_element(By.ID,"whyUsDropdown")

button.click()

n = 10
while n<1111:
    driver.execute_script(f"window.scrollTo({n-10}, {n});")
    time.sleep(0.05)
    n+=10
    
driver.close()