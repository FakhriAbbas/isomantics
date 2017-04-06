#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:48:25 2017

@author: fabbas1
"""

import unittest
from GoogleTranslateAPI import translate
from GoogleTranslateAPI import is_bidirection_translation

class TestingGoogleTranslateAPI(unittest.TestCase):

  def test_translate(self):
      """
      Test single word tranlsation
      'car' tranlsatoion is 'Auto' in German
      """
      translation = translate('car' , 'en' , 'de')
      self.assertEqual( translation, 'Auto')      

      translation = translate("собака" , 'ru','en')
      self.assertEqual( translation, 'dog')      

      translation = translate( "laptop" , 'en' , 'zh-CN') 
      self.assertEqual( translation, '笔记本电脑')      

      translation = translate('dog' , 'en' , 'de' )
      self.assertEqual( translation, 'Hund')      

      translation = translate('Hund' , 'de' , 'en' )
      self.assertEqual( translation, 'dog')      

      translation = translate('ذهب' , 'ar' , 'en' )
      self.assertEqual( translation, 'Go')      

      translation = translate('go' , 'en' , 'he' )
      self.assertEqual( translation, 'ללכת')      


  def test_bidirectional(self):
      """
      Test bidirectional feature of the word
      'Car' translated to 'Auto' in German
      'Auto' translated to 'Automobile' in English
      
      'dog' translated to 'Hund' in German
      'Hund' translated to 'dog' in English
      
      """
      word_en = 'car'
      false_case = is_bidirection_translation(word_en , 'en','de')
      self.assertFalse( false_case )
      
      word_en = 'dog'
      true_case = is_bidirection_translation(word_en , 'en','de')
      self.assertTrue( true_case )

      


  
if __name__ == '__main__':
    unittest.main()