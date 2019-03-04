#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:32:28 2019

@author: ranley
"""
import re
handle = open("test.txt")
sum = 0
count = 0;
for line in handle:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) == 0: continue;
    for number in numbers:
        sum = sum + int(number);

print(sum)
    