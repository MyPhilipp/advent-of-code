#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:24:35 2022

@author: philipp
"""

def depthIncrease(sonar_sweep: list[int]) -> int:
    increase = 0
    depth_old = sonar_sweep[0]
    for depth in sonar_sweep[1:]:
        if depth > depth_old:
            increase += 1
        depth_old = depth
    return increase



if __name__ == "__main__":
    with open('depthIncrease.input', 'r') as fh:
        sonar_sweep = [int(depth) for depth in fh.read().split()]
        print('Test answer for input: ', depthIncrease(sonar_sweep))
    