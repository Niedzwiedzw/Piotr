#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:42:29 2018

@author: piotr
"""

import urllib.request, urllib.parse

url = 'https://www.youtube.com/watch?v=T8GqaPNan6k'

def get_sourcecode(url):
    return urllib.request.urlopen(url).read()

print(get_sourcecode(url))




