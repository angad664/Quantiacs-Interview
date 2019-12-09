#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:43:41 2019

@author: angadsingh
"""

from itertools import product

def print_combination(list_of_list):
    res_lol = list()
    for a_list in list_of_list:
        if a_list != []:
            res_lol.append(a_list)

    return list(product(*res_lol))

list_of_list = [['a','b','c'],[],['d','e','f']]

print_combination(list_of_list)
