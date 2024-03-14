#!/usr/bin/env python3
"""A function that takes in a list of integers
and/or floats and returns the sum"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum up the elements of a list of integers
     and floats and return the result."""
    return sum(mxd_lst)
