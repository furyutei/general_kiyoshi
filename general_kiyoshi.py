# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import random
import collections

def general_kiyoshi( phrase_pattern, last_phrase, debug = False ):
  phrase_pattern = collections.deque( phrase_pattern )
  phrases = list( set( phrase_pattern ) )
  current_phrase_pattern = collections.deque( [], len( phrase_pattern ) )
  if debug:
    phrase_dict = dict( zip( phrases, [ 0 ] * len( phrases ) ) )
  
  def random_phrase_generator():
    while True:
      yield random.choice( phrases )
  
  def check_phrase_pattern():
    return ( current_phrase_pattern == phrase_pattern )
  
  for phrase in random_phrase_generator():
    print( phrase )
    if debug:
      phrase_dict[ phrase ] += 1
    
    current_phrase_pattern.append( phrase )
    
    if check_phrase_pattern():
      break
  
  print( last_phrase )
  if debug:
    for phrase in phrases:
      print( '{phrase} : {count}'.format( phrase = phrase, count = phrase_dict[ phrase ] ) )


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
