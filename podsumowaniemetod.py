#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:58:13 2018

@author: piotr
"""

import urllib.request, urllib.parse

url = 'https://www.youtube.com/watch?v=T8GqaPNan6k'

source = urllib.request.urlopen(url).read()

decode_parse = urllib.parse.parse_qs(source.decode('unicode_escape'))

video_links = []
for video_stream in decode_parse['url']:
    if "googlevideo" == video_stream.split('/')[2].split('.')[1]:
        video_links.append(video_stream)
print(video_links)