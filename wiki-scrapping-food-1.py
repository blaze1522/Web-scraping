import requests
import bs4
import selenium
from selenium import webdriver

not_food_list = ['Vegetarian', 'Non-Vegetarian', 'Sweet', ]


class hash_tag(object):
    pass


def foodname(x):
    inputs = list(map(str, x.split()))
    y = 0
    if len(inputs) <= 3 & len(inputs) > 0:
        if inputs[0] not in not_food_list:
            if inputs[0][0] != '[':
                y += 1
    if y == 1:
        return True
    else:
        return False


def remove_space(x):
    char_list = [i for i in x]
    for i in char_list:
        if i == ' ':
            char_list.remove(i)
    new = ""
    for s in char_list:
        new += s
    return new


def scraping_wiki():
    res = requests.get('https://en.wikipedia.org/wiki/List_of_Indian_dishes')
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    foodtable = soup.select("body table tbody tr td")
    j = 0
    foodlist = []

    for i in foodtable:
        j += 1
        if foodname(i.text):
            foodlist.append(remove_space(i.text).lower())
        if j == 1212:
            break
    return foodlist


tags = scraping_wiki()

print(len(tags))

for i in tags:
    print(i)

print(tags)

# https://www.instagram.com/explore/tags/aloogobi/


insta_url = 'https://www.instagram.com/explore/tags/' + tags[5] + '/'

# driver = webdriver.Chrome(
#  executable_path = r'C:\Users\Goirik\AppData\Local\Google\Chrome\Application\chromedriver.exe')
# res=driver.get(insta_url)
