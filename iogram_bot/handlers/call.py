from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, ContentType, ReplyKeyboardRemove
from aiogram import F
from ..loggin import log
from ..button import *
from ..utils import captcha
# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start", 'help']))
async def process_start_command(message: Message):
    await message.answer(text='Hello!\nits button command\n'
                              'q-request\n'
                              'z-share geo,contact, add request',
                         reply_markup=button.func_keyboard)
    log.bot_log(message.message_id)


# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@router.message(F.content_type.in_({ContentType.VOICE,
                                    ContentType.VIDEO,
                                    ContentType.ANIMATION,
                                    ContentType.STICKER,
                                    ContentType.PHOTO,
                                    ContentType.LOCATION,
                                    ContentType.CONTACT}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали контент который пока не поддерживается')
    log.bot_log(message.message_id)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@router.message(Text(text='q'))
async def process_start_command(message: Message):
    await message.answer(text='Чего кошки боятся больше?',
                         reply_markup=button.keyboard_q)


# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@router.message(Text(text='Собак 🦮'))
async def process_dog_answer(message: Message):
    await message.answer(text='Да, несомненно, кошки боятся собак. '
                              'Но вы видели как они боятся огурцов?',
                         reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@router.message(Text(text='Огурцов 🥒'))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов '
                              'кошки боятся больше',
                         reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Text(text='z'))
async def process_start_command(message: Message):
    await message.answer(text='Экспериментируем со специальными кнопками',
                         reply_markup=button.keyboard_z)


@router.message(Text(text='captcha'))
async def process_start_command(message: Message):
    await captcha.throw_captcha(message, 9)


@router.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)
    log.bot_log(message.message_id)

if __name__ == '__main__':
    pass
