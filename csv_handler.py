import csv
import json

with open('us-500.csv', 'rU') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            json_str = json.dumps(row)
            row = json.loads(json_str)
            print ', '.join(row)

