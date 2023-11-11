from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the URL of the site with the cookie pop-up
url = "https://bbcgoodfood.com"

# Initialize the WebDriver
driver = webdriver.Firefox()
driver.get(url)

# Define a function to handle the cookie pop-up
def handle_cookie_popup():
    try:
        # Wait for the cookie pop-up to appear (adjust the locator as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'message-container')))
        print("found")

        # Find the element that accepts or agrees to cookies (modify the selector as needed)
        accept_button = driver.find_element(By.CSS_SELECTOR, 'button[title="AGREE"]')

        # Click the button to accept cookies
        accept_button.click()
    except:
        print("No cookie pop-up found or encountered an error.")

# Call the function to handle the cookie pop-up
handle_cookie_popup()

# Your further actions after accepting the cookies
# For instance, navigate to different pages, perform other tasks, etc.
