import requests
import json

#API URL
url = "https://jsonplaceholder.typicode.com/posts"
request_json = json.loads(requests.json())

response = requests.post(url, request_json)

#validating response code
assert response.status_code == 200