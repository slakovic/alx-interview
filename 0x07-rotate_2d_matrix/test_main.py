#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[7, 4, 1],
              [8, 5, 2],
              [9, 6, 3]]

    rotate_2d_matrix(matrix)
    print(matrix)
