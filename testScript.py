import requests
import re

from azure.storage.blob import BlockBlobService

r = requests.get('https://api.chucknorris.io/jokes/random')


#upload

with open('output.json', 'wb') as f:
    f.write(r.content)

