#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:54:29 2022

@author: philipp
"""

import re
from copy import deepcopy
filename = 'day5.input'


def getCratesPerLine(line: str) -> list:
    crates_per_line = list()
    for crate in range(len(line)//4):
        #print(crate)
        if line[1+crate * 4] != ' ':
            crates_per_line.append(line[1+crate * 4])
        else:
            crates_per_line.append(None)
    #print(crates_per_line)
    return crates_per_line    

def getArrangements(line: str) -> list:
    quantity, origin, destination = re.findall('[0-9]+', line)
    return int(quantity), int(origin), int(destination)

def getInput(filename):
    stack_input = list()
    arrangement_input = list()
    with open(filename, 'r') as file_handle:
        CRATES = True
        ARRANGEMENTS = False
        for index, line in enumerate(file_handle.readlines()):            
            try:
                if line[1] == '1':
                    CRATES = False
                    #print(line)
            except:
                pass
            if CRATES:
                stack_input.append(getCratesPerLine(line))
            elif ARRANGEMENTS:
                arrangement_input.append(getArrangements(line))
            if line == '\n':
                ARRANGEMENTS = True
    return stack_input, arrangement_input

def getStacksFromInput(stack_input):
    stacks = list()
    for stack in range(len(stack_input[0])):
        stacks.append([])
        
    for i in range(len(stack_input)):
        for j in range(len(stack_input[0])):
            if stack_input[i][j]:
                stacks[j].append(stack_input[i][j])
    
    for i in range(len(stacks)):
        stacks[i].reverse()
        
    return stacks

def printSolution(stacks, part: int):
    tops = str()
    for stack in stacks:
        tops += stack[-1]
    print('Solution Part', part, ':', tops)

def arrangePart1(stacks, arrangement_input):
    for quantity, origin, destination in arrangement_input:
        for q in range(quantity):
            pop_crate = stacks[origin - 1].pop()
            stacks[destination - 1].append(pop_crate)
    return stacks


def arrangePart2(stacks, arrangement_input):
    for quantity, origin, destination in arrangement_input:
        crates = stacks[origin - 1][-1 * quantity :]
        for q in range(quantity):
            stacks[origin - 1].pop()
        stacks[destination - 1] += crates
    return stacks

stack_input, arrangement_input = getInput(filename)


stacks = getStacksFromInput(stack_input)    


rearranged_stacks_1 = arrangePart1(deepcopy(stacks), arrangement_input)
rearranged_stacks_2 = arrangePart2(deepcopy(stacks), arrangement_input)
    
print(stacks)
print(rearranged_stacks_1)
print(rearranged_stacks_2)

printSolution(rearranged_stacks_1, 1)
printSolution(rearranged_stacks_2, 2)


