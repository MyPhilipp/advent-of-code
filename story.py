#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:43:41 2022

@author: philipp
"""
from importIntList import importIntList
from depthIncrease import depthIncrease
from rollingSum import rollingSum

# Day 1 Part 1
print('There are', depthIncrease(importIntList('depthIncrease.input')), 'larger measurements.')

# Day 1 Part 2
print('There are', depthIncrease(rollingSum(importIntList('depthIncrease.input'))), 'larger sums.')