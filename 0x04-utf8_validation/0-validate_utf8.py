#!/usr/bin/python3
"""module docs for 0-validate_utf8.py"""

from typing import List


def validUTF8(data):  # type (list[int]) -> bool
    """
    The validUTF8 function takes in a list of integers and returns True if the
    list represents a valid UTF-8 encoding, or False otherwise.

    data `List[int]`: Store the data that is being passed into the function
    return: True if the data is a valid utf-8 encoding
    """
    data_len = len(data)  # get the length of the dataset
    i = 0  # initialize counter to 0
    while i < data_len:  # loop thru all elements in dataset
        num = data[i]
        num_binary = '{0:08b}'.format(num)

        # calculate the number of 1's
        num_chars = 0
        for char in num_binary:
            if char == '1':
                num_chars += 1
                continue
            break

        if num_chars == 1 or num_chars > 4:
            # 10XXX condition doesn't exist
            # only 1 to 4 bytes long
            return False

            # for 1 byte, num chars can be zero
        num_chars = num_chars - 1 if num_chars > 1 else 0

        check_till = i + num_chars
        if check_till >= data_len:
            # if there are not many required elements to check
            return False

        for j in range(i + 1, check_till + 1):
            curr_num = data[j]
            curr_num_binary = '{0:08b}'.format(curr_num)
            if curr_num_binary[:2] != '10':
                return False

        i = check_till + 1

    return True
