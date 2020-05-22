import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime


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

    def __init__(self, name, related=[], num_posts=0, img_links=[]):
        self.name = name
        self.related = related
        self.num_posts = num_posts
        self.img_links = img_links
        self.time = datetime.datetime.now()

    def get_data(self):
        """This function fills Related tags, Number of posts and the time at which it was updated for a given hashtag"""

        timeout = 10
        timeout_less = 2

        rel_class = "LFGs8.xil3i"
        num_posts_class = "g47SY"

        url = 'https://www.instagram.com/explore/tags/' + self.name + '/'

        # This code block looks for a browser instance if it doesn't find one then it creates one.
        # This options in the browser instance blocks images and makes loading faster and there is less data consumed.
        try:
            driver.get(url)
        except:
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(
                executable_path='chromedriver', chrome_options=chrome_options)
            driver.get(url)

        # Wait for the required class of elements to appear and get the elements.
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, rel_class)))
            rel_tags = driver.find_elements_by_class_name(rel_class)
        except:
            print("skipped related")

        try:
            WebDriverWait(driver, timeout_less).until(
                EC.visibility_of_element_located((By.CLASS_NAME, num_posts_class)))
            num_posts_tags = driver.find_element_by_class_name(
                num_posts_class)
        except:
            print("skipped page")
            driver.quit()
            return False

        # Make a list of related tags and number of posts and assign them to respective attributes.
        tag_list = [remove_htag(x.text) for x in rel_tags]
        num_posts = num_posts_tags.text

        self.related = tag_list
        self.num_posts = num_posts

        # Update the date-time when the information was obtained.
        self.time = datetime.datetime.now()

        driver.quit()
        return [num_posts, tag_list]

    def get_img(self):
        """This function fills the image links attibute"""

        timeout = 15
        img_class = "FFVAD"

        url = 'https://www.instagram.com/explore/tags/' + self.name + '/'

        # This code block looks for a browser instance if it doesn't find one then it creates one.
        try:
            driver.get(url)
        except:
            driver = webdriver.Chrome(executable_path='chromedriver')
            driver.get(url)

        # Wait for the required class of elements to appear and get the elements.
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, img_class)))
            img_elem = driver.find_elements_by_class_name(img_class)
        except:
            driver.quit()
            return False

        # Make a list of related tags and number of posts and assign them to respective attributes.
        img_links = [x.get_attribute('src') for x in img_elem]

        self.img_links = img_links

        driver.quit()
        return img_links

# Test code - Uncomment to use.


'''
food1 = hashtags('aloogobi')
food1.get_data()
print(food1.related)
print(food1.num_posts)
print(food1.time)
print("Number of links =", len(food1.get_img()))
print(food1.img_links)

food2 = hashtags(food1.related[0])
food2.get_data()
print(food2.related)
print(food2.num_posts)
print(food2.time)
print("Number of links =", len(food2.get_img()))
print(food2.img_links)
'''

# Class details

'''
print(dir(hashtags))
print(help(hashtags))
'''
