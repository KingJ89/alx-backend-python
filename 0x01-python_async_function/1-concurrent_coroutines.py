#!/usr/bin/env python3
"""Execute multiple coroutines concurrently with async."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute `wait_random` `n` times with a specified `max_delay`, 
    and return a list of all delays in ascending order.

    Parameters:
    - n (int): Number of times to call `wait_random`.
    - max_delay (int): Maximum delay for each `wait_random` call.

    Returns:
    - List[float]: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
