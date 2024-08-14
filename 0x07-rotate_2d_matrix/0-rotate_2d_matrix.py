#!/usr/bin/python3
"""0-rotate_2d_matrix.py"""


def rotate_2d_matrix(matrix):
    """ a func to rotate a square matrix"""
    new_arr = []
    for i in range(len(matrix)):
        col = []
        for j in range(len(matrix[i])):
            col.append(matrix[j][i])
        new_arr.append(col[::-1])
    for x in range(len(new_arr)):
        for y in range(len(new_arr)):
            matrix[x][y] = new_arr[x][y]
    return matrix
