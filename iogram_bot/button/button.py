from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup)

# Создаем объекты кнопок
button_dog: KeyboardButton = KeyboardButton(text='Собак 🦮')
button_cucumber: KeyboardButton = KeyboardButton(text='Огурцов 🥒')

# Создаем объекты кнопок команд
button_1: KeyboardButton = KeyboardButton(text='q')
button_2: KeyboardButton = KeyboardButton(text='not exist')
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