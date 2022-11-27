#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:05:56 2022

@author: philipp
"""

def importIntList(filename: str) -> list[int]:
    int_list = []
    with open(filename, 'r') as file_handle:
        int_list = [int(item) for item in file_handle.read().split()]
    return int_list



if __name__ == '__main__':
    filename = 'importIntList.testdata'
    int_list = importIntList(filename)
    if type(int_list) == type(list()) and type(int_list[0]) == type(int()):
        print('Successfully imported list of integer')
    else:
        print('Fail')