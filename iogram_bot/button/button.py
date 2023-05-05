from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создаем объекты кнопок
button_dog: KeyboardButton = KeyboardButton(text='Собак 🦮')
button_cucumber: KeyboardButton = KeyboardButton(text='Огурцов 🥒')

# Создаем объекты кнопок команд
button_1: KeyboardButton = KeyboardButton(text='q')
button_2: KeyboardButton = KeyboardButton(text='z')
button_3: KeyboardButton = KeyboardButton(text='not exist')
button_4: KeyboardButton = KeyboardButton(text='not exist')
button_5: KeyboardButton = KeyboardButton(text='not exist')
button_6: KeyboardButton = KeyboardButton(text='not exist')
button_7: KeyboardButton = KeyboardButton(text='not exist')
button_8: KeyboardButton = KeyboardButton(text='not exist')
button_9: KeyboardButton = KeyboardButton(text='not exist')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard_q: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_dog, button_cucumber]])


# Создаем объект клавиатуры, добавляя в него кнопки
func_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                        keyboard=[[button_1, button_2, button_3],
                                  [button_4, button_5, button_6],
                                  [button_7, button_8, button_9]],
                        resize_keyboard=True)

# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn: KeyboardButton = KeyboardButton(
                                text='Отправить телефон',
                                request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(
                                text='Отправить геолокацию',
                                request_location=True)
poll_btn: KeyboardButton = KeyboardButton(
                                text='Создать опрос/викторину',
                                request_poll=KeyboardButtonPollType())

# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

# Создаем объект клавиатуры
keyboard_z: ReplyKeyboardMarkup = kb_builder.as_markup(
                                    resize_keyboard=True,
                                    one_time_keyboard=True)


