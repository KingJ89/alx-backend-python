#!/usr/bin/env python3
"""Measure the average runtime of executing wait_n concurrently."""

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of wait_n executed `n` times with a specified `max_delay`.

    Parameters:
    - n (int): The number of times to execute the coroutine.
    - max_delay (int): The maximum delay for each call to wait_n.

    Returns:
    - float: The average time taken per call.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start
    return total_time / n
