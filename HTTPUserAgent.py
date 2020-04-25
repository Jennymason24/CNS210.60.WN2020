import httplib

host = "hostname"

req = httplib.HTTP(host)
req.putrequest("GET", "/")
req.putheader("Host", host)
req.putheader("User-Agent", "Test browser: 4.1")
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Response: ", statusMsg) 