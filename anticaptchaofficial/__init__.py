import requests

default_headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

session = requests.Session()
session.headers.update(default_headers)