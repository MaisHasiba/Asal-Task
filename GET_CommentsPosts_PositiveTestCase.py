import json
import requests
#import pytest
requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')

response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
response.status_code

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

    def read_data(test_id):
        response_json = json.loads(response.json())
        #variable = response_json["id"]
        #id = payload["Player_id"]
        if test_id in response_json:
            entry = response_json[id]
            return {"Code": 200,
                    "Response": {"userId": entry[0], "id": entry[1], "title": entry[2], "body": entry[3]},
                    "Message": "Read Operation Succesful"}

        else:
            return {"Code": 404, "Message": "ID does not exists"}

    # API Testing Function

    # Testing function
#For Passed Testing / Valid ID
    test_id = {
        "TestID": 1
    }


    def test_read_player():
        response = read_data(test_id)
        assert response.get("Code") == 200