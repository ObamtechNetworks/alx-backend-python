#!/usr/bin/env python3
"""Using mypy to validate code"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return list(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
