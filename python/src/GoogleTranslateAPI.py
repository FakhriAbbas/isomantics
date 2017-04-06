#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:00:23 2017

@author: Fakhri Abbas 
"""

from urllib.request import urlopen
import urllib
import json

def translate(source_lang,target_lang,source_text):
    """Return Google Translation for a given word
    Language codes can be found under:
        https://ctrlq.org/code/19899-google-translate-languages
        
    Keyword arguments:
    source_lang -- The language code for the source text argument
    target_lang -- The language code for the translated language
    source_text -- Text to be translated
    """
    
    # free google API translation
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=" \
        + source_lang + "&tl=" + target_lang + "&dt=t&q=" + (source_text)

    
    req = urllib.request.Request(url, headers={'User-Agent' : "Any Browser"}) 
    con = urllib.request.urlopen( req )
    string_result = con.read().decode('utf-8').split('"')[1]
    return (string_result)

def is_bidirection_translation(source_lang,target_lang,source_text):
    """Return a given word in source language is bidirectional 
    Language codes can be found under:
        https://ctrlq.org/code/19899-google-translate-languages
        
    Keyword arguments:
    source_lang -- The language code for the source text argument
    target_lang -- The language code for the translated language
    source_text -- Text to be translated
    """

    translated_word = translate(source_lang,target_lang,source_text)
    word = translate(target_lang,source_lang,translated_word)
    if word == source_text:
        return True
    else:
        return False
    
if __name__ == '__main__':
  print (translate('en','de','dog'))
  print (translate('de','en','Auto'))
  