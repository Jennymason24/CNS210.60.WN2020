#!/usr/bin/python

import urllib
import urllib2

url = "http://3.17.10.219/forms/action_page.php"
data = {'fname': 'kate', 'lname': 'vajda', 'submit' : 'Submit'}
params = url(lib.urlencode(data)
request = urllib2.Request(url, data=params)
handle = urllib2.urlopen(request)
page = handle.read()
print(page)