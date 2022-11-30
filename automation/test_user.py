import requests
import json
import jsonpath



# api url
url = "https://reqres.in/api/users?page=2"

# send get requerst
response = requests.get(url)

# display responce content
# print(response._content)
# print(response.headers)

# parse responcee to json format
json_response = json.loads(response.text)
# print(json_response)

# fetch value using json path
pages = jsonpath.jsonpath(json_response,'total_pages')
assert pages[0] == 2