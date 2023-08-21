#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range(n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = temp
    if n % 2 == 1:
        mid = n//2
        for i in range(n):
            temp = matrix[mid][i]
            matrix[mid][i] = matrix[mid][n-1-i]
            matrix[mid][n-1-i] = temp
