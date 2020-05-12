import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def remove_space(x):
    char_list = [i for i in x]
    for i in char_list:
        if i == ' ':
            char_list.remove(i)
    new = ""
    for s in char_list:
        new += s
    return new.lower()


options = Options()
options.page_load_strategy = 'none'

driver = webdriver.Chrome(executable_path='chromedriver', options=options)
driver.get('https://en.wikipedia.org/wiki/List_of_Indian_dishes')

foodname = driver.find_elements_by_xpath("//tbody/tr/td[position()=1]")

foodlist = [remove_space(x.text) for x in foodname if x.text != '']

for i in foodlist:
    print(i)

print(len(foodlist))

driver.quit()

food = pd.DataFrame(foodlist, columns=['food_name'])
food.to_csv('food.csv')
