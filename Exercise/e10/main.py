# import requests
# import json
import os
import time
# url = 'https://cwbackend.com/ihre-loesung'

# r = requests.get(url)

# pages = json.loads(r.text)

# for page in pages['page']:
#     print(page)
    
Int = 10


while True:
    commad = ''' sleep 2; osascript -e 'say "Hello World!"'; osascript -e 'display alert "hello world"' '''

    os.system(commad)
    time.sleep(Int)