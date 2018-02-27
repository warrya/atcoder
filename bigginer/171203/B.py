# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 01:43:15 2017

@author: Yuki
"""

x = int(input())

keta = len(str(x))

f = []
for i in range(keta):
    f.append(int(str(x)[i]))
f = sum(f)

if x%f == 0:
    print('Yes')
else:
    print('No')