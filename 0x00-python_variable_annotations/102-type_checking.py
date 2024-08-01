#!/usr/bin/env python3
"""Using mypy to validate code"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """A function that defines ann array or list of zoom levels

    Args:
        lst (Tuple): A tuple of zoom items
        factor (int, optional): An integer factor. Defaults to 2.

    Returns:
        List: Returns an array of zoom levels
    """
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return list(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
