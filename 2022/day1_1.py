#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:41:46 2022

@author: philipp
"""

filename = 'day1_1.input'
liste = []
with open(filename, 'r') as file_handle:
    #int_list = [int(item) for item in file_handle.read().split()]
    elve = 0
    for item in file_handle.readlines():
        if item.strip() != '':
            elve += int(item.strip())
        else:
            liste += [elve]
            elve = 0
print(max(liste))

print(sum(sorted(liste, reverse=True)[:3]))
        