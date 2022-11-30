import json
import requests
payload={
    "name": "morpheus",
    "job": "zion resident"
}

def test_testpost():
    resp = requests.post("https://reqres.in/api/users/2",data=payload)
    # data = json.loads(open("data.json","r").read()))
    print(resp)
    print(resp.json())
    assert resp.json()['job']== 'zion resident'