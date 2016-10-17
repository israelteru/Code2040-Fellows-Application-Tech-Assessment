import json
import requests

githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365', 'github': githubURL}
r = requests.post('http://challenge.code2040.org/api/register', payload)

payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365'}
r = requests.post('http://challenge.code2040.org/api/reverse', payload)

originalString = r.text

# reverse a string
reversedString = originalString[::-1]

payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365', 'string': reversedString}
r = requests.post('http://challenge.code2040.org/api/reverse/validate', payload)
