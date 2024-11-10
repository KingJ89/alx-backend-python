#!/usr/bin/env python3
"""Type-annotated function make_multiplier that takes a float multiplier."""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a given float by a predefined multiplier.
    
    Args:
        multiplier (float): The value to multiply by.
    
    Returns:
        Callable[[float], float]: A function that takes a float and returns its product with the multiplier.
    """
    def multiplier_func(number: float) -> float:
        """Multiply the given number by the multiplier."""
        return number * multiplier
    
    return multiplier_func
