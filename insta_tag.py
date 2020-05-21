import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

timeout = 15
driver = webdriver.Chrome(executable_path='chromedriver')


def add_htag(x):
    new = '#'+x
    return new


def remove_htag(x):
    c = [i for i in x]
    c.remove('#')
    new = ""
    for i in c:
        new = new + i
    return new


class hashtags():
    """This is a class of instagram food hashtags."""

    def __init__(self, name, related, num_posts, links):
        self.name = name
        self.related = related
        self.num_posts = num_posts
        self.links = links

    def get_related(self):
        rel_class = "LFGs8.xil3i"
        num_posts_class = "g47SY"

        url = 'https://www.instagram.com/explore/tags/' + self.name + '/'
        driver.get(url)

        # Wait for the required class of elements in this case images to appear.
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, rel_class)))
            print("found")
        except:
            print("skipped")
            return False

        # Pick all the elements with required class
        rel_tags = driver.find_elements_by_class_name(rel_class)
        num_posts_tags = driver.find_elements_by_class_name(num_posts_class)

        # Make a list of related tags
        tag_list = [remove_htag(x.text) for x in rel_tags]
        num_posts = num_posts_tags[0].text

        self.related = tag_list
        self.num_posts = num_posts

        driver.quit()
        return [num_posts, tag_list]


# print(help(hashtags))

food1 = hashtags("aloogobi", [], 0, [])
print(len(food1.get_related()))
print(food1.related)
print(food1.num_posts)
