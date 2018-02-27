# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:07:34 2017

@author: Yuki
"""

N, C = map(int, input().split())
s_list = []
t_list = []
c_list = []
for i in range(N):
    s_i, t_i, c_i = map(int, input().split())
    s_list.append(s_i)
    t_list.append(t_i)
    c_list.append(c_i)


time = [0 for i in range(max(t_list))]

for i in range(N):
    rg = t_list[i]-s_list[i]+1
    for ii in range(rg):
        time[s_list[i]+ii-1] += 1

print(max(time))

