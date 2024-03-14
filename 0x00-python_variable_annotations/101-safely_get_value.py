#!/usr/bin/env python3
"""
Given the parameters and the return values, add type annotations
to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""

from typing import TypeVar, Dict, Optional

K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> \
        Optional[V]:
    """Returns the value of key if it exists in the dict else the
    default value"""
    if key in dct:
        return dct[key]
    else:
        return default
