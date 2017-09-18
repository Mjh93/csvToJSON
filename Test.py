import httplib

conn = httplib.HTTPConnection("127.0.0.1:7800")
conn.request("GET", "/")
r1 = conn.getresponse()
print r1.status, r1.reason

data1 = r1.read()
conn.request("GET", "/")
r2 = conn.getresponse()
print r2.status, r2.reason

data2 = r2.read()
conn.close()