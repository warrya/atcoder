# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:12:27 2017

@author: Yuki
"""

n, k = map(int, input().split())
a_s = input().split()

kind = []
for i in range(n):
    a_s[i] = int(a_s[i])
    if a_s[i] in kind:
        pass
    else:
        kind.append(a_s[i])

kind_suuzi = len(kind)
a_s_suuzi = len(a_s)
now_shurui = len(kind)
if k>=kind_suuzi:
    print(0)
else:
    kind_nums = [0 for x in range(kind_suuzi)]
    for i in range(kind_suuzi):
        for ii in range(a_s_suuzi):
            if a_s[ii] == kind[i]:
                kind_nums[i] += 1
    cnt = 0
    kind_nums_sorted = sorted(range(len(kind_nums)), key=kind_nums.__getitem__)
    for i in range(1000000):
        cnt += kind_nums[kind_nums_sorted[i]]
        now_shurui -= 1
        if k == now_shurui:
            print(cnt)
            break


