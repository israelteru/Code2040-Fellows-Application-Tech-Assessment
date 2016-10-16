import json
import requests

githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365', 'github': githubURL})
r = requests.post('http://challenge.code2040.org/api/register', payload)

payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365'})
r = requests.post('http://challenge.code2040.org/api/reverse', payload)

originalString = json.loads(r.text)["result"]

reversedString = originalString[::-1]

payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365', 'string': reversedString})
r = requests.post('http://challenge.code2040.org/api/reverse/validate', payload)