#!/usr/bin/env python3
"""Annotating functions ---> complex typs"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that takes a float multiplier as  argument
    and then returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): The float value

    Returns:
        Callable: The callable function
    """
    def func(value: float) -> float:
        return value * multiplier
    return func
