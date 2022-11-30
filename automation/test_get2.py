import requests

def test_get():
    resp = requests.get("https://reqres.in/api/users/2")
    json_response = resp.json()
    print(json_response["data"])
    # assert (json_response[""]) == 2
    print(json_response["data"]["first_name"])
    assert (json_response["data"]["first_name"]) == 'Janet'