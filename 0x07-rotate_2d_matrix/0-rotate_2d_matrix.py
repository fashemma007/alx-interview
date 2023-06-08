#!/usr/bin/python3
"""module docs for 0-rotate_2d_matrix.py"""


def rotate_2d_matrix(matrix) -> None:
    """rotates a 2D matrix in-place"""
    temp = []  # initialize empty list
    for item in matrix:
        temps = []  # initialize empty inner list
        # print(item)
        for item in matrix:  # for each inner list
            elem = item.pop(0)  # pop it's first item
            temps.insert(0, elem)  # add it to the start of the list
            # print(item)
            # print(temps)
        temp.append(temps)  # append to list to the mother list
    matrix.clear()  # reset/ clear the given list
    for item in temp:  # add all items back
        matrix.append(item)
