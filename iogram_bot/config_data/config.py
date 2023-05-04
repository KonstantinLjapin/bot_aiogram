import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
from ..handlers import call


async def main():
    if not find_dotenv():
        exit('Переменные окружения не загружены т.к отсутствует файл .env')
    else:
        load_dotenv()
    API_TOKEN: str = os.environ.get('BOT_TOKEN')

    # Создаем объекты бота и диспетчера
    bot: Bot = Bot(token=API_TOKEN)
    bot_dispatcher: Dispatcher = Dispatcher()
    # Регистриуем роутеры в диспетчере
    bot_dispatcher.include_router(call.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await bot_dispatcher.start_polling(bot)
