#!/usr/bin/env python3
"""This module defines an asynchronous coroutine called async_generator."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """This couroutine returns a list of random numbers"""

    for i in range(10):
        number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield number
