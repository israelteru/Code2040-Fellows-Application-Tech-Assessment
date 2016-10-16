import json
import requests

payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365', 'github': 'https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment'})
r = requests.post('http://challenge.code2040.org/api/register', params = payload)

payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365'})
r = requests.post('http://challenge.code2040.org/api/reverse', params = payload)

print r.text

originalString = json.loads(r.text)

reversedString = originalString[::-1]

payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365', 'answer': reversedString})
r = requests.post('http://challenge.code2040.org/api/reverse/validate', params = payload)
