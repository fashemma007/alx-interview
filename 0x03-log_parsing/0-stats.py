#!/usr/bin/python3
"""module docs for 0-stats.py"""

from signal import SIGINT, signal
import re
import sys

PATTERN = '^(([0-9]{1,3}.){4,4})...+.([0-9]{4,4}).([0-9]{2,2}).([0-9]{2,2})...\
+\"GET..[a-z]+.[0-9]+.HTTP/1.1\".[0-9]+.[0-9]+'

status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}


def logger(func):
    """logger decor"""
    def wrapper(*args, **kwargs):
        print(f"File size: {size}")
        for k, v in status_codes.items():
            print("{0}: {1}".format(k, v))
        return func(*args, **kwargs)
    return wrapper


@logger
def end(signum, frame):
    """function to call when ending the program"""
    exit(0)


def check_line(lines):
    """line checker"""
    try:
        re.search(PATTERN, lines).group()
        return True
    except AttributeError:
        return False


if __name__ == "__main__":
    signal(SIGINT, end)
    count = 0
    size = 0
    for line in sys.stdin:
        # get data and append to a list
        # if list == 10, sum and print it
        # else keep appending

        if check_line(line):
            count += 1
            stat_code = line.split()[-2]
            status_codes[stat_code] += 1
            size += int(line.split()[-1])
            if count % 10 == 0:
                print(f"File size: {size}")
                for k, v in status_codes.items():
                    print("{0}: {1}".format(k, v))
                # print(f"{status_codes} {count}")
        else:
            pass
