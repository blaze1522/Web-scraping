import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def make_tags(x):
    char_list = [i for i in x]
    for i in char_list:
        if i == ' ':
            char_list.remove(i)
    j = 0
    for j in range(len(char_list)):
        if char_list[j] == '(':
            char_list = char_list[0: j]
            break
        else:
            j += 1
    new = ""
    for s in char_list:
        new += s
    return new.lower()


def wikiscrap():
    options = Options()
    options.page_load_strategy = 'none'

    driver = webdriver.Chrome(executable_path='chromedriver', options=options)
    driver.get('https://en.wikipedia.org/wiki/List_of_Indian_dishes')

    foodname = driver.find_elements_by_xpath("//tbody/tr/td[position()=1]")

    foodlist = [make_tags(x.text) for x in foodname if x.text != '']

    print("No of names scrapped =", len(foodlist))

    driver.quit()

    food = pd.DataFrame(foodlist, columns=['food_name'])
    food.to_csv('food.csv')
