#!/usr/bin/python3

"""Validates that a list of integers is comprised of valid utf-8 data"""


def validUTF8(data):
    """checks that data is utf-8 encoded"""

    if type(data) is list \
            and len(data) > 0 \
            and all(type(num) is int for num in data) \
            and all(num <= 127 and num >= 0 for num in data):
        return True
    else:
        return False
