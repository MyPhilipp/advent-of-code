#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:46:35 2022

@author: philipp
"""
filename = 'day3.input'

def itemTypeValue(item_type):
    item_value = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return item_value.index(item_type) + 1

compartment_list = list()
with open(filename, 'r') as file_handle:
    item_priority_sum = 0
    for line in file_handle.readlines():
        compartment_list.append(line.split())
        print(line)
        compartment1 = line[:len(line)//2]
        compartment2 = line[len(line)//2:]
        print(compartment1)
        print(compartment2)
        
        item_types = list()
        
        for item_type in compartment1:
            if item_type in compartment2 and item_type not in item_types:
                item_types.append(item_type)
                print(item_type)
                print(itemTypeValue(item_type))
                item_priority_sum += itemTypeValue(item_type)
                print(item_priority_sum)



# Round 2

item_priority_sum = 0

for i in range(len(compartment_list)//3):
    # print(i)
    item_types = list()
    
    for compartment in compartment_list[i * 3][0]:
        for item_type in compartment:
            if item_type in compartment_list[i * 3 + 1][0] and item_type in compartment_list[i * 3 + 2][0] and item_type not in item_types:
                item_types.append(item_type)
                print(item_type)
                item_priority_sum += itemTypeValue(item_type)
print(item_priority_sum)
