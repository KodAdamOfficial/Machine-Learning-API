# -*- coding: utf-8 -*-

import requests

url = 'http://127.0.0.1:3000/api/'

payload = {
        'exp':1.8        
}

r = requests.post(url, json=payload)

print(r.json())