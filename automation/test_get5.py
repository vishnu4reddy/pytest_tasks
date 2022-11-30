import requests

def test_get():
    resp = requests.get("https://reqres.in/api/unknown/2")
    json_response = resp.json()
    print(json_response["data"]["name"])
    assert (json_response["data"]["id"]) == 2
    print(json_response["support"]["text"])
    assert (json_response["support"]["text"]).startswith("To")