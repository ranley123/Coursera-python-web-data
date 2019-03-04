#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:15:52 2019

@author: ranley
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
position = input('Enter position: ')
position = int(position)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tag = soup.select('a')[position - 1]
temp = tag.get('href', None)

# Retrieve all of the anchor tags
for i in range(int(count)-1):
    html = urllib.request.urlopen(temp, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.select('a')[position - 1]
    temp = tag.get('href', None)
   
print(tag.contents[0])
    
    