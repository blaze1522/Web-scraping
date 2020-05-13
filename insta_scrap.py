'''
Only first 4 tags will be explored. See line 41


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

try:
    dataframe = pd.read_csv('food.csv')
    print('Try')
except:
    wiki_scrapping_food.wikiscrap()
    dataframe = pd.read_csv('food.csv')
    print('Except')

tags = [x for x in dataframe.food_name]

dict_tags = {}

i = 0
for i in range(len(tags)):
    x = tags[i]
    url = 'https://www.instagram.com/explore/tags/' + x + '/'

    driver.get(url)

    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "FFVAD")))
    except:
        continue

    image_src = driver.find_elements_by_class_name("FFVAD")
    images = [x.get_attribute('src') for x in image_src]

    dict_tags[i] = images
    if i == 4:
        break
    print("--------YYYYYYAAAAAASSSSSS----------")

print(len(images))

driver.quit()
