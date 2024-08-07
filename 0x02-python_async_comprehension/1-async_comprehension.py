#!/usr/bin/env python3
"""Async Comprehension"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers
    from async_generator using an async comprehension.
    Returns a list of the 10 random numbers.
    """
    return [number async for number in async_generator()]
