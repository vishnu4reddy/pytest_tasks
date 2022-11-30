import json
import requests
payload={
    "name": "morpheus",
    "job": "zion resident"
}

def testpost():
    resp = requests.post("https://reqres.in/api/users/2",data=payload)
    # data = json.loads(open("data.json","r").read()))
    print(resp)
    print(resp.json()["name"])
    assert resp.json()['id']!= 95