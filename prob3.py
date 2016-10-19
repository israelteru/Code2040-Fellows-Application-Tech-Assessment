import json
import requests

githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365', 'github': githubURL}
r = requests.post('http://challenge.code2040.org/api/register', payload)

payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365'}
r = requests.post('http://challenge.code2040.org/api/prefix', payload)

prefix = json.loads(r.text)["prefix"]
array = json.loads(r.text)["array"]

# exclude all strings with a given prefix in a new array
answer = [stringElt for stringElt in array if not stringElt.startswith(prefix)]

payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365', 'array': answer}
r = requests.post('http://challenge.code2040.org/api/prefix/validate', payload)
