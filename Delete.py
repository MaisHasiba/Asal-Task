import requests
#import pytest

#API URL
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)

#validating response code
print(response.status_code)
assert response.status_code == 200