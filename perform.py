import requests
import random
import json

with open('/Users/eric/github/local/clickstream_poetry/samples/fk.json') as fk:
    poem = json.load(fk)
random.shuffle(poem['content'])
for url in poem['content']:
    requests.get(url)
    print url
print 'performed "{}". {}'.format(poem['title'], poem['copyright'])
