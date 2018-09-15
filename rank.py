#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 12:04:53 2018

@author: rimeljammal
"""

import numpy as np

a = np.array([[1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4]])
b = np.array([[0, -1, 2, -2], [-7, -7, 2, -8], [0, 4, -6, 6], [2, -2, 0, -2]])
c = np.array([[1, 7, 2, 5], [-2, 1, 1, 5], [-1, 2, 1, 4], [1, 4, 1, 2]])
d = np.array([[1, 2, -4, -2, -1], [0, -2, 4, 2, 0], [1, 1, -2, -1, 1]])
e = np.array([[1, 2, 4], [6, 3, 9], [1, 2, 4], [0, 2, 4]])

def swap_rows(arr, i, j):
    arr[[i, j]] = arr[[j, i]]
    return a

def get_rank(arr):
    rows = np.size(arr, 0)
    columns = np.size(arr, 1)
    rank = rows
    print("Rows:", rows)
    print("Columns:", columns)
    for x in range(0, rows - 1):
        if(arr[x][x] == 0):
            swap_rows(arr, x, x + 1)
        if(arr[x][x] != 0):
            for col in range(x + 1, rows):
                if(arr[col][x] != 0):
                    multiplier = (arr[col][x] / arr[x][x])
                    for w in range(0, columns):
                        arr[col][w] -= multiplier * arr[x][w]
                    print(arr)
                    print('--------')
    zeros = arr.any(axis = 1)
    print(zeros)
    for i in range(0, len(zeros)):
        if(~zeros[i]):
            rank -= 1
    return rank

print(get_rank(f))
