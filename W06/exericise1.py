#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 18:02:05 2019

@author: ranley
"""

import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter location: ')
print('Retrieving', url)
connection = urllib.request.urlopen(url)
data = connection.read().decode()
print('Retrieved', len(data), ' characters')

sum = 0
count = 0
js = json.loads(data)
comments = js['comments']
for comment in comments:
    sum = sum + int(comment['count'])
    count = count + 1

print('Count:', count)
print('Sum:', sum)