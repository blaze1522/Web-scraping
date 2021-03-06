import requests
import bs4
import pickle
import pandas as pd


def make_tags(x):
    char_list = [i for i in x]
    # Remove spaces
    for i in char_list:
        if i == ' ':
            char_list.remove(i)
    # Remove bracketed text
    j = 0
    for j in range(len(char_list)):
        if char_list[j] in ['(', '\n', '/']:
            char_list = char_list[0: j]
            break
        else:
            j += 1
    new = ""
    for s in char_list:
        new += s
    return new.lower()


def wikiscrap():
    res = requests.get('https://en.wikipedia.org/wiki/List_of_Indian_dishes')
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    tables = soup.findAll("tbody")
    foodlist = []
    foodname = ''

    # Finding all the names of foods from a wikipedia page

    for table in tables[1:6]:
        for row in table.findAll('tr')[1:]:
            foodname = row.findAll('td')[0].text
            foodlist.append(make_tags(foodname))

    print("No of names scrapped =", len(foodlist))

    food = pd.DataFrame(foodlist, columns=['food_name'])
    food.to_csv('food.csv')

    return foodlist
