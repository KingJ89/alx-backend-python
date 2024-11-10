#!/usr/bin/env python3
"""Use mypy to validate the piece of code and apply any changes."""
from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Returns a list with each integer in the tuple duplicated `factor` times."""
    zoomed_in: List[int] = [
            item for item in lst
            for _ in range(factor)
            ]
    return zoomed_in

array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
