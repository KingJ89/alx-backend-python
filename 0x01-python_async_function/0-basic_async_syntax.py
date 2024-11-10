#!/usr/bin/env python3
"""An asynchronous coroutine that takes an integer argument and returns a float after a random delay."""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds, then return the delay.

    Parameters:
    - max_delay (int): Maximum number of seconds to wait. Defaults to 10.

    Returns:
    - float: The actual delay time.
    """
    new_rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(new_rand)
    return new_rand
