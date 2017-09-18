import httplib, urllib
import csv, json
import sys


def post_to_server(json_object, url):
    params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(url)
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    conn.close()


def main():
    json_object = ""
    with open(sys.argv[1], 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='\n')
        json_object = json.dumps(next(csv_reader))
        for entry in csv_reader:
            processed_data = process_entry(entry)
            json_object.add(processed_data)

    return json_object


def process_entry(entry):
    print("Some generic unknown processing here")
    return(entry)


if __name__ == "__main__":
    if sys.argv.__len__() > 1:
        json_object = main()
        post_to_server(json_object, "127.0.0.1:7800")
        sys.exit(0)
    else:
        print("FAILED: No csv file given.")
        sys.exit(-1)