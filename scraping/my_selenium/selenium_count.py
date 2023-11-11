import os

from my_selenium import DRIVER

url = "https://twinflamesuniverse.com/"

website = url.replace("https://www.", "")
website = website.replace(".com/", "")


DRIVER.get(url)

page_source = DRIVER.page_source

phrase = "twin flames"

count = page_source.lower().count(phrase)

print(f"The phrase {phrase} appears {count} times on my {website} homepage.")



