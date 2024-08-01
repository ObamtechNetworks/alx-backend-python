#!/usr/bin/env python3
"""complex types string/int/float to tuples"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A function that takes a string 'k'
    and an int OR float 'v'
    Then returns them as a float

    Args:
        k (str): A string
        v (Union[int, float]): An integer or float

    Returns:
        Tuple: Returns them as tuple, first element k: is a  string
        second element v: is the square of the int or float v
    """

    return (k, v * v)
