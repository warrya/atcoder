# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:02:38 2017

@author: Yuki
"""

n = int(input())

a_s = input().split()
for i in range(n):
    a_s[i] = int(a_s[i])

cnt = 0
flag = True
while flag:
    for i in range(n):
        a_s[i] = a_s[i]/2
        if a_s[i]%1 == 0.5:
            print(cnt)
            flag = False
            break
        
    cnt += 1
