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
      translation = translate('en','de','car')
      self.assertEqual( translation, 'Auto')      

  def test_bidirectional(self):
      """
      Test bidirectional feature of the word
      'Car' translated to 'Auto' in German
      'Auto' translated to 'Automobile' in English
      
      'dog' translated to 'Hund' in German
      'Hund' translated to 'dog' in English
      
      """
      word_en = 'car'
      false_case = is_bidirection_translation('en','de',word_en)
      self.assertFalse( false_case )
      
      word_en = 'dog'
      true_case = is_bidirection_translation('en','de',word_en)
      self.assertTrue( true_case )

      


  
if __name__ == '__main__':
    unittest.main()