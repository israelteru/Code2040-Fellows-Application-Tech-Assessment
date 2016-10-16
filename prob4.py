import json
import requests
import iso8601
import datetime
from datetime import timedelta

githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365', 'github': githubURL})

payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365'})
r = requests.post('http://challenge.code2040.org/api/dating', payload)


originalContent = json.loads(r.text)
datestamp = originalContent["datestamp"]
interval = originalContent["interval"]

datestampToUse = iso8601.parse_date(datestamp)
intervalToUse = datetime.timedelta(seconds=interval)
newDatestamp = (datestampToUse + intervalToUse).isoformat

payload = json.dumps({'token': 'ef24eaa8e037499e9eb6b829328a1365', 'datestamp': newDatestamp})
r = requests.post('http://challenge.code2040.org/api/reverse/validate', payload)
