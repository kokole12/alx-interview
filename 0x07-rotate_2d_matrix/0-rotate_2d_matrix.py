#!/usr/bin/python3
"""implementing 2D matrix roations

TRANSPOSE
REVERSE
ROTATE
"""


def transpose_matrix(matrix, n):
    """transporsinG the matrix"""
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """Reversng the matrix"""
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """implementing the rotation of the matrix"""
    n = len(matrix)
    transpose_matrix(matrix, n)
    reverse_matrix(matrix)

    return matrix
