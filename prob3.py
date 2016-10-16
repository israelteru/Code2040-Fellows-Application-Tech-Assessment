import json
import requests

githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365', 'github': githubURL})
r = requests.post('http://challenge.code2040.org/api/register', payload)

payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365'})
r = requests.post('http://challenge.code2040.org/api/prefix', payload)

originalContent = json.loads(r.text)
prefix = originalContent["prefix"]
array = originalContent["array"]

answer = [stringElt for stringElt in array if not stringElt.startswith(prefix)]

payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365', 'array': answer})
r = requests.post('http://challenge.code2040.org/api/reverse/validate', payload)
