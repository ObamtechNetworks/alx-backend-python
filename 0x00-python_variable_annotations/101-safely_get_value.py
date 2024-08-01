#!/usr/bin/env python3

from typing import Mapping, Any, Union, Optional, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T,
                                    Optional[None]
                                    ] = None) -> Union[Any, T]:
    """Safely get value from a dictionary

    Args:
        dct (Mapping[Any]): A dictionary
        key (Any): Key
        default (Union[T, Optional[None]], optional):
        Any type. Defaults to None.

    Returns:
        Union[Any, T]: Any type
    """
    if key in dct:
        return dct[key]
    else:
        return default
