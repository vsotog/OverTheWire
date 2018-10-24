#!/usr/bin/env python

import requests
import re

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

#response = requests.get(url, auth = (username, password), headers = headers)
session = requests.Session()

response = session.post(url , data = {"secret":"oubWYf2kBq", "submit":"submit"}, auth = (username, password) )
#response = session.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit":"submit"}, auth = (username, password) )
content = response.text

#print session.cookies['loggedin']
#print content
 
print re.findall('The password for natas9 is (.*)', content)[0]