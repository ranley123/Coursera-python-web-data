#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:43:58 2019

@author: ranley
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
sum = 0
for tag in tags:
    result = tag.contents[0]
    temp = int(str(result))
    sum = sum + temp

print(sum)