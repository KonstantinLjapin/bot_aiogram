from ..config_data.config import bot_dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram import F
from ..loggin import log


# Этот хэндлер будет срабатывать на команду "/start"
@bot_dispatcher.message(Command(commands=["start", 'help']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
    log.bot_log(message.message_id)


# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@bot_dispatcher.message(F.content_type.in_({ContentType.VOICE,
                                            ContentType.VIDEO,
                                            ContentType.ANIMATION,
                                            ContentType.STICKER,
                                            ContentType.PHOTO}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали контент который пока не поддерживается')
    log.bot_log(message.message_id)


@bot_dispatcher.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)
    log.bot_log(message.message_id)


if __name__ == '__main__':
    pass
