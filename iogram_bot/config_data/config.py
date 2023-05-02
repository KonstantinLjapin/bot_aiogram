import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
API_TOKEN: str = os.environ.get('BOT_TOKEN')


# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
bot_dispatcher: Dispatcher = Dispatcher()
