#!/usr/bin/env python3
"""Mixed lists of types"""

from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """A function that receives a mixed list of integers and floats

    Args:
        mxd_lst (Union[int, float]): A list containing integers and floats

    Returns:
        float: Returns the sum of the elements as a float
    """
    return float(sum(mxd_lst))
