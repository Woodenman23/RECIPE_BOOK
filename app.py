import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

from scraping.my_selenium import DRIVER

search_term = "vampire"

def main():
    url = "https://www.wikipedia.org/"

    DRIVER.get(url)

    try:
        # Locate the close button element
        close_button = WebDriverWait(DRIVER, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".banner__close"))
    )

        # Click the close button to dismiss the banner
        close_button.click()
        
        search_bar = DRIVER.find_element(By.XPATH, '//*[@id="searchInput"]')
    
        
        search_bar.send_keys(search_term)
        search_button = DRIVER.find_element(By.XPATH,"/html/body/div[3]/form/fieldset/button")
        search_button.click()
        
         
        paragraph1_text = _get_text("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[3]")
        _add_to_file(paragraph1_text)
        


        time.sleep(5)

    except:
        print("something failed")
        time.sleep(5)
    DRIVER.quit()

def _get_text(xpath):
    text_element = DRIVER.find_element(By.XPATH, xpath)
    text = text_element.text
    return(text)

def _add_to_file(text: str):
    
    dir_path = Path(r'C:\\Users\fosterj\pyprojects\RECIPE_BOOK\wiki_texts')

   
    file_path = dir_path / search_term
    with file_path.open(mode="w") as file: 
        file.write(text)

main()

