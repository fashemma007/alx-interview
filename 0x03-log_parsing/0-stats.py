#!/usr/bin/python3
"""This documents gather stats from stdin"""
import sys
import re

PATTERN = '^(([0-9]{1,3}.){4,4})...+.([0-9]{4,4}).([0-9]{2,2}).([0-9]{2,2})...\
+\"GET..[a-z]+.[0-9]+.HTTP/1.1\".[0-9]+.[0-9]+'


def check_line(lines):
    """line checker"""
    try:
        re.search(PATTERN, lines).group()
        return True
    except AttributeError:
        return False


def print_pretty(size, code_dict):
    """parse important data"""
    print("File size: {}".format(size))
    for key, value in sorted(code_dict.items()):
        if (value != 0):
            print("{}: {}".format(key, value))


if __name__ == '__main__':
    size = 0
    code_dict = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    try:
        line_counter = 0
        for line in sys.stdin:
            if check_line(line):
                line_counter += 1
                code = line.split()[7]
                size += int(line.split()[8])
                if code in code_dict:
                    code_dict[code] += 1
                if (line_counter % 10 == 0):
                    print_pretty(size, code_dict)
        print_pretty(size, code_dict)
    except KeyboardInterrupt:
        print_pretty(size, code_dict)
        raise
