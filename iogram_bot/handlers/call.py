from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram import F
from ..loggin import log

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start", 'help']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
    log.bot_log(message.message_id)


# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@router.message(F.content_type.in_({ContentType.VOICE,
                                    ContentType.VIDEO,
                                    ContentType.ANIMATION,
                                    ContentType.STICKER,
                                    ContentType.PHOTO}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали контент который пока не поддерживается')
    log.bot_log(message.message_id)


@router.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)
    log.bot_log(message.message_id)


if __name__ == '__main__':
    pass
