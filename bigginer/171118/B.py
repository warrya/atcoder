# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 01:19:14 2017

@author: Yuki
"""

n = int(input())
n += 1
ln0 = 2
ln1 = 1
if n == 0:
    print(ln0)
elif n==1:
    print(ln1)
else:
    for i in range(n-2):
        now = ln1
        ln1 = ln1+ln0
        ln0 = now
    print(ln1)

