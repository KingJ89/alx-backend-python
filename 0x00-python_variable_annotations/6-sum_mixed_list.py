#!/usr/bin/env python3
"""Type-annotated function that sums a list of floats."""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """Calculate and return the sum of all floats in the list.
    
    Args:
        input_list (List[float]): A list of float numbers.
    
    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)
