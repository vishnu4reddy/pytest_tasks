
import requests
def test_get():
    resp = requests.get("https://reqres.in/api/users?page=2")
    json_response = resp.json()
    print(json_response["total"])
    assert (json_response["total"]) == 12
    print(json_response["data"][0]["id"])
    # assert (json_response["data"][0]["email"]).endswith("reqres.in")
    assert (json_response["data"][0]["id"]) == 7
    print(json_response)