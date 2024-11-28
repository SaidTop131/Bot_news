from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU

# Создание объектов кнопок

but1 = KeyboardButton(text=LEXICON_RU['but1']) 
but2 = KeyboardButton(text=LEXICON_RU['but2'])
but3 = KeyboardButton(text=LEXICON_RU['but3'])


# Создаем объект клавиатуры, добавляя в нее кнопки
keyboard = ReplyKeyboardMarkup(keyboard = [[but1], [but2], [but3]],
                               resize_keyboard=True,
                               one_time_keyboard=True)