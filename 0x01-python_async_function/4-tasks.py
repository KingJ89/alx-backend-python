#!/usr/bin/env python3
"""Create a function similar to wait_n but using task_wait_random."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times with a specified max_delay and return completion times in order.

    Parameters:
    - n (int): The number of tasks to run.
    - max_delay (int): The maximum delay for each task.

    Returns:
    - List[float]: A list of completion times in the order tasks complete.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
