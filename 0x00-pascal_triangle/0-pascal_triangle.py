#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a representation of the Pascal’s triangle of n
    """
    triangle = []  # initialize empty list to return
    if n <= 0:  # return empty list when 0 is given
        return triangle
    for i in range(n):  # loop from 0 to n
        temp_list = []  # initialize temporary list for each iteration
        # sub list creation loop
        for j in range(i+1):
            if j == 0 or j == i:
                # append 1 at beginning and end of lists
                temp_list.append(1)
            else:  # add 2 opposite values to get new value
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)  # append temp list to return list
    # print(triangle)
    return triangle
