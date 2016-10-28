import json, requests

myToken = 'ef24eaa8e037499e9eb6b829328a1365'
githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = {'token': myToken, 'github': githubURL}
r = requests.post('http://challenge.code2040.org/api/register', payload)

payload = {'token': myToken}
r = requests.post('http://challenge.code2040.org/api/haystack', payload)

needle = json.loads(r.text)['needle']
haystack = json.loads(r.text)['haystack']

# find the index of a given string in an array
# if given string doesn't exist in array, return -1
index = -1
if needle in haystack:
    index = haystack.index(needle)

payload = {'token': myToken, 'needle': index}
r = requests.post('http://challenge.code2040.org/api/haystack/validate', payload)
