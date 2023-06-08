#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 0, 2, 3],
              [4, 0, 5, 6],
              [4, 0, 5, 6],
              [7, 0, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
