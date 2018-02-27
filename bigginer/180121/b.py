# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:43:47 2018

@author: Yuki
"""

a, b = map(int,input().split())


if b//10 == 0:
    n = 10*a+b
elif b//10 == 1:
    n = 100*a+b
else:
    n = 1000*a+b

heihou = int(n**0.5)

if heihou**2 != n:
    print('No')
else:
    print('Yes')

