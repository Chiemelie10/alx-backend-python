#!/usr/bin/env python3
"""This module defines an asynchronous coroutine called async_generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """This couroutine yields a random number till the loop ends"""

    for _ in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
