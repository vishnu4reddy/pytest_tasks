import requests

def test_get():
    resp = requests.get("https://reqres.in/api/users/23")
    json_response = resp.json()
    print(json_response)
    # print(resp.json())
    # assert resp.json == 404
    assert json_response == {}
    # # assert (json_response[""]) == 2
    # print(json_response["data"]["first_name"])
    # assert (json_response["data"]["first_name"]) == 'Janet'