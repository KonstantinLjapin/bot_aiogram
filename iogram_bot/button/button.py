from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import random
from typing import Any
# Создаем объекты кнопок
button_dog: KeyboardButton = KeyboardButton(text='Собак 🦮')
button_cucumber: KeyboardButton = KeyboardButton(text='Огурцов 🥒')

# Создаем объекты кнопок команд
button_1: KeyboardButton = KeyboardButton(text='q')
button_2: KeyboardButton = KeyboardButton(text='z')
button_3: KeyboardButton = KeyboardButton(text='captcha')
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
captcha_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем кнопки kb_bilder
contact_btn: KeyboardButton = KeyboardButton(
                                text='Отправить телефон',
                                request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(
                                text='Отправить геолокацию',
                                request_location=True)
poll_btn: KeyboardButton = KeyboardButton(
                                text='Создать опрос/викторину',
                                request_poll=KeyboardButtonPollType())
captcha_btn: KeyboardButton = KeyboardButton(
                                text='captcha')


# button_captcha
def captcha_keys(temp: int) -> list:
    """
     Take answer, generate objekt buttons, return list "buttons"
    :param temp: int answer of the captcha
    :return: list of "KeyboardButton" with answer
    """
    temp = str(temp)
    first_button: KeyboardButton = KeyboardButton(
        text=temp)
    next_button: KeyboardButton = KeyboardButton(
        text='joke')
    next_last_button: KeyboardButton = KeyboardButton(
        text='joke')
    last_button: KeyboardButton = KeyboardButton(
        text='joke')
    out_list = [first_button, next_button, next_last_button, last_button]
    random.shuffle(out_list)
    return out_list


# Добавляем кнопки в билдер fun
kb_builder.row(contact_btn, geo_btn, poll_btn, captcha_btn,  width=1)


def gen_captcha_button_builder(temp: int) -> Any:
    """trow int
       add buttons"""
    captcha_buttons = captcha_keys(temp)
    for i in range(len(captcha_buttons)):
        captcha_builder.add(captcha_buttons[i])

    keyboard_captcha: ReplyKeyboardMarkup = captcha_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True)

    return keyboard_captcha


# Создаем объект клавиатуры
keyboard_z: ReplyKeyboardMarkup = kb_builder.as_markup(
                                    resize_keyboard=True,
                                    one_time_keyboard=True)


if __name__ == '__main__':
    pass
