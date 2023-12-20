# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 14:22:59 2023

@author: S.Stycenkov
"""
u = [int(i) for i in input().split()]

ind = 0
for i in range(len(u) - 1):
    if u[ i + 1 ] > u [i] : ind += 1

print(ind)

# nums = tuple(map(int, input().split()))
# print(sum(1 for i in range(1, len(nums)) if nums[i-1] < nums[i]))