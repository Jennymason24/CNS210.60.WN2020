# /usr/bin/python3

import http.client

# Connect to localhost on port 8000
h = http.client.HTTPConnection('localhost', 8000)

# issue a GET response
h.request("GET", "/")

# save the response
data = h.getresponse()

# print the response code
print("Response code: ", data.code)

# print headers
print(data.headers)

# read lines
text = data.readlines()
count=0

# print lines
for t in text:
    print(t.decode('utf-8')) 