
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[  [KeyboardButton(text="Апельсины")],
                [KeyboardButton(text="Бананы"), KeyboardButton(text="Яблоки")],
                [KeyboardButton(text="Ананас"), KeyboardButton(text="Груша"),
                 KeyboardButton(text="Дыня"),KeyboardButton(text="Арбуз")],
             ],
    resize_keyboard=True
)


friends = ReplyKeyboardMarkup(
    keyboard=[
                [KeyboardButton(text="Юра"), KeyboardButton(text="Алина")],
                [KeyboardButton(text="Артем"), KeyboardButton(text="Даша")],
                [KeyboardButton(text="Надя"), KeyboardButton(text="Паша")],
             ],
    resize_keyboard=True
)


fruits = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Апельсины")],
                [KeyboardButton(text="Бананы"), KeyboardButton(text="Яблоки")],
              ],
resize_keyboard=True
)