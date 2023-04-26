import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv, find_dotenv
if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    pass
