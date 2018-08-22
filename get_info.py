#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:58:50 2018

@author: piotr
"""

import urllib.request, urllib.parse
import get_sourcecode

url = 'https://www.youtube.com/watch?v=T8GqaPNan6k'

def get_info():
    return urllib.parse.parse_qs(get_sourcecode.get_sourcecode(url).decode('unicode_escape'))

print(get_info())