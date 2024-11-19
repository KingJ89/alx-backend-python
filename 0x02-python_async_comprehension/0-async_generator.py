#!/usr/bin/env python3
"""Asynchronous generator that yields random floating-point numbers."""

import random
import asyncio
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Yield 10 random floating-point numbers between 0 and 10, with a 1-second delay.
    This asynchronous generator uses the random module to generate numbers and
    pauses for 1 second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
