#!/usr/bin/env python3
"""Complex types annotations"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """A functiont that takes in a list of floats
    as arguments

    Args:
        input_list (List[float]): A list of floats

    Returns:
        float: Returns sum of the floats
    """
    return sum(input_list)
