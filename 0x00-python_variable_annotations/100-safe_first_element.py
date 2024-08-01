#!/usr/bin/env python3
"""Duck Typing first element of a sequence"""

from typing import Sequence, Any, Union, Optional


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, Optional[None]]:
    """A function that safely returns the first element from a list

    Args:
        lst (Sequence[Any]): List of sequence of any type

    Returns:
        Union[Any, Optional[None]]: Any type or None Type
    """
    if lst:
        return lst[0]
    else:
        return None
