# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 01:29:08 2017

@author: Yuki
"""

n = input()
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])

if a+b+c+d==7:
    print(str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)+'=7')
elif a+b+c-d==7:
    print(str(a)+'+'+str(b)+'+'+str(c)+'-'+str(d)+'=7')
elif a+b-c+d==7:
    print(str(a)+'+'+str(b)+'-'+str(c)+'+'+str(d)+'=7')
elif a+b-c-d==7:
    print(str(a)+'+'+str(b)+'-'+str(c)+'-'+str(d)+'=7')
elif a-b+c+d==7:
    print(str(a)+'-'+str(b)+'+'+str(c)+'+'+str(d)+'=7')
elif a-b+c-d==7:
    print(str(a)+'-'+str(b)+'+'+str(c)+'-'+str(d)+'=7')
elif a-b-c+d==7:
    print(str(a)+'-'+str(b)+'-'+str(c)+'+'+str(d)+'=7')

