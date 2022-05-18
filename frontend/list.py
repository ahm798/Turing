
import requests
from getpass import getpass

username = input("username:   ")
password = getpass("password:   ")

endpoint = 'http://127.0.0.1:8000/api/auth/'

response = requests.post(endpoint, json={"username": username, 'password': password})

if response.status_code == 200:
    endpoint = 'http://127.0.0.1:8000/api/blog/articles/'
    token = response.json()['token']
    headersv2 = {'authorization': f'token {token}'}
    response_v2 = requests.get(endpoint, headers=headersv2)
    data = response_v2.json()
    next_url = data['next']
    if next_url is not None:
        res = requests.get(next_url, headers=headersv2)
        print(res.json())