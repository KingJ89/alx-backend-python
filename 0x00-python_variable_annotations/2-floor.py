#!/usr/bin/env python3
"""
This module defines a type-annotated function `floor` 
that returns the floor of a given float.
"""
import math

def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Args:
        n (float): The float number to be floored.

    Returns:
        int: The largest integer less than or equal to `n`.
    """
    return math.floor(n)
