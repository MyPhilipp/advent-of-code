#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 01:17:02 2022

@author: philipp
"""

def shapeValue(shape):
    if shape == 'rock':
        return 1
    elif shape == 'paper':
        return 2
    elif shape == 'scissor':
        return 3
    else:
        print('ERROR')
        return -10000000000000000
    
def opponentShape(character):
    if character == 'A':
        return 'rock'
    elif character == 'B':
        return 'paper'
    elif character == 'C':
        return 'scissor'
    else:
        print('!!!ERROR!!!!')

def myShape(character):
    if character == 'X':
        return 'rock'
    elif character == 'Y':
        return 'paper'
    elif character == 'Z':
        return 'scissor'
    else:
        print('!!!ERROR!!!!')
        
def roundValue(opponent, me):
    if opponent == me:
        return 3
    elif ((me == 'rock' and opponent == 'scissor') or
          (me == 'paper' and opponent == 'rock') or
          (me == 'scissor' and opponent == 'paper')):
        return 6
    else:
        return 0

def roundOutcomeShape(opponent, outcome):
    if outcome == 'X':
        if opponent == 'rock':
            return 'scissor'
        elif opponent == 'paper':
            return 'rock'
        elif opponent == 'scissor':
            return 'paper'
        else:
            print('ERRORRRRRRRRRRRRRR')
            return -10000000000000000
    elif outcome == 'Y':
        return opponent
    elif outcome == 'Z':
        if opponent == 'rock':
            return 'paper'
        elif opponent == 'paper':
            return 'scissor'
        elif opponent == 'scissor':
            return 'rock'
        else:
            print('ERRORRRRRRRRRRRRR0R')
            return -10000000000000000
    else:
        print('ERRRORRRRRRRRRRRRRRRROOOR')
        return -999999999999999000
        
            
            
filename = 'day2.input'
liste = []
with open(filename, 'r') as file_handle:
    shape_value_1 = 0
    shape_value_2 = 0
    round_value_1 = 0
    round_value_2 = 0
    for line in file_handle.readlines():
        opponent, me = line.split()
        print('Input:', opponent, me)
        opponent_shape = opponentShape(opponent)
        my_shape_1 = myShape(me)
        shape_value_1 += shapeValue(my_shape_1)
        round_value_1 += roundValue(opponent_shape, my_shape_1)
                
        # Round 2
        my_shape_2 = roundOutcomeShape(opponent_shape, me)
        shape_value_2 += shapeValue(my_shape_2)
        round_value_2 += roundValue(opponent_shape, my_shape_2)
    
        print('\t\t', 'Opponent \t', 'Me\t\t', 'Shape Value\t', 'Round Value')
        print('Round1:\t', opponent_shape,'\t\t', my_shape_1, '\t', shape_value_1, '\t\t\t', round_value_1)
        print('Round2:\t', opponent_shape, '\t\t', my_shape_2, '\t', shape_value_2, '\t\t\t', round_value_2)
        print()

            
    
print(sum([shape_value_1, round_value_1]))
    
print(sum([shape_value_2, round_value_2]))
          
    
    
        