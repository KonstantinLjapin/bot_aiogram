import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv, find_dotenv
if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
BOT_TOKEN: str = os.environ.get('BOT_TOKEN')

if __name__ == '__main__':
    print(BOT_TOKEN)
