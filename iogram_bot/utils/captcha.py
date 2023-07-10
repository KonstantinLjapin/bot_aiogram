import asyncio
import os
import time
from typing import Any
from captcha.image import ImageCaptcha
from random import randint
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from ..button import button
threw_integer: int = randint(1000, 9999)


def waiter_time(delay):
    time.sleep(delay)
    return True


async def throw_captcha(message: Message, temp_integer: int):
    await message.answer("start catcha")
    cat = FSInputFile("iogram_bot/utils/cap.png")
    await message.answer_photo(cat, caption="caption")
    await message.answer(text='answer too captcha',
                         reply_markup=button.gen_captcha_button_builder(1234))
    await message.answer("reply_text", reply_markup=ReplyKeyboardRemove())




