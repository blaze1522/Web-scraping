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

        try:
            driver.get(url)
            print("Found browser")
        except:
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(
                executable_path='chromedriver', chrome_options=chrome_options)
            driver.get(url)
            print("Didn't find Browser")

        # Wait for the required class of elements in this case images to appear.
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, rel_class)))
            rel_tags = driver.find_elements_by_class_name(rel_class)
        except:
            print("skipped related")

        try:
            WebDriverWait(driver, timeout_less).until(
                EC.visibility_of_element_located((By.CLASS_NAME, num_posts_class)))
            num_posts_tags = driver.find_elements_by_class_name(
                num_posts_class)
        except:
            print("skipped page")
            return False

        # Make a list of related tags
        tag_list = [remove_htag(x.text) for x in rel_tags]
        num_posts = num_posts_tags[0].text

        self.related = tag_list
        self.num_posts = num_posts
        self.time = datetime.datetime.now()

        driver.quit()
        return [num_posts, tag_list]

    def get_img(self):
        """This function fills the image links attibute"""

        timeout = 15
        img_class = "FFVAD"

        url = 'https://www.instagram.com/explore/tags/' + self.name + '/'

        try:
            driver.get(url)
            print("Found browser")
        except:
            driver = webdriver.Chrome(executable_path='chromedriver')
            driver.get(url)
            print("Didn't find Browser")

        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, img_class)))
            img_elem = driver.find_elements_by_class_name(img_class)
        except:
            return False

        img_links = [x.get_attribute('src') for x in img_elem]

        self.img_links = img_links

        driver.quit()

        return img_links

# Test code - Uncomment to use


'''
food1 = hashtags('aloogobi')
print(len(food1.get_data()))
print(food1.related)
print(food1.num_posts)
print(food1.time)
print(len(food1.get_img()))
print(food1.img_links)

food2 = hashtags(food1.related[0])
print(len(food2.get_data()))
print(food2.related)
print(food2.num_posts)
print(food2.time)
print(len(food2.get_img()))
print(food2.img_links)
'''

# Class details

'''
print(dir(hashtags))
print(help(hashtags))
'''
