#!/usr/bin/env python
"""This module defines the function safe_first_element."""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This funtion returns the first element or None if no element."""

    if lst:
        return lst[0]
    else:
        return None
