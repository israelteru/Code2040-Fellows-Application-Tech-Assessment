import json, requests

myToken = 'ef24eaa8e037499e9eb6b829328a1365'
githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = {'token': myToken, 'github': githubURL}
r = requests.post('http://challenge.code2040.org/api/register', payload)

payload = {'token': myToken}
r = requests.post('http://challenge.code2040.org/api/prefix', payload)

prefix = json.loads(r.text)["prefix"]
array = json.loads(r.text)["array"]

# exclude strings that start with given prefix in new answer array
answer = [stringElt for stringElt in array if not stringElt.startswith(prefix)]

payload = {'token': myToken, 'array': answer}
r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = payload)
