from facebook_scraper import get_posts
from facebook_scraper import *
from staty import *
from resources import creds  # put your login info in this file and variable locally

#merge1
print(4)
for post in get_posts(group='1543813289196226/', credentials=creds, pages=1):
    print(post['text'][:50])

