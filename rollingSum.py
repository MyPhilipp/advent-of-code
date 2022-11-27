#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 18:08:42 2022

@author: philipp
"""

def rollingSum(int_list: list[int]) -> int:
    rolling_sum = []
    for index in range(len(int_list) - 2):
        rolling_sum.append(sum(int_list[index:index+3]))
    return rolling_sum

if __name__ == '__main__':
    int_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    if rollingSum(int_list) == [607, 618, 618, 617, 647, 716, 769, 792]:
        print('Function correct')
    else:
        print('Fail')