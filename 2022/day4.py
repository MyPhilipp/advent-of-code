#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 17:21:57 2022

@author: philipp
"""
filename = 'day4.input'


with open(filename, 'r') as file_handle:
    fully_contained = 0
    overlap = 0
    for line in file_handle.readlines():
        newline = line.split()[0]
        elve1, elve2 = newline.split(',')
        elve1, elve2 = elve1.split('-'), elve2.split('-')
        elve1 = set(range(int(elve1[0]), int(elve1[1]) + 1))
        elve2 = set(range(int(elve2[0]), int(elve2[1]) + 1))

        # Round 1
        if elve1.difference(elve2) == set() or elve2.difference(elve1) == set():
            fully_contained += 1
        
        # Round 2
        for section in elve1:
            if section in elve2:
                overlap += 1
                break

    print('Round 1:', fully_contained, 'fully contained sections')
    print('Round 2:', overlap, 'overlapping pairs')