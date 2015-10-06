#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests
import json

import urllib3



#query - send some sort of text to wit.ai
def query(query):
    headers = {'Authorization': 'Bearer ' + key}
    url = 'https://api.wit.ai/message?q=' + urllib.quote(query)
    return requests.get(url, headers = headers)
#queryAudio - send audio file to wit.ai
#key - Server Access Token from Your wit.ai account

def queryAudio(filename,key):
    wav_file = open(filename, 'rb')
    headers = {'Authorization': 'Bearer ' + key, 'Content-Type': 'audio/wav'}
    url =  'https://api.wit.ai/speech?v=20141022'
    data = wav_file
    r = requests.post(url, headers = headers, data = data)
    wav_file.close()
    a = r.text
    a= json.loads(a,encoding = 'iso-8859-2')
    return a
