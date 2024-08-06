#!/usr/bin/env python3
"""Still dealing with creating tasks async in python"""

import asyncio
import heapq
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all delays spawned from wait_random"""
    # define an empty list to take all the delays
    # delays = [wait_random(max_delay) for _ in range(n)]

    # return await asyncio.gather(*delays)

    # APPROACH TO RETURN DELAYS IN ASCENDING ORDER
    # NB INSERSTION SORT CAN BE USED, IF .gather method was used
    # to call the functions

    # empty list to hold all delays in ascending order
    delays = []
    # create tasks for coroutines to run n times
    # using task_wait_random instead asyncio.create_tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # using a heap to maintain order as delays complete
    heap = []

    for task in asyncio.as_completed(tasks):
        # create a delay for completed task
        delay = await task

        # use heapq to push completed task to heap
        heapq.heappush(heap, delay)

    # extracting elements fromt he heap to get them in ascending order
    while heap:
        delays.append(heapq.heappop(heap))

    return delays
