#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a string and an int/float."""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is the string k and
    the second element is the square of v.
    
    Args:
        k (str): A string key.
        v (Union[int, float]): An integer or float value.
    
    Returns:
        Tuple[str, float]: A tuple with the string and the squared value as a float.
    """
    return k, float(v ** 2)
