#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 00:06:38 2018

@author: piotr
"""
import get_info

url = 'https://www.youtube.com/watch?v=T8GqaPNan6k'

def get_stream_map_list():
    video_links = []
    for video_stream in get_info.get_info()['url']:
        if "googlevideo" == video_stream.split('/')[2].split('.')[1]:
            video_links.append(video_stream)
    return video_links

print(get_stream_map_list())

