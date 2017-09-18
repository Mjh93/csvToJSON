import httplib, urllib
import csv, json

def read_and _convert_csv_to_json
params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("127.0.0.1:7800")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print response.status, response.reason

data = response.read()
data

conn.close()