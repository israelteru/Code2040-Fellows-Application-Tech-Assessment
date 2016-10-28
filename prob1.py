import json, requests

myToken = 'ef24eaa8e037499e9eb6b829328a1365'
githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = {'token': myToken, 'github': githubURL}
r = requests.post('http://challenge.code2040.org/api/register', payload)

payload = {'token': myToken}
r = requests.post('http://challenge.code2040.org/api/reverse', payload)

originalString = r.text

# reverse a string
reversedString = originalString[::-1]

payload = {'token': myToken, 'string': reversedString}
r = requests.post('http://challenge.code2040.org/api/reverse/validate', payload)
