#!/usr/bin/env python3
"""The basics of async in python"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that takes in an integer argument
    (max_delay with default of 10)
    and waits for a random delay between 0 and max_delay
    (included and float value)seconds
    and eventually returns it
    """

    # use the random.uniform module to reference the delay value
    delay = random.uniform(0, float(max_delay))
    # wait using asyncio.sleep
    await asyncio.sleep(delay)
    # return the random value
    return delay
