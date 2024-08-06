#!/usr/bin/env python3
"""To measure the runtime of our coroutines"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n
    Returns:
        total_time / n -> a float
    """
    # take note of start time
    start_time = time.perf_counter()
    # run the coroutine
    asyncio.run(wait_n(n, max_delay))
    # take note of the end time
    total_time = time.perf_counter() - start_time

    # return the average of the total time for each runs
    return total_time / n
