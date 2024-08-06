#!/usr/bin/env python3
"""Create tasks using asyncio"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an integer max_delay and returns an asyncio.Task

    Args:
        max_delay (int): an integer referecing delay length for task to run

    Returns:
        asyncio.Task: an object
    """
    tasks = asyncio.create_task(wait_random(max_delay))
    return tasks
