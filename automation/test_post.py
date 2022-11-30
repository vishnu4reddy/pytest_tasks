import json
import requests
payload={
    "name": "morpheus",
    "job": "leader"
}

def testpost():
    resp = requests.post("https://reqres.in/api/users",data=payload)
    # data = json.loads(open("data.json","r").read()))
    print(resp)
    print(resp.json())
    assert resp.json()['job']== 'leader'