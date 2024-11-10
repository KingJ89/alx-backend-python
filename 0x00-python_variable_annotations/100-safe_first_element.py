#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations"""
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of the sequence if it exists, otherwise return None."""
    return lst[0] if lst else None

