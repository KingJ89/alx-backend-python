#!/usr/bin/env python3
"""Add type annotations for parameters and return values."""
from typing import Mapping, Any, TypeVar, Optional, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """Return the value associated with `key` in `dct` if it exists, otherwise return `default`."""
    return dct[key] if key in dct else default
