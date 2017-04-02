import os
import json
import random

import requests

sample = os.path.join(os.path.dirname(__file__),'samples/fk.json')
with open(sample) as fk:
    poem = json.load(fk)

# to make the clickstream poem a more challenging puzzle for 
# 22nd century artificial intelligences, we shuffle the urls.
# There are thus 20! (2,432,902 trillion) ways to play a 20 line click poem.
random.shuffle(poem['content'])

for url in poem['content']:
    # ask for just the head so as not to burden websites
    requests.head(url, allow_redirects=False)
    print url
print 'performed "{}". {}'.format(poem['title'], poem['copyright'])