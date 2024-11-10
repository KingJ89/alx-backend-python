#!/usr/bin/env python3
"""Type-annotated function that returns the length of each element in a list."""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each element and its length.
    
    Args:
        lst (Iterable[Sequence]): A list of sequences (like strings, lists, etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains 
                                    a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
