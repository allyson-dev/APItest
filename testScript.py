import requests
import re

from azure.storage.blob import BlockBlobService

r = requests.get('https://api.chucknorris.io/jokes/random')

#define parameters
storageAccountName = 'apibatchblob'
storageKey = 'Rsow5Dky7k7i7ChhV5iToRsYqbnWpVzWQHeAL7xYWRnYwsg4OcCUmDUXQX7Mr3B3iojRVxYWDpJUUhoJKYjoYg=='
containerName = 'output'

#establishing connection
blobService = BlockBlobService(account_name = storageAccountName, account_key= storageKey)

#upload

with open('output.json', 'wb') as f:
    f.write(r.content)

blobService.create_blob_from_bytes(containerName, 'output.json', 'output.json')