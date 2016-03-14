# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import random

def general_kiyoshi( phrase_pattern, last_phrase ):
  phrase_pattern_number = len( phrase_pattern )
  phrase_dict = dict( zip( phrase_pattern, [ 0 ] * phrase_pattern_number ) )
  phrases = phrase_dict.keys()
  
  def random_phrase_generator():
    while True:
      yield phrases[ random.randint( 0, len( phrases ) - 1 ) ]
  
  def check_phrase_pattern( current_phrase_pattern ):
    for index in range( 0, phrase_pattern_number ):
      if phrase_pattern[ index ] != current_phrase_pattern[ index ]:
        return False
    return True
  
  current_phrase_pattern = [ None ] * phrase_pattern_number
  
  for phrase in random_phrase_generator():
    print( phrase )
    #phrase_dict[ phrase ] += 1
    
    current_phrase_pattern.pop( 0 )
    current_phrase_pattern.append( phrase )
    
    if check_phrase_pattern( current_phrase_pattern ):
      print( last_phrase )
      '''
      #for phrase in phrases:
      #  print( '{phrase} : {count}'.format( phrase = phrase, count = phrase_dict[ phrase ] ) )
      '''
      break

if __name__ == '__main__':
  def kiyoshi():
    general_kiyoshi( [ 'ズン', 'ズン', 'ズン', 'ズン', 'ドコ' ], 'キ・ヨ・シ！' )
  
  def cockrobin():
    general_kiyoshi( [ 'パパンがパン', '誰が殺した', 'クックロビン', '誰が殺した', 'クックロビン' ], 'スズメが弓と矢でもって、クックロビンを殺したの' )
  
  print( '■ kiyoshi()' )
  kiyoshi()
  print( '' )
  
  print( '■ cockrobin()' )
  cockrobin()
  print( '' )
