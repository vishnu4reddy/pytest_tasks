import json
import requests
payload={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
def testpost():
    resp = requests.post("https://reqres.in/api/register",data=payload)
    data = json.loads(open("data.json","r").read())
    print(resp.content)
    print(resp.json()["id"])
    assert resp.json()['token']== 'QpwL5tke4Pnpja7X4'
    # assert resp.json()["password"]== "pistol"
    # assert resp["data"]["email"]== "pistol"
    # assert 
    print(data["email"])
    assert (data["email"]) == "eve.holt@reqres.in"