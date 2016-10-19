import json
import requests


githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365', 'github': githubURL}
r = requests.post('http://challenge.code2040.org/api/register', payload)

payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365'}
r = requests.post('http://challenge.code2040.org/api/haystack', payload)

needle = json.loads(r.text)['needle']
haystack = json.loads(r.text)['haystack']

# find the index of a given string in an array
index = -1
if needle in haystack:
    index = haystack.index(needle)

payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365', 'needle': index}
r = requests.post('http://challenge.code2040.org/api/reverse/validate', payload)
