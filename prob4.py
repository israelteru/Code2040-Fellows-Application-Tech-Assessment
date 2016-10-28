import json, requests, iso8601, datetime
from datetime import timedelta

myToken = 'ef24eaa8e037499e9eb6b829328a1365'
githubURL = "https://github.com/israelteru/Code2040-Fellows-Application-Tech-Assessment"
payload = {'token': myToken, 'github': githubURL}

payload = {'token': myToken}
r = requests.post('http://challenge.code2040.org/api/dating', payload)

datestamp = json.loads(r.text)["datestamp"]
interval = json.loads(r.text)["interval"]

# add given number of seconds to a given iso8601 date
datestampToUse = iso8601.parse_date(datestamp)
intervalToUse = datetime.timedelta(seconds=interval)
newDatestamp = (datestampToUse + intervalToUse).isoformat().replace("+00:00", "Z")

payload = {'token': myToken, 'datestamp': newDatestamp}
r = requests.post('http://challenge.code2040.org/api/dating/validate', json = payload)
