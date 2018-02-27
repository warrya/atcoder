# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 03:05:36 2017

@author: Yuki
"""
#import numpy as np
n = int(input())
shop_i = []
for i in range(n):
    shop_i.append(list(map(int, input().split())))
gain_i = []
for i in range(n):
    gain_i.append(list(map(int, input().split())))

gain_max = -10000000000000
for i in range(2**10):
    if i ==0:
        pass
    else:        
        shop_sister = format(i, '010b')
        gain_now = []
        for shop in range(n):
            times = 0
            for n_cap in range(10):
                if shop_i[shop][n_cap] == 1 and shop_sister[n_cap] == '1':
                    times += 1
            gain_now.append(gain_i[shop][times]) 
        gain_now = sum(gain_now)
        if gain_now>gain_max:
            gain_max = gain_now

print(gain_max)

#3
#1 1 1 1 1 1 0 0 1 1
#0 1 0 1 1 1 1 0 1 0
#1 0 1 1 0 1 0 1 0 1
#-8 6 -2 -8 -8 4 8 7 -6 2 2
#-9 2 0 1 7 -5 0 -2 -6 5 5
#6 -6 7 -9 6 -5 8 0 -9 -7 -7