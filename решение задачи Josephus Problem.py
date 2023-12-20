# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:51:50 2023

@author: S.Stycenkov
"""
N = 100
numb_ind = 8
game_range = [(x + 1) for x in range(N)]
len_range = len (game_range)
position = 0
indexpos = 0
print(*game_range)
print('-'*30)

while len(game_range)>1:
    # print(*game_range)
    print(game_range[position], ':\tpos=', position,' indxp=', indexpos, sep="")
    position += 1
    indexpos += 1
    if position >= len(game_range):
        position = 0
    if indexpos == (numb_ind - 1):
        print("[x]:", game_range[position], ' / ', sep=" ", end="")
        game_range.pop(position)
        indexpos = 0
        print(*game_range,"\n")
        # b=input()
    if position >= len(game_range):
        position = 0
        
print('Итоговое число: ',*game_range)