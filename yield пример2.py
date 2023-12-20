# -*- coding: utf-8 -*-
"""
Created on Fri May 26 11:56:37 2023

@author: S.Stycenkov
"""

def simple_generator():
  yield 'apple'
  yield 'orange'
  yield 'pear'

for fruit in simple_generator():
  print(fruit)