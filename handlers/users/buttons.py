from keyboard.default.knopki import menu
from loader import dp
from aiogram import types

from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text, Command


@dp.message_handler(Command("menu"))
async def knopki(message: types.Message):
    await message.answer("Выбери товар из списка...", reply_markup=menu)

@dp.message_handler(text="Апельсины")
async def orange(message: types.Message):
    await message.answer("Ты выбрал Апельсины", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Яблоки","Бананы"]))
async def apples(message: types.Message):
    await message.answer(f"Ты выбрал {message.text}")




