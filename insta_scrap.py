'''
Only first 4 tags will be explored. See line 30.
If the page does not load in 15 seconds then it will be skipped even if it is a valid hashtag.
If you have slow internet the increase timeout time in insta_tag.py.
'''

import pandas as pd
import wiki_scrapping_food
from insta_tag import hashtags

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
    x = hashtags(tags[i])
    images = x.get_img()
    dict_tags[tags[i]] = images
    if i == 4:
        break

print("Number of pages read =", len(dict_tags))

# This Dictionary can now be used
# print(dict_tags)
# print(len(dict_tags))
