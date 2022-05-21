
import requests
from getpass import getpass

username = input("username:   ")
password = getpass("password:   ")

endpoint = 'http://127.0.0.1:8000/api/auth/'

response = requests.post(endpoint, json={"username": username, 'password': password})

data = {
    'topic': {
        'name': 'java'
    },
    'title': "fuckin python",
    'slug': 'ahmed-ssddpfffython',
    'content': 'hhhhhhhhhhhhhhhhhhhhhhhhh',
    'status': 'published'
}

if response.status_code == 200:
    endpoint = 'http://127.0.0.1:8000/api/blog/articles/create/'
    token = response.json()['token']
    headersv2 = {'authorization': f'token {token}'}
    response_v2 = requests.post(endpoint, json=data,headers=headersv2)
    print(response_v2.json())
