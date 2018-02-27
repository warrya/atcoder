# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:40:47 2018

@author: Yuki
"""

a, b = map(int,input().split())

product = a*b

if product%2 == 0:
    print('Even')
else:
    print('Odd')
