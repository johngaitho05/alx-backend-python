#!/usr/bin/env python3
"""A function that takes in a list of interger
and/or floats and returns the sum"""
from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    return sum(mxd_lst)
