#!/bin/python2.7

import urllib2
import requests

gh_url = 'https://api.github.com'


req = urllib2.Request(gh_url)


r = requests.get('http://google.com')
print r.status_code
print r.headers['content-type']
print  r.encoding
print  r.text

response = requests.get('https://python.org')

print response.request.headers

print response.headers

print response.status_code

k  = requests.get('https://python.org', verify=True)
print k.status_code
