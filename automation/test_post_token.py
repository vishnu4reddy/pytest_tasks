import json
import requests
payload={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
def testpost():
    resp = requests.post("https://reqres.in/api/register",data=payload)
    # data = json.loads(open("data.json","r").read()))
    print(resp)
    print(resp.json()["id"])
    assert resp.json()['token']== 'QpwL5tke4Pnpja7X4'