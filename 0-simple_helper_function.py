#!/usr/bin/env python3
""" Function that takes two integers as args and returns a tuple."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing a start and end index
    Args:
        page: The page number
        page_size: The number of items
    Returns:
        return: A tuple containing the start and end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
