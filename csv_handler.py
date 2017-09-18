import csv
import json
import socket
import urllib2

with open('us-500.csv', 'rU') as csv_file:
        csv_reader = csv.reader(csv_file)
        json_str = ""
        for row in csv_reader:
            json_str += json.dumps(row)
            row = json.loads(json_str)
            # print ', '.join(row)


test_data ='This is the string I want to send to the server'
jsonObj = json.dumps(test_data)

data = jsonObj
