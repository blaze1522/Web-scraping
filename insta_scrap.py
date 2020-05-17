'''
Only first 4 tags will be explored. See line 53.
If the page does not load in 15 seconds then it will be skipped even if it is a valid hastag.
If you have slow internet the increase timeout time. See line 16.
Any section of any class can be selected. See line 19.
'''

import wiki_scrapping_food
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

timeout = 15
driver = webdriver.Chrome(executable_path='chromedriver')
class_to_find = "FFVAD"

# Read food.csv is avaiable else first write it
try:
    dataframe = pd.read_csv('food.csv')

except:
    wiki_scrapping_food.wikiscrap()
    dataframe = pd.read_csv('food.csv')

tags = [x for x in dataframe.food_name]

dict_tags = {}

# Go through each insta hashtag page
i = 0
for i in range(len(tags)):
    x = tags[i]
    url = 'https://www.instagram.com/explore/tags/' + x + '/'

    driver.get(url)

    # Wait for the required class of elements in this case images to appear.
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, class_to_find)))
        print("Read")
    except:
        print("Skipped")
        continue

    # Pick up all the image links an keep the list in a dictionary with the hashtag as the key.
    image_src = driver.find_elements_by_class_name(class_to_find)
    images = [x.get_attribute('src') for x in image_src]

    dict_tags[tags[i]] = images
    if i == 4:
        break


print("Number of pages read =", len(dict_tags))

# This Dictionary can now be used
# print(dict_tags)

driver.quit()
