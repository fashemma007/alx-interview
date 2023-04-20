#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a representation of the Pascal’s triangle of n
    """
    triangle = []
    if n <= 0:  # return empty list when 0 is given
        return triangle
    for i in range(n):  # loop thru
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)  # append to temporary list
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    # print(triangle)
    return triangle
