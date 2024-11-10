#!/usr/bin/env python3
"""Create an asyncio Task without using an async function."""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that runs wait_random with a specified delay.

    Parameters:
    - max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
    - asyncio.Task: The created asyncio Task running wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
