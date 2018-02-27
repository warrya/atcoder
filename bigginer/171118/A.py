# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 01:16:26 2017

@author: Yuki
"""

num = input()

if num[0] == num[1] and num[0] ==num[2]:
    print('Yes')
elif num[1] == num[2] and num[2] ==num[3]:
    print('Yes')
else:
    print('No')
