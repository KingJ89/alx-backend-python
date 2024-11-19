#!/usr/bin/env python3
"""Collect 10 random numbers using async comprehension."""

from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collect 10 random floating-point numbers from an asynchronous generator.

    This function uses an asynchronous comprehension to iterate over the
    async_generator and collects its results into a list.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    result = [i async for i in async_generator()]
    return result
