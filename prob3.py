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
answer = []
for stringElt in array:
    if not stringElt.startswith(prefix):
        answer.append(stringElt.encode("ascii"))
print answer
#answer = [stringElt.encode("ascii") for stringElt in array if not stringElt.startswith(prefix)]
#print answer
#print answer[0]
payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365', 'array': answer}
r = requests.post('http://challenge.code2040.org/api/prefix/validate', payload)
print r.text

#url = 'http://challenge.code2040.org/api/prefix/validate'
#http = urllib3.PoolManager()
#r = http.request(payload, url)
#r.status


#data = urllib.urlencode(payload)
#data = data.encode('ascii') # data should be bytes
#req = urllib2.Request(url, data, headers)
#response = urllib2.urlopen(req)
#the_page = response.read()

#data = urllib.urlencode(payload)
#req = urllib2.Request(url, payload)
#try:
#    urllib2.urlopen(url)
#except urllib2.HTTPError, e:
#    print e.code
#    print e.msg
#    print e.headers
#    print e.fp.read()
#except urllib2.URLError, e:
#    print e.args
#the_page = response.read()

#encoded_args = urllib.urlencode(payload)
#print urllib.urlopen(url, encoded_args).read()
