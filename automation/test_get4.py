import requests

def test_get():
    resp = requests.get("https://reqres.in/api/unknown")
    json_response = resp.json()
    print(json_response["data"])
    assert (json_response["data"][1]["id"]) == 2
    print(json_response["data"][0]["color"])
    assert (json_response["data"][0]["year"]) == 2000