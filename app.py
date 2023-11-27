import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pathlib import Path

from scraping.my_selenium import DRIVER

search_term = "spanish food"

def main():
    url = "https://www.wikipedia.org/"

    DRIVER.get(url)

    try:
        try:
            # Locate the close button element
            close_button = WebDriverWait(DRIVER, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".banner__close"))
        )
            
            close_button.click()
        except TimeoutException:
            print("passed")
        search_bar = DRIVER.find_element(By.XPATH, '//*[@id="searchInput"]')
    
        
        search_bar.send_keys(search_term)
        search_button = DRIVER.find_element(By.XPATH,"/html/body/div[3]/form/fieldset/button")
        search_button.click()
        
        content = DRIVER.find_element(By.ID, 'content')
        
        #need to scroll down page and find more <p>s
        paragraphs = content.find_elements(By.TAG_NAME, 'p') 
        
        dir_path = Path(r'C:\\Users\fosterj\pyprojects\RECIPE_BOOK\wiki_texts')
        file_path = dir_path / f"{search_term}.txt"
        with file_path.open(mode="w") as file:
            for paragraph in paragraphs:
                text = paragraph.text
                file.write("\n--------------------\n")
                file.write(text)
    except:
        print("something failed")
        time.sleep(5)
    DRIVER.quit()

def _get_text(xpath):
    text_element = DRIVER.find_element(By.XPATH, xpath)
    text = text_element.text
    return(text)

def _add_to_file(text: str):
    
    
   
    
    with file_path.open(mode="w") as file: 
        file.write(text)

main()

