#!/usr/bin/env python3
"""Measure runtime of asynchronous tasks executed in parallel."""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension four times in parallel.

    This function runs four instances of async_comprehension concurrently
    using asyncio.gather and calculates the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
