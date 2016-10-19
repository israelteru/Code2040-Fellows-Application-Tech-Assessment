import json
import requests
import iso8601
import datetime
from datetime import timedelta

githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365', 'github': githubURL}

payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365'}
r = requests.post('http://challenge.code2040.org/api/dating', payload)

datestamp = json.loads(r.text)["datestamp"]
interval = json.loads(r.text)["interval"]

# add given number of seconds to a given iso8601 date to find the new date
datestampToUse = iso8601.parse_date(datestamp)
intervalToUse = datetime.timedelta(seconds=interval)
newDatestamp = (datestampToUse + intervalToUse).isoformat

payload = {'token': 'ef24eaa8e037499e9eb6b829328a1365', 'datestamp': newDatestamp}
r = requests.post('http://challenge.code2040.org/api/dating/validate', payload)
