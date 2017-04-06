#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:00:23 2017

@author: Fakhri Abbas 
"""

from urllib.request import urlopen
from urllib.parse import urlencode
import urllib
import json
    
def translate(text, from_lang, to_lang):
    # taken and modified from 
    # http://codegist.net/snippet/python/google-translatepy_lotabout_python

    
    
    url = 'https://translate.googleapis.com/translate_a/single?'
 
    params = []
    params.append('client=gtx')
    params.append('sl=' + from_lang)
    params.append('tl=' + to_lang)
    params.append('hl=en-US')
    params.append('dt=t')
    params.append('dt=bd')
    params.append('dj=1')
    params.append('source=input')
    params.append(urlencode({'q': text}))
    url += '&'.join(params)
 
    request = urllib.request.Request(url)
    browser = "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
    request.add_header('User-Agent', browser)
    response = urllib.request.urlopen(request)
    dictionary = json.loads(response.read().decode('utf8'))
    return dictionary["sentences"][0]['trans']
    
def is_bidirection_translation(source_text,source_lang,target_lang):
    """Return a given word in source language is bidirectional 
    Language codes can be found under:
        https://ctrlq.org/code/19899-google-translate-languages
        
    Keyword arguments:
    source_lang -- The language code for the source text argument
    target_lang -- The language code for the translated language
    source_text -- Text to be translated
    """

    translated_word = translate(source_text , source_lang,target_lang)
    word = translate(translated_word , target_lang ,source_lang  )
    if word == source_text:
        return True
    else:
        return False
    
if __name__ == '__main__':
  print(translate("собака" , 'ru','en'))
  print(translate( "laptop" , 'en' , 'zh-CN') ) 
  print(translate('dog' , 'en' , 'de' ))
  print(translate('Hund' , 'de' , 'en' ))
  print(translate('ذهب' , 'ar' , 'en' ))
  print(translate('go' , 'en' , 'he' ))
  
  
  