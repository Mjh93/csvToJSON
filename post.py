import httplib, urllib
import csv, json
import sys


def post_to_server(json_object, url):
    params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(url)
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    if response.status != 200:
        sys.exit(-2)
    print response.status, response.reason
    data = response.read()
    conn.close()


def main():
    csv_file = open(sys.argv[1], 'rU')
    json_file = open('file.json', 'w')
    reader = csv.reader(csv_file)
    fieldnames = next(reader)
    reader = csv.DictReader(csv_file, fieldnames)
    for row in reader:
        json.dump(process_entry(row), json_file)
        json_file.write('\n')  #TODO this should be changed if handling large csv files
    return json_file


def process_entry(entry):
    # print("Some generic unknown processing here")
    return(entry)


if __name__ == "__main__":
    if sys.argv.__len__() > 1:
        json_object = main()
        post_to_server(json_object, sys.argv[2])
        sys.exit(0)
    else:
        print("FAILED: No csv file given.")
        sys.exit(-1)