#!/usr/bin/env python3
"""Duck tying => an iterable object"""

from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculates the length of a list items

    Args:
        lst (Iterable[Sequence]): takes an iterable

    Returns:
        List[Tuple[Sequence, int]]: a list of
    """
    return [(i, len(i)) for i in lst]
