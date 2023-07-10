import asyncio
import time
from typing import Any
from captcha.image import ImageCaptcha
from random import randint
from aiogram.types import Message, InputMediaPhoto

threw_integer: int = randint(1000, 9999)


def waiter_time(delay):
    time.sleep(delay)
    return True


async def throw_captcha(message: Message, temp_integer: int):
    pass




